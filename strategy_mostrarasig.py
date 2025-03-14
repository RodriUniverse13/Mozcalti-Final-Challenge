from abc import ABC, abstractmethod

class Estrategia(ABC):
    def __init__(self, asignacion):
        self.asignacion = asignacion

    @abstractmethod
    def mostrar(self):
        pass

class EstrategiaVerTarea(Estrategia):
    def __init__(self, asignacion):
        super().__init__(asignacion)

    def mostrar(self):
        return f"El nombre de la tarea es: {self.asignacion.nombre} y su descripcion es: {self.asignacion.descripcion}"
    
    def ver_archivos(self):
        return f"Los archivos de la tarea son: {self.asignacion.archivos}"

class EstrategiaVerExamen(Estrategia):
    def __init__(self, asignacion):
        super().__init__(asignacion)
        self.asignacion.questions = self.asignacion.questions or []

    def mostrar(self):
        return f"El examen es: {self.asignacion.nombre}, descripcion: {self.asignacion.descripcion}, fecha: {self.asignacion.fecha_entrega}"
    
    def mostrar_preguntas(self):
        return f"Las preguntas son: {self.asignacion.questions}"

class EstrategiaVerProyecto(Estrategia):
    def __init__(self, asignacion):
        super().__init__(asignacion)

    def mostrar(self):
        return f"El proyecto es: {self.asignacion.nombre}, descripcion: {self.asignacion.descripcion}, fecha: {self.asignacion.fecha_entrega}"
        
    def mostrar_archivos(self):
        return f"Los archivos son: {self.asignacion.archivos}"

class Manager:
    def __init__(self, estrategia):
        self.estrategia = estrategia
        
    def set_estrategia(self, estrategia):
        self.estrategia = estrategia
        
    def mostrar(self):
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