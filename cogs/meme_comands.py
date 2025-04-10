import discord
import os
import imghdr
import random
from discord.ext import commands
from config import BASE_PATH

class MemeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to save an attached image from a message
    @commands.command(name="save_meme", help="Saves an image attached to the message")
    async def save_meme(self, ctx):
        """
        Saves image attachments from the user's message to the server-specific directory.
        Only valid image formats (jpeg, png, gif) are allowed.
        """
        if ctx.message.attachments:
            guild_folder = os.path.join(BASE_PATH, str(ctx.guild.id), "images")
            os.makedirs(guild_folder, exist_ok=True)

            for attachment in ctx.message.attachments:
                image_path = os.path.join(guild_folder, attachment.filename)
                await attachment.save(image_path)

                img_type = imghdr.what(image_path)
                if img_type in ['jpeg', 'png', 'gif']:
                    await ctx.send(f"Meme saved! The image '{attachment.filename}' is valid.")
                else:
                    os.remove(image_path)
                    await ctx.send(f"The file '{attachment.filename}' is not a valid image.")
        else:
            await ctx.send("This message does not contain any attached images.")

    # Command to send a random image from the saved memes
    @commands.command(name="random_meme", help="Fetches a random meme from the server")
    async def random_meme(self, ctx):
        """
        Sends a random meme image from the server's image directory.
        Only valid image formats are considered.
        """
        images_folder = os.path.join(BASE_PATH, str(ctx.guild.id), "images")

        if os.path.exists(images_folder) and os.listdir(images_folder):
            meme_files = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            if meme_files:
                meme_file = random.choice(meme_files)
                meme_path = os.path.join(images_folder, meme_file)
                await ctx.send(file=discord.File(meme_path))
            else:
                await ctx.send("No valid memes were found.")
        else:
            await ctx.send("There are no saved memes in this server.")

async def setup(bot):
    await bot.add_cog(MemeCommands(bot))
