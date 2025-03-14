LMS


Singleton: Conexión a servidor central
Builder: Crear actividades para los alumnos
Strategy: Cargar diferentes tipos de actividades (examenes, actividades,pdfs) 
Observer: Notificar de nuevas actividades

Justificacion:
    Singleton: Se utiliza el patrón singleton para mantener una sola conexion al servidor central, 
    se eligio este patron de diseño por su sencillez y funcion de mantener una sola instancia
    activa.
    El patrón abarca las clases:
        ConexionServer -> Clase que representa una conexión única al servidor

    Builder: Se utiliza el patrón Builder en la creacion de asignaciones debido a que estas pueden tener 
    una variedad de funciones, como subir archivos, ver un pdf, abrir un link, mostrar un formulario con 
    preguntas, etc. El patron Builder nos permite tener muchas funcionalidades y utilizar las necesarias 
    para las funciones que requiera cada asignacion

    Strategy: El patron Strategy nos permite cambiar la funcionalidad dependiendo de diferentes parametros, 
    en este caso se utiliza para interpretar la asignacion creada por el Builder. Por ejemplo, el builder
    crea una asignacion en la que el profesor sube un archivo pdf, implementa una formulario, etc.

    Observer: Este patrón se utiliza para enviar notificaciones a los usuarios como podría ser una alumno
    acerca de alguna tarea asignada, como un profesor al cual se le ha enviado una tarea asignada por este.
    El patrón abarca las clases:
        Publicador -> "Publica" los cambios a los suscriptores(alumnos o profesores) y les notifica acerca
                        de los eventos que se le manden
        Suscriptor -> Clase base abstracta de un suscriptore
        SuscriptorAlumno -> Clase especifíca de Suscriptor para notificar a un alumno
        SuscriptorProfesor -> Clase especifíca de Suscriptor para notificar a un profesor
    