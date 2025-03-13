import discord
import os
import imghdr
import random
from discord.ext import commands
from config import BASE_PATH

class MemeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Command ! to save a image
    @commands.command(name="save_meme", help="Guarda una imagen adjunta al mensaje")
    async def save_meme(self, ctx):
        if ctx.message.attachments:
            guild_folder = os.path.join(BASE_PATH, str(ctx.guild.id), "images")
            os.makedirs(guild_folder, exist_ok=True)

            for attachment in ctx.message.attachments:
                image_path = os.path.join(guild_folder, attachment.filename)
                await attachment.save(image_path)

                img_type = imghdr.what(image_path)
                if img_type in ['jpeg', 'png', 'gif']:
                    await ctx.send(f"¡Meme guardado! La imagen '{attachment.filename}' es válida.")
                else:
                    os.remove(image_path)
                    await ctx.send(f"El archivo '{attachment.filename}' no es una imagen válida.")
        else:
            await ctx.send("Este mensaje no contiene ninguna imagen adjunta.")
    #Command to send a random image
    @commands.command(name="random_meme", help="Obtiene un meme aleatorio del servidor")
    async def random_meme(self, ctx):
        images_folder = os.path.join(BASE_PATH, str(ctx.guild.id), "images")

        if os.path.exists(images_folder) and os.listdir(images_folder):
            meme_files = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            if meme_files:
                meme_file = random.choice(meme_files)
                meme_path = os.path.join(images_folder, meme_file)
                await ctx.send(file=discord.File(meme_path))
            else:
                await ctx.send("No se encontraron memes válidos.")
        else:
            await ctx.send("No hay memes guardados en este servidor.")

async def setup(bot):
    await bot.add_cog(MemeCommands(bot))
