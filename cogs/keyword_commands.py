import discord
from discord.ext import commands
from config import BASE_PATH
from utils.data_utils import load_keywords, save_keywords

class KeywordCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Listens for incoming messages and checks if any keyword matches.
        If a match is found, sends the associated response.
        """
        if message.author == self.bot.user:
            return

        keywords = load_keywords(message.guild.id)
        for keyword, response in keywords.items():
            if keyword.lower() in message.content.lower():
                await message.channel.send(response)
                break

        await self.bot.process_commands(message)

    # Command to show all registered keywords
    @commands.command(name="show_keywords", help="Displays the server's registered keywords")
    async def show_keywords(self, ctx):
        """
        Shows all keywords and their responses defined for the server.
        """
        keywords = load_keywords(ctx.guild.id)
        if keywords:
            response = "\n".join([f"{key}: {value}" for key, value in keywords.items()])
            await ctx.send(f"Keywords in this server:\n{response}")
        else:
            await ctx.send("There are no defined keywords.")

    # Command to add a new keyword and its associated response
    @commands.command(name="add_keyword", help="Adds a new keyword with a response")
    async def add_keyword(self, ctx, keyword: str, response: str):
        """
        Adds a new keyword and its response to the server's keyword list.
        """
        keywords = load_keywords(ctx.guild.id)
        if keyword.lower() in keywords:
            await ctx.send(f"The keyword '{keyword}' already exists.")
        else:
            keywords[keyword.lower()] = response
            save_keywords(ctx.guild.id, keywords)
            await ctx.send(f"Keyword '{keyword}' added with response: '{response}'")

    # Command to delete a keyword from the list
    @commands.command(name="delete_keyword", description="Removes a keyword from the bot")
    async def delete_keyword(interaction: discord.Interaction, keyword: str):
        """
        Deletes a keyword from the server's keyword list if it exists.
        """
        guild_id = interaction.guild.id
        keywords = load_keywords(guild_id)

        if keyword.lower() in keywords:
            del keywords[keyword.lower()] 
            save_keywords(guild_id, keywords)  
            await interaction.response.send_message(f"✅ The keyword '{keyword}' has been removed.")
        else:
            await interaction.response.send_message(f"⚠️ The keyword '{keyword}' does not exist.")

async def setup(bot):
    await bot.add_cog(KeywordCommands(bot))
