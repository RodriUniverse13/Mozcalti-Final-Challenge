class Asignacion:
    """
    Clase que representa una asignacion de tarea, examen o proyecto con sus respectivos atributos.
    Esta clase utiliza el patron Builder para crear una asignacion de tarea, examen o proyecto.
    
    Atributos:
    -------
        archivos (list): 
            Lista de archivos de la asignacion.
        descripcion (str): 
            Descripcion de la asignacion.
        nombre (str): 
            Nombre de la asignacion.
        questions (list): 
            Lista de preguntas de la asignacion.
        fecha_entrega (str): 
            Fecha de entrega de la asignacion.
    
    Metódos:
    -------
        __init__: 
            Inicializa la clase con una lista de archivos, descripcion, nombre, preguntas y fecha de entrega.
        agregar_archivo: 
            Agrega un archivo a la lista de archivos de la asignacion.
    """
    def __init__(self):
        self.archivos = []
        self.descripcion = ""
        self.nombre = ""
        self.questions = []
        self.fecha_entrega = ""
    
    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)

class Creador:
    """
    Clase que crea una asignacion de tarea, examen o proyecto con sus respectivos atributos.
    Esta clase utiliza el patron Builder para crear una asignacion de tarea, examen o proyecto.
    
    Metódos:
    -------
        agregar_desc: 
            Agrega una descripcion a la asignacion.
        agregar_nombre: 
            Agrega un nombre a la asignacion.
        agregar_pregunta: 
            Agrega una pregunta a la asignacion.
        asignar_fecha_entrega: 
            Asigna una fecha de entrega a la asignacion.
        agregar_archivo: 
            Agrega un archivo a la asignacion.
        __init__: 
            Inicializa la clase con una instancia de Asignacion.
    """
    
    def __init__(self):
        self.asignacion = Asignacion()
    
    def agregar_desc(self, desc):
        """
        Función para agregar una descripcion a la asignacion.
        
        Parámetros:
        ----------
            desc (str): 
            Descripcion de la asignacion.
        
        Retorna:
        -------
            self: 
            Retorna la instancia de la clase Creador con la descripción agregada.
        """
        self.asignacion.descripcion = desc
        return self
    
    def agregar_nombre(self, nombre):
        """
        Función para agregar un nombre a la asignación.
        
        Parámetros:
        ----------
            nombre (str): 
            Nombre de la asignación.
        
        Retorna:
        -------
            self: 
            Retorna la instancia de la clase Creador con el nombre agregado.
        """
        self.asignacion.nombre = nombre
        return self
    
    def agregar_pregunta(self, pregunta):
        """
        Función para agregar una pregunta a la asignacion.
        
        Parámetros:
        ----------
            pregunta (str): 
            Pregunta de la asignacion.
        
        Retorna:
        -------
            self: 
            Retorna la instancia de la clase Creador con la pregunta agregada.
        """
        self.asignacion.questions.append(pregunta)
        return self
    
    def asignar_fecha_entrega(self, fecha):
        """
        Función para asignar una fecha de entrega a la asignacion.
        
        Parámetros:
        ----------
            fecha (str): 
            Fecha de entrega de la asignacion.
        
        Retorna:
        -------
            self: 
            Retorna la instancia de la clase Creador con la fecha de entrega agregada.
        """
        self.asignacion.fecha_entrega = fecha
        return self
    
    def agregar_archivo(self, archivo):
        """
        Función para agregar un archivo a la asignacion.
        
        Parámetros:
        ----------
            archivo (str): 
            Archivo de la asignacion.
        
        Retorna:
        -------
            self: 
            Retorna la instancia de la clase Creador con el archivo agregado.
        """
        self.asignacion.archivos.append(archivo)
        return self

class Asignador:
    """
    Clase que asigna una tarea, examen o proyecto a un estudiante.
    Esta clase utiliza el patron Builder para crear una asignacion de tarea, examen o proyecto.
    
    Metódos:
    -------
        asignar_tarea: 
            Asigna una tarea a un estudiante.
        asignar_examen: 
            Asigna un examen a un estudiante.
        asignar_proyecto: 
            Asigna un proyecto a un estudiante.
        __init__: 
            Inicializa la clase con una instancia de Creador.
    """
    def __init__(self, creador):
        self.creador = creador
        
    def asignar_tarea(self, nombre, desc):
        """
        Función para asignar una tarea a un estudiante.
        
        Parámetros:
        ----------
            nombre (str): Nombre de la tarea.    
            desc (str): Descripcion de la tarea.
        
        Retorna:
        -------
            self: Retorna la instancia de la clase Creador con el nombre y descripcion agregados.
        """
        return self.creador.agregar_nombre(nombre).agregar_desc(desc)
        
    def asignar_examen(self, nombre, desc, fecha):
        """
        Función para asignar un examen a un estudiante.
        
        Parámetros:
        ----------
            nombre (str): Nombre del examen.
            desc (str): Descripcion del examen.
            fecha (str): Fecha de entrega del examen.
        
        Retorna:
        -------
            self: Retorna la instancia de la clase Creador con el nombre, descripcion y fecha de entrega agregados.
        """
        return self.creador.agregar_nombre(nombre).agregar_desc(desc).asignar_fecha_entrega(fecha)

    def asignar_proyecto(self, nombre, desc, fecha):
        """
        Función para asignar un proyecto a un estudiante.
        
        Parámetros:
        ----------
            nombre (str): Nombre del proyecto.
            desc (str): Descripcion del proyecto.
            fecha (str): Fecha de entrega del proyecto.
        Retorna:
        -------
            self: Retorna la instancia de la clase Creador con el nombre, descripcion y fecha de entrega agregados.
        """
        return self.creador.agregar_nombre(nombre).agregar_desc(desc).asignar_fecha_entrega(fecha)

