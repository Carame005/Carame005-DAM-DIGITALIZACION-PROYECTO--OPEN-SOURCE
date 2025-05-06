DISCLAIMER: Este bot es con fines ludicos, por lo cual no posee cualidades realmente aplicables en el fin empresarial más allá de servir como método de entretenimiento.

## Criterio 6a) Objetivos estratégicos:
### ¿Qué objetivos estratégicos específicos de la empresa aborda tu software?
El bot aborda la necesidad de fomentar la participación y la interacción entre los miembros de una comunidad interna, promoviendo un ambiente más dinámico y entretenido. Además, automatiza tareas repetitivas como respuestas frecuentes o juegos interactivos.
### ¿Cómo se alinea el software con la estrategia general de digitalización?
Contribuye a la digitalización interna al introducir un canal de comunicación automatizado y accesible desde Discord, reduciendo la dependencia de herramientas tradicionales como correos o formularios físicos para algunas interacciones internas.
## Criterio 6b) Áreas de negocio y comunicaciones:
### ¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?
Como tal, ninguna, podría entrar dentro de las de comunicación ya que puede ser personalizado para crear avisos o repetir palabras clave, tambien almacenar informacion.
### ¿Qué impacto operativo esperas en las operaciones diarias?
Esperamos una mejora del ambiente laboral, mayor confianza entre miembros, risas y algo con lo que aligerar la carga de trabajo.
## Criterio 6c) Áreas susceptibles de digitalización:
### ¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?
La gestión del ocio interno, feedback informal entre empleados, y la automatización de pequeñas tareas administrativas o de comunicación (como celebraciones de cumpleaños, anuncios automáticos, etc.).
### ¿Cómo mejorará la digitalización las operaciones en esas áreas?
Permite una interacción más fluida, disminuye el tiempo invertido en tareas repetitivas, y hace más eficiente el uso de canales digitales mediante respuestas automáticas e interacciones instantáneas.
## Criterio 6d) Encaje de áreas digitalizadas (AD):
### ¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?
El bot puede funcionar como puente entre áreas tradicionales y digitales, notificando eventos, recopilando datos informales o sugerencias de quienes no usan herramientas más complejas.
### ¿Qué soluciones o mejoras propondrías para integrar estas áreas?
Incluir funcionalidades como exportación de datos del bot a informes simples (CSV o PDF), así como integraciones básicas con herramientas de gestión como Trello o Google Sheets para extender su utilidad a departamentos más estructurados.
## Criterio 6e) Necesidades presentes y futuras:
### ¿Qué necesidades actuales de la empresa resuelve tu software?
Resuelve la necesidad de contar con una herramienta de entretenimiento interna, automatización ligera de tareas sociales, y dinamización de comunidades dentro de la empresa. A futuro, puede escalarse para incluir encuestas, minijuegos educativos o control de participación en eventos.
## Criterio 6f) Relación con tecnologías:
### ¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?
Se emplean tecnologías como:
-Discord API (comunicación automatizada)
-Python (automatización)
-Archivos JSON (almacenamiento ligero y rápido)
Estas permiten implementar soluciones simples y funcionales sin depender de servidores externos, lo cual es útil para equipos pequeños o prototipos internos.
### ¿Qué beneficios específicos aporta la implantación de estas tecnologías?
-Bajo coste de mantenimiento
-Fácil personalización
-Rápida iteración
-Fácil escalabilidad funcional
## Criterio 6g) Brechas de seguridad:
### ¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?
Que el token del bot se filtre.
### ¿Qué medidas concretas propondrías para mitigarlas?
Almacenamiento seguro de tokens en archivos `.env` no compartidos
## Criterio 6h) Tratamiento de datos y análisis:
### ¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?
Se usan archivos JSON como base de datos local. La lectura y escritura se realiza mediante funciones que validan la estructura antes de actualizar cualquier dato, evitando corrupción del archivo.
### ¿Qué haces para garantizar la calidad y consistencia de los datos?
-Validación de datos antes de guardarlos
-Creación de backups automáticos de los archivos JSON (En proceso)
-Control de errores y manejo de excepciones en todas las operaciones de lectura/escritura

