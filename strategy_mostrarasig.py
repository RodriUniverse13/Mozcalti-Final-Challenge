from abc import ABC, abstractmethod

class Estrategia(ABC):
    """
    Clase abstracta que define la interfaz para las estrategias de visualización de asignaciones.
    
    Atributos:
    ---------
        asignacion (object): 
            Objeto que representa la asignación a mostrar.
    
    Métodos:
    -------
        mostrar(): 
            Método abstracto que debe ser implementado por las subclases para mostrar la información de la asignación.
    """
    
    def __init__(self, asignacion):
        self.asignacion = asignacion

    @abstractmethod
    def mostrar(self):
        pass

class EstrategiaVerTarea(Estrategia):
    """
    Clase que implementa la estrategia para mostrar una tarea.
    Hereda de la clase abstracta Estrategia y define cómo mostrar la información de una tarea.
    
    Atributos:
    ---------
        asignacion (object): 
            Objeto que representa la tarea a mostrar.
    
    Métodos:
    -------
        mostrar(): 
            Método que muestra el nombre y la descripción de la tarea.
        ver_archivos(): 
            Método que muestra los archivos asociados a la tarea.
    """
    def __init__(self, asignacion):
        super().__init__(asignacion)

    def mostrar(self):
        """
        Método que muestra el nombre y la descripción de la tarea.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene el nombre y la descripción de la tarea.
        """
        return f"El nombre de la tarea es: {self.asignacion.nombre} y su descripcion es: {self.asignacion.descripcion}"
    
    def ver_archivos(self):
        """
        Método que muestra los archivos asociados a la tarea.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene los archivos asociados a la tarea.
        """
        return f"Los archivos de la tarea son: {self.asignacion.archivos}"

class EstrategiaVerExamen(Estrategia):
    """
    Clase que implementa la estrategia para mostrar un examen.
    Hereda de la clase abstracta Estrategia y define cómo mostrar la información de un examen.
    
    Atributos:
    ---------
        asignacion (object): 
            Objeto que representa el examen a mostrar.
    
    Métodos:
    -------
        mostrar(): 
            Método que muestra el nombre, la descripción y la fecha de entrega del examen.
        mostrar_preguntas(): 
            Método que muestra las preguntas asociadas al examen.
    """
    def __init__(self, asignacion):
        super().__init__(asignacion)
        self.asignacion.questions = self.asignacion.questions or []

    def mostrar(self):
        """
        Método que muestra el nombre, la descripción y la fecha de entrega del examen.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene el nombre, la descripción y la fecha de entrega del examen.
        """
        return f"El examen es: {self.asignacion.nombre}, descripcion: {self.asignacion.descripcion}, fecha: {self.asignacion.fecha_entrega}"
    
    def mostrar_preguntas(self):
        """
        Método que muestra las preguntas asociadas al examen.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene las preguntas del examen.
        """
        return f"Las preguntas son: {self.asignacion.questions}"

class EstrategiaVerProyecto(Estrategia):
    """
    Clase que implementa la estrategia para mostrar un proyecto.
    Hereda de la clase abstracta Estrategia y define cómo mostrar la información de un proyecto
    
    Atributos:
    ---------
        asignacion (object): 
            Objeto que representa el proyecto a mostrar.
    
    Métodos:
    -------
        mostrar(): 
            Método que muestra el nombre, la descripción y la fecha de entrega del proyecto.
        mostrar_archivos(): 
            Método que muestra los archivos asociados al proyecto.
    """
    
    def __init__(self, asignacion):
        super().__init__(asignacion)

    def mostrar(self):
        """
        Método que muestra el nombre, la descripción y la fecha de entrega del proyecto.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene el nombre, la descripción y la fecha de entrega del proyecto.
        """
        return f"El proyecto es: {self.asignacion.nombre}, descripcion: {self.asignacion.descripcion}, fecha: {self.asignacion.fecha_entrega}"
        
    def mostrar_archivos(self):
        """
        Método que muestra los archivos asociados al proyecto.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene los archivos asociados al proyecto.
        """
        return f"Los archivos son: {self.asignacion.archivos}"

class Manager:
    """
    La clase Manager gestiona una estrategia y permite cambiarla y mostrarla.
    
    Atributos:
    -----------
    estrategia : object
        La estrategia que se va a gestionar.
    
    Métodos:
    --------
        __init__(estrategia):
            Inicializa la clase Manager con una estrategia.
        set_estrategia(estrategia):
            Establece una nueva estrategia.
        mostrar():
            Muestra la estrategia actual.
    """
    def __init__(self, estrategia):
        self.estrategia = estrategia
        
    def set_estrategia(self, estrategia):
        """
        Establece una nueva estrategia.
        
        Parámetros:
        ----------
            estrategia (Estrategia): 
                La nueva estrategia a establecer.
        """
        self.estrategia = estrategia
        
    def mostrar(self):
        """
        Muestra la estrategia actual.
        
        Retorna:
        -------
            str: 
            Cadena de texto que contiene la información de la estrategia actual.
        """
        return self.estrategia.mostrar()
    
# if __name__ == "__main__":
#     from builder_tareas import Creador

#     creador = Creador()
#     tarea = creador.agregar_nombre("Tarea 1").agregar_desc("Descripción de la tarea").agregar_archivo("archivo1.txt").asignacion
#     examen = creador.agregar_nombre("Examen 1").agregar_desc("Descripción del examen").asignar_fecha_entrega("2023-12-01").asignacion
#     proyecto = creador.agregar_nombre("Proyecto 1").agregar_desc("Descripción del proyecto").agregar_archivo("archivo2.txt").asignar_fecha_entrega("2023-12-15").asignacion

#     context = Manager(EstrategiaVerTarea(tarea))
#     print(context.mostrar())
    
#     context.set_estrategia(EstrategiaVerExamen(examen))
#     print(context.mostrar())
    
#     context.set_estrategia(EstrategiaVerProyecto(proyecto))
#     print(context.mostrar())