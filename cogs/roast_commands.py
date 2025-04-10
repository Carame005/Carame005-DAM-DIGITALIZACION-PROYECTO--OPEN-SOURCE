import discord
import random
from discord.ext import commands

# List of playful roast messages in English
roasts = [
    "Did you know that rocks have more brain cells than you?",
    "If you were a vegetable, you'd be an onion: annoying and with too many layers.",
    "You're like outdated software: slow and obsolete.",
    "Your brain is like a hard drive: full, but with no space for anything useful.",
    "I'd follow you for the rest of my life, but my dog asked me not to.",
    "You have as much common sense as an umbrella in the desert.",
    "You're the reason some animals eat their young.",
    "I look at you and see evolution going backwards.",
]

class RoastCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Roast command
    @commands.command(name="roast", help="Sends a playful insult to a user")
    async def roast(self, ctx, user: discord.Member):
        """
        Sends a randomly selected roast message mentioning the specified user.
        """
        roast_message = random.choice(roasts)
        await ctx.send(f"{user.mention}, {roast_message}")

async def setup(bot):
    await bot.add_cog(RoastCommands(bot))
