from abc import ABC, abstractmethod

class ConexionServer:
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