LMS


Singleton: Conexion a servidor central
Builder: Crear actividades para los alumnos
Strategy: Cargar diferentes tipos de actividades (examenes, actividades,pdfs) 
Observer: Notificar de nuevas actividades

Justificacion:
    Singleton: Se utiliza el patron singleton para mantener una sola conexion al servidor central, 
    se eligio este patron de diseño por su sencilleza y funcion de mantener una sola instancia
    activa.

    Builder: Se utiliza el patron Builder en la creacion de asignaciones debido a que estas pueden tener 
    una variedad de funciones, como subir archivos, ver un pdf, abrir un link, mostrar un formulario con 
    preguntas, etc. El patron Builder nos permite tener muchas funcionalidades y utilizar las necesarias 
    para las funciones que requiera cada asignacion

    Strategy: El patron Strategy nos permite cambiar la funcionalidad dependiendo de diferentes parametros, 
    en este caso se utiliza para interpretar la asignacion creada por el Builder. Por ejemplo, el builder
    crea una asignacion en la que el profesor sube un archivo pdf, implementa una formulario 