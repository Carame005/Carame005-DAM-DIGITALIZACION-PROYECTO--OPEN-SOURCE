import discord
import random
from discord.ext import commands

roasts = [
    "¿Sabías que las piedras tienen más cerebro que tú?",
    "Si fueras un vegetal, serías una cebolla: molesto y con muchas capas.",
    "Eres como un software sin actualizaciones: lento y obsoleto.",
    "Tu cerebro es como un disco duro: lleno, pero sin espacio para nada útil.",
    "Te seguiría el resto de mi vida, pero mi perro me pidió que no lo hiciera.",
    "Tienes la misma cantidad de sentido común que un paraguas en el desierto.",
    "Eres la razón por la que algunos animales se comen a sus crías.",
    "Te miro y veo cómo la evolución retrocede.",
]

class RoastCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Roast command
    @commands.command(name="roast", help="Insulta a un usuario de manera divertida")
    async def roast(self, ctx, user: discord.Member):
        roast_message = random.choice(roasts)
        await ctx.send(f"{user.mention}, {roast_message}")

async def setup(bot):
    await bot.add_cog(RoastCommands(bot))
