#AVISO IMPORTANTE, ESTA ES LA VERSION SIN MODULARIZAR, SI LA OTRA NO FUNCIONA USEN ESTA QUE SI LO HACE
#PUEDEN MOVER ESTE ARCHIVO A OTRA CARPETA SI ES NECESARIO

#DISCLAIMER, THIS IS A NON MODULARIZED VERSION, IF THE OTHER ONE DOESN'T WORK YOU CAN USE THIS THAT IT DOES,
#YOU CAN MOVE THIS ARCHIVE TO OTHER FOLDER IF NECCESARY

import discord
import os
import json
import imghdr
import random
from discord.ext import commands

TOKEN = #Your token here

# Crear el bot/bot create
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de insultos divertidos/roast list(you can change the messages)
roasts = [
    "Estás apollardao pishita",
    "Ere un papafrita illo",
    "Ere un pejiguero enserio",
    "Que te f*lle un pez",
    "¿Eres tonto o te duchas con paraguas?",
    "Eres más feo que pegarle a un padre con un calcetín sudao.",
    "Te voy a dar una hostia que te voy dejar la cara como un Picasso.",
    "¿Eres cortito?",
    "Eres tan tonto que tus células cerebrales están en la lista de especies en extinción",
    "Eres tan feo que, cuando naciste, el médico te tiró al aire y dijo: si vuela es un murciégalo.",
    "Eres más falso que un billete de 15€",
]

# Carpeta donde se almacenarán las imágenes (por ID del servidor)/folder where de images are saved
base_path = "memes"

# Función para cargar las palabras clave del archivo JSON
def load_keywords(guild_id):
    guild_folder = os.path.join(base_path, str(guild_id))
    json_file = os.path.join(guild_folder, "keywords.json")

    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            return json.load(f)
    else:
        return {}

# Función para guardar las palabras clave en el archivo JSON/save json fun
def save_keywords(guild_id, keywords):
    guild_folder = os.path.join(base_path, str(guild_id))
    json_file = os.path.join(guild_folder, "keywords.json")

    os.makedirs(guild_folder, exist_ok=True)
    with open(json_file, "w") as f:
        json.dump(keywords, f, indent=4)

# Evento para detectar mensajes y responder a palabras clave/event to detect keywords
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignorar mensajes del bot

    keywords = load_keywords(message.guild.id)
    for keyword, response in keywords.items():
        if keyword.lower() in message.content.lower():
            await message.channel.send(response)
            break  # Responder solo una vez por mensaje

    await bot.process_commands(message)

# Comando Slash para insultar a un usuario/slash command to roast someone
@bot.tree.command(name="roast", description="Insulta a un usuario de manera divertida")
async def roast(interaction: discord.Interaction, user: discord.Member):
    roast_message = random.choice(roasts)  # Seleccionar un insulto aleatorio
    await interaction.response.send_message(f"¡{user.mention}! {roast_message}")

# Comando para guardar una imagen/command ! to save an image
@bot.command(name="save_meme", help="Guarda una imagen adjunta al mensaje")
async def save_meme(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            try:
                # Crear las carpetas del servidor e imágenes si no existen
                guild_folder = os.path.join(base_path, str(ctx.guild.id))
                images_folder = os.path.join(guild_folder, "images")
                os.makedirs(images_folder, exist_ok=True)

                # Ruta temporal para guardar la imagen
                image_path = os.path.join(images_folder, attachment.filename)

                # Descargar el archivo adjunto
                await attachment.save(image_path)

                # Validar si el contenido es una imagen válida
                img_type = imghdr.what(image_path)
                if img_type in ['jpeg', 'png', 'gif']:
                    await ctx.send(f"¡Meme guardado! La imagen '{attachment.filename}' es válida y se ha almacenado.")
                else:
                    os.remove(image_path)  # Eliminar archivo no válido
                    await ctx.send(f"El archivo '{attachment.filename}' no es una imagen válida.")
            except Exception as e:
                await ctx.send(f"Error al procesar el archivo '{attachment.filename}': {e}")
    else:
        await ctx.send("Este mensaje no contiene ninguna imagen adjunta.")

# Comando para obtener un meme aleatorio/command to get a random meme
@bot.tree.command(name="random_meme", description="Obtiene un meme aleatorio del servidor")
async def random_meme(interaction: discord.Interaction):
    guild_id = str(interaction.guild.id)
    images_folder = os.path.join(base_path, guild_id, "images")

    # Verificar si la carpeta existe y contiene imágenes
    if os.path.exists(images_folder) and os.listdir(images_folder):
        meme_files = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        
        if meme_files:
            meme_file = random.choice(meme_files)  # Seleccionar un archivo aleatorio
            meme_path = os.path.join(images_folder, meme_file)
            
            # Enviar la imagen seleccionada
            await interaction.response.send_message(file=discord.File(meme_path))
        else:
            await interaction.response.send_message("No se encontraron memes válidos en este servidor.")
    else:
        await interaction.response.send_message("No hay memes guardados en este servidor. ¡Agrega algunos usando el comando correspondiente!")

# Evento para manejar cuando el bot se conecta/event to manage when the bot connects
@bot.event
async def on_ready():
    try:
        # Sincronización de comandos para todos los servidores
        await bot.tree.sync()
        print(f'{bot.user} está conectado. Comandos Slash sincronizados globalmente.')
    except Exception as e:
        print(f"Error al sincronizar los comandos: {e}")

# Comando Slash para mostrar las palabras clave/slash command to show keywords
@bot.tree.command(name="show_keywords", description="Muestra las palabras clave del servidor")
async def show_keywords(interaction: discord.Interaction):
    guild_id = interaction.guild.id
    keywords = load_keywords(guild_id)

    if keywords:
        keyword_list = "\n".join([f"{key}: {value}" for key, value in keywords.items()])
        await interaction.response.send_message(f"Palabras clave en este servidor:\n{keyword_list}")
    else:
        await interaction.response.send_message("No hay palabras clave definidas en este servidor.")

# Comando Slash para agregar una palabra clave/slash command to add a keyword
@bot.tree.command(name="add_keyword", description="Agrega una palabra clave con su respuesta")
async def add_keyword(interaction: discord.Interaction, keyword: str, response: str):
    guild_id = interaction.guild.id
    keywords = load_keywords(guild_id)

    if keyword.lower() in keywords:
        await interaction.response.send_message(f"La palabra clave '{keyword}' ya existe.")
    else:
        keywords[keyword.lower()] = response
        save_keywords(guild_id, keywords)
        await interaction.response.send_message(f"¡Palabra clave '{keyword}' añadida con la respuesta: '{response}'!")

# Comando Slash para eliminar una palabra clave/slash command to delete a keyword
@bot.tree.command(name="delete_keyword", description="Elimina una palabra clave del bot")
async def delete_keyword(interaction: discord.Interaction, keyword: str):
    guild_id = interaction.guild.id
    keywords = load_keywords(guild_id)

    if keyword.lower() in keywords:
        del keywords[keyword.lower()]  # Eliminar la palabra clave
        save_keywords(guild_id, keywords)  # Guardar los cambios
        await interaction.response.send_message(f"✅ La palabra clave '{keyword}' ha sido eliminada.")
    else:
        await interaction.response.send_message(f"⚠️ La palabra clave '{keyword}' no existe.")


# Comando de presentación/introduction command(put your own message)
@bot.tree.command(name="presentacion", description="El bot se presenta con un mensaje")
async def presentacion(interaction: discord.Interaction):
    embed = discord.Embed(
        title="¡Hola! Soy Carameloh, un bot creado por Carame05.\n"
        "Puedo parecer adorable pero soy un ser lleno de maldad pura.",
        description="Estoy aquí para ayudarte con comandos divertidos y útiles.\n\n"
                    "Puedes probar mis comandos con `/` o `!`.\n"
                    "Por ejemplo: `/roast`, `/random_meme`, `/add_keyword`.",
        color=discord.Color.blue()
    )
    embed.set_footer(text="¡Espero ser útil en tu servidor!")

    await interaction.response.send_message(embed=embed)


# Iniciar el bot/start bot
bot.run(TOKEN)

