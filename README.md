# **Descripción del Proyecto: Bot de Discord en Python**  

## Motivación  
¡Bienvenidos a mi primer proyecto open-source! Se trata de un script en Python diseñado para programar un bot de Discord.  

La principal razón para desarrollar este proyecto fue la necesidad de contar con un bot personalizado para mis servidores y los de mis amigos. Quería algo con diversas funcionalidades que pudiéramos probar y expandir con el tiempo.  

Además, este proyecto está pensado para ayudar a programadores novatos interesados en el desarrollo de bots para Discord. Con este código base, podrán descargarlo, probarlo y modificarlo a su gusto. También estoy abierto a sugerencias y mejoras para seguir evolucionando el bot con el tiempo.  

## Instrucciones de Uso  
Las instrucciones detalladas están en el propio código, pero aquí tienes un resumen:  

1. Abre el archivo `config.py` y pega el **token de tu bot** en formato de cadena (`"tu_token_aquí"`).  
2. En el mismo archivo, puedes personalizar la configuración, como la carpeta donde se guardarán los archivos.  
3. Ejecuta el script desde el archivo `main.py` para activar el bot.  
4. **Nota:** Si los comandos no responden inmediatamente, puede deberse a un pequeño retraso en la sincronización con Discord. Solo espera unos minutos y deberían aparecer.  

## Ejemplo de Funcionalidad  
Uno de los comandos básicos del bot es:  

- `!savememe`: Si adjuntas una imagen al usar este comando, el bot la guardará automáticamente en una carpeta específica.  
  - La ubicación de almacenamiento se define en `config.py`.  
  - Las imágenes se organizan por el ID del servidor para evitar conflictos al usar el bot en múltiples servidores.  

Para más información sobre funcionalidades adicionales, consulta el apartado **Wiki** del repositorio.  

---

