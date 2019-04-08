# ProyectoApis
Muchas veces nos toca trabajar con varias plataformas como Twitter, Facebook o Google para hacer llegar la información a todo el mundo, puesto que las distintas plataformas ofrecen diferentes servicios, como las notificaciones de Twitter o el almacenamiento de documentos en Dropbox, etc.

Nosotros nos hemos propuesto sintetizar el repetitivo trabajo del profesor, a la hora de publicar fechas de exámenes y notas de éstos, en un único proceso que se llevará a cabo transparente al usuario y que usará varias plataformas como puede ser Twitter y Google.

Obviamente, no estamos dando solución a un “gran” problema, pero la misma idea se puede extrapolar o ampliar a entornos y situaciones más complejos en un futuro. La programación de sistemas distribuidos hace posible que distintas plataformas web, que trabajan con diversos lenguajes, se puedan comunicar para dar soporte unos a otros.



# IDEA DEL PROYECTO

El proyecto consiste en desarrollar una pequeña aplicación, usando conocimientos de Python, HTML y programación de sistemas distribuidos, para facilitar el uso concurrente de varias plataformas de comunicación (en este caso Twitter y Google), a la hora de que el profesor usuario de la aplicación tenga varios medios de emisión de información a los alumnos.

Se usará Twitter como medio de notificación de cada una de las operaciones que haga el usuario. En cada tweet vendrá facilitado el link con el documento propio para un fácil acceso por los alumnos.

Usaremos Calendar para asignar fechas de exámenes que sean accesibles por los alumnos y Spreadsheets como medio de publicación de las notas de los exámenes, siempre con el link al documento Google.

Dropbox nos proporcionará el medio de almacenamiento de los archivos JSON, que el usuario cargará con la lista de los alumnos matriculados en la asignatura (matriculados, no sólo presentados al examen; contemplamos la nota en blanco como No presentado).

El proyecto se encuentra ejecutándose en cloud9 en el siguiente enlace:
https://proyectoapis-edsoncastro.c9.io/
