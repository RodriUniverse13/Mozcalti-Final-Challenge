from abc import ABC, abstractmethod

from builder_tareas import Creador, Asignador
from strategy_mostrarasig import Manager, EstrategiaVerTarea, EstrategiaVerExamen, EstrategiaVerProyecto

class ConexionServer:
    """Clase que representa una conexión a un servidor, implementando el patrón Singleton.
    Esta clase asegura que solo haya una instancia de la conexión al servidor en todo momento.
    
    Atributos:
    ---------
        _instancia (ConexionServer): 
            Instancia única de la conexión al servidor.
    """
    
    _instancia = None  #Instancia unica de la conexion al servidor 

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(ConexionServer, cls).__new__(cls) #Si no existe crea una conexion
            print("Conexion a servidor exitosa!")
        return cls._instancia
    
class Suscriptor(ABC):
    """
    Clase abstracta base para los suscriptores en el patrón observer
    """
    @abstractmethod
    def notificar(self):
        pass

class SuscriptorAlumno(Suscriptor):
    """
    Clase que representa un suscriptor de tipo Alumno.
    Hereda de la clase abstracta Suscriptor.
    """
    def notificar(self, eventos):
        print(f'Notificación para Alumno: {eventos}')


class SuscriptorProfesor(Suscriptor):
    """
    Clase que representa un suscriptor de tipo Profesor.
    Hereda de la clase abstracta Suscriptor.
    """
    def notificar(self, eventos):
        print(f'Notificación para Profesor: {eventos}')

class Publicador:
    """
    Clase que representa un publicador de eventos, que puede tener múltiples suscriptores.
    Esta clase permite agregar y eliminar suscriptores, así como publicar eventos a los suscriptores.
    
    Atributos:
    ---------
        suscriptores (list): Lista de suscriptores que recibirán los eventos.
    """
    
    def __init__(self):
        self.suscriptores = []
    
    def suscribir(self, suscriptor) -> None:
        """
        Agrega un suscriptor a la lista de suscriptores.
        Args:
            suscriptor (Suscriptor): El suscriptor a agregar.
        """
        self.suscriptores.append(suscriptor)
        print(f'Suscriptor {suscriptor} agregado.')

    def desuscribir(self, suscriptor) -> None:
        """
        Elimina un suscriptor de la lista de suscriptores.
        Args:
            suscriptor (Suscriptor): El suscriptor a eliminar.
        """
        self.suscriptores.remove(suscriptor)
        print(f'Suscriptor {suscriptor} eliminado.')
    
    def notificarSuscriptores(self, eventos : list = []):
        """
        Publica los eventos a todos los suscriptores.
        Recorre la lista de suscriptores y llama al método notificar de cada uno, pasando los eventos.
        Args:
            eventos (list): Lista de eventos a publicar.
        """
        for suscriptor in self.suscriptores:
            suscriptor.notificar(eventos)

#Funciones solo para uso del main
def crear_asignacion():
    creador = Creador()
    asignador = Asignador(creador)
    
    print("Seleccione el tipo de asignación a crear:")
    print("1. Tarea")
    print("2. Examen")
    print("3. Proyecto")
    opcion = input("Ingrese el número de la opción: ")

    nombre = input("Ingrese el nombre de la asignación: ")
    descripcion = input("Ingrese la descripción de la asignación: ")

    if opcion == "1":
        tarea = asignador.asignar_tarea(nombre, descripcion).asignacion
        return tarea, EstrategiaVerTarea(tarea)
    elif opcion == "2":
        fecha_entrega = input("Ingrese la fecha de entrega del examen (YYYY-MM-DD): ")
        examen = asignador.asignar_examen(nombre, descripcion, fecha_entrega).asignacion
        return examen, EstrategiaVerExamen(examen)
    elif opcion == "3":
        fecha_entrega = input("Ingrese la fecha de entrega del proyecto (YYYY-MM-DD): ")
        proyecto = asignador.asignar_proyecto(nombre, descripcion, fecha_entrega).asignacion
        return proyecto, EstrategiaVerProyecto(proyecto)
    else:
        print("Opción no válida.")
        return None, None

def main():
    publicador = Publicador()
    suscriptor_alumno = SuscriptorAlumno()
    suscriptor_profesor = SuscriptorProfesor()
    publicador.suscribir(suscriptor_alumno)
    publicador.suscribir(suscriptor_profesor)

    while True:
        print("\nMenú:")
        print("1. Crear asignación")
        print("2. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            asignacion, estrategia = crear_asignacion()
            if asignacion and estrategia:
                publicador.notificarSuscriptores([f"Nueva asignación creada: {asignacion.nombre}"])
                manager = Manager(estrategia)
                print(manager.mostrar())
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()