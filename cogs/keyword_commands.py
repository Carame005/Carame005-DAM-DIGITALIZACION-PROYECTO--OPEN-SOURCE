import discord
from discord.ext import commands
from config import BASE_PATH
from utils.data_utils import load_keywords, save_keywords

class KeywordCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        keywords = load_keywords(message.guild.id)
        for keyword, response in keywords.items():
            if keyword.lower() in message.content.lower():
                await message.channel.send(response)
                break

        await self.bot.process_commands(message)
    #Command to show keywords
    @commands.command(name="show_keywords", help="Muestra las palabras clave del servidor")
    async def show_keywords(self, ctx):
        keywords = load_keywords(ctx.guild.id)
        if keywords:
            response = "\n".join([f"{key}: {value}" for key, value in keywords.items()])
            await ctx.send(f"Palabras clave en este servidor:\n{response}")
        else:
            await ctx.send("No hay palabras clave definidas.")
    #Command to add keywords
    @commands.command(name="add_keyword", help="Agrega una palabra clave con su respuesta")
    async def add_keyword(self, ctx, keyword: str, response: str):
        keywords = load_keywords(ctx.guild.id)
        if keyword.lower() in keywords:
            await ctx.send(f"La palabra clave '{keyword}' ya existe.")
        else:
            keywords[keyword.lower()] = response
            save_keywords(ctx.guild.id, keywords)
            await ctx.send(f"Palabra clave '{keyword}' añadida con la respuesta: '{response}'")
    #Command to delete keywords
    @commands.command(name="delete_keyword", description="Elimina una palabra clave del bot")
    async def delete_keyword(interaction: discord.Interaction, keyword: str):
        guild_id = interaction.guild.id
        keywords = load_keywords(guild_id)

        if keyword.lower() in keywords:
            del keywords[keyword.lower()] 
            save_keywords(guild_id, keywords)  
            await interaction.response.send_message(f"✅ La palabra clave '{keyword}' ha sido eliminada.")
        else:
            await interaction.response.send_message(f"⚠️ La palabra clave '{keyword}' no existe.")

async def setup(bot):
    await bot.add_cog(KeywordCommands(bot))
