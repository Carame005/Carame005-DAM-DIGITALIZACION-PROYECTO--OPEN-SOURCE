import discord
from discord.ext import commands
from config import TOKEN
import os

print("Ruta actual del script:", os.getcwd())  # Verifica la ruta actual
print("Archivos en el directorio actual:", os.listdir())  # Verifica los archivos

# Configurar los intents del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear instancia del bot
bot = commands.Bot(command_prefix="!", intents=intents)


# Cargar los módulos (cogs)
cog_folder = "cogs"
print("Contenido de la carpeta cogs:", os.listdir(cog_folder)) 
for filename in os.listdir(cog_folder):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    await bot.tree.sync()  # Sincronizar comandos de barra (/)
    print(f"{bot.user} está conectado.")

# Iniciar el bot
bot.run(TOKEN)
