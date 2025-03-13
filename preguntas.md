## 1.Ciclo de vida del dato (5b):
**¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?**
Al ser un bot de discord esta programado para manejar texto e imagenes, si el usuario asigna una palabra a una respuesta del bot esta se guardará en un archivo json en una carpeta con el id del servidor, lo mismo ocurre si se guarda una imagen/gif, se creará una carpeta si no existe ya y esta guardará todas las imagenes en esta.

Usando un comando tambien se pueden eliminar las palabras claves del archivo json.

**¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?**
Basicamente asignar una carpeta individual para cada servidor en el que opere el bot, asi no se confundirá a la hora de elegir la carpeta ya que la carpeta tiene el ID del servidor.

**Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?**


## 2.Almacenamiento en la nube (5f):
**Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?**


**¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?**


**Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?**
Tal vez usando una api o haciendo que esos archivos sean subidos a Google Drive automaticamente.

## 3.Seguridad y regulación (5i):
**¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?**


**¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?**


**Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?**
En principio la unica brecha de seguridad es que el token del bot se filtre, ya que sin este no puede funcionar, simplemente no compartas el token con nadie y todo debe estar bien, tal vez una medida para proteger esto sea asignar el token a una variable y ocultarlo.

## 4.Implicación de las THD en negocio y planta (2e):
**¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?**

**¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?**

**Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?**
Principalmente en el entorno del ocio, está planeado para ser una adición pequeña a un servidor de discord que tú puedas usar desde tu dispositivo, puede servir cómo una buena manera de introducir a personas principiantes en la creación de bots de discord.También te permite controlar que cosas hace o no el bot.

## 5.Mejoras en IT y OT (2f):
**¿Cómo puede tu software facilitar la integración entre entornos IT y OT?**

**¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?**

**Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?**


## 6.Tecnologías Habilitadoras Digitales (2g):
**¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?**

**¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?**

**Si no has utilizado THD, ¿cómo podrías implementarlas para enriquecer tu solución?**
