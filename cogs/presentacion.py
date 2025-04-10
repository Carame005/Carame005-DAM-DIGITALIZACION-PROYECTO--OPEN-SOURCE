import discord
from discord.ext import commands

class Presentation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Prints a message to the console when the cog is loaded and the bot is ready.
        """
        print("Presentation command loaded.")

    # Presentation command
    @commands.hybrid_command(name="presentacion", description="The bot introduces itself with a message")
    async def presentacion(self, ctx):
        """
        Sends an embedded message introducing the bot and explaining how to use commands.
        """
        embed = discord.Embed(
            title="Hello! I'm your bot 🤖",
            description="I'm here to help you with fun and useful commands.\n\n"
                        "You can try my commands using `/` or `!`.\n"
                        "For example: `/roast`, `/random_meme`, `/add_keyword`.",
            color=discord.Color.blue()
        )
        embed.set_footer(text="I hope to be useful in your server!")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Presentation(bot))
