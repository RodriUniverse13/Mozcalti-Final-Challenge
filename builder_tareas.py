class Asignacion:
    def __init__(self):
        self.archivos = []
        self.descripcion = ""
        self.nombre = ""
        self.questions = []
        self.fecha_entrega = ""
    
    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)

class Creador:
    def __init__(self):
        self.asignacion = Asignacion()
    
    def agregar_desc(self, desc):
        self.asignacion.descripcion = desc
        return self
    
    def agregar_nombre(self, nombre):
        self.asignacion.nombre = nombre
        return self
    
    def agregar_pregunta(self, pregunta):
        self.asignacion.questions.append(pregunta)
        return self
    
    def asignar_fecha_entrega(self, fecha):
        self.asignacion.fecha_entrega = fecha
        return self
    
    def agregar_archivo(self, archivo):
        self.asignacion.archivos.append(archivo)
        return self

class Asignador:
    def __init__(self, creador):
        self.creador = creador
        
    def asignar_tarea(self, nombre, desc):
        return self.creador.agregar_nombre(nombre).agregar_desc(desc)
        
    def asignar_examen(self, nombre, desc, fecha):
        return self.creador.agregar_nombre(nombre).agregar_desc(desc).asignar_fecha_entrega(fecha)

    def asignar_proyecto(self, nombre, desc, fecha):
        return self.creador.agregar_nombre(nombre).agregar_desc(desc).asignar_fecha_entrega(fecha)

