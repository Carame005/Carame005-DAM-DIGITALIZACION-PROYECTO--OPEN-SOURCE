import discord
from discord.ext import commands

class Presentation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Comando de presentación cargado.")
    #Presentation command
    @commands.hybrid_command(name="presentacion", description="El bot se presenta con un mensaje")
    async def presentacion(self, ctx):
        embed = discord.Embed(
            title="¡Hola! Soy tu bot 🤖",
            description="Estoy aquí para ayudarte con comandos divertidos y útiles.\n\n"
                        "Puedes probar mis comandos con `/` o `!`.\n"
                        "Por ejemplo: `/roast`, `/random_meme`, `/add_keyword`.",
            color=discord.Color.blue()
        )
        embed.set_footer(text="¡Espero ser útil en tu servidor!")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Presentation(bot))
