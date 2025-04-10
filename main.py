import discord
from discord.ext import commands
from config import TOKEN
import os

# Debugging: check current working directory and contents
print("Current script path:", os.getcwd())
print("Files in current directory:", os.listdir())

# Configure bot intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Load modules (cogs)
cog_folder = "cogs"
print("Contents of the 'cogs' folder:", os.listdir(cog_folder))
for filename in os.listdir(cog_folder):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    """
    Event that is triggered when the bot is ready.
    It also syncs slash commands with Discord.
    """
    await bot.tree.sync()  # Sync slash (/) commands
    print(f"{bot.user} is now connected.")

# Start the bot
bot.run(TOKEN)
