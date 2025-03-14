import pytest
from main import ConexionServer, Publicador, SuscriptorAlumno, SuscriptorProfesor


class TestConexionUnicaAlServidor:
    def test_conexion_unica_al_servidor(self):
        """Prueba el patron de diseño Singleton, verifica que solo exista
        una instancia de conexion al servidor, si no muestra un mensaje de error"""
        db1 = ConexionServer()
        db2 = ConexionServer()
        assert db1 is db2, "Existe mas de una instancia de conexion a el servidor"

class TestPublicador:
    def __init__(self):
        publicador = Publicador()
        alumno1 = SuscriptorAlumno()
        alumno2 = SuscriptorAlumno()
        profesor1 = SuscriptorProfesor()
        profesor2 = SuscriptorProfesor()
        #Se crearon todos los suscriptores y se instancia un publicador

    def test_suscribir(self):
        """Prueba que se agreguen los suscriptores a la lista de suscriptores"""
        self.suscribir(self.alumno1)
        self.suscribir(self.alumno2)
        self.suscribir(self.profesor1)
        self.suscribir(self.profesor2)
        #Se suscriben los suscriptores al publicador
        assert self.publicador.suscriptores == [self.alumno1, self.alumno2, self.profesor1, self.profesor2], "No se agregaron todos los suscriptores"

    def test_desuscribir(self):
        if(self.publicador.suscriptores == []):
            self.suscribir(self.alumno1)
            self.suscribir(self.alumno2)
            self.suscribir(self.profesor1)
            self.suscribir(self.profesor2)
        self.desuscribir(self.alumno1)
        self.desuscribir(self.alumno2)
        self.desuscribir(self.profesor1)
        self.desuscribir(self.profesor2)
        assert self.publicador.suscriptores == [], "No se eliminaron todos los suscriptores"

    def test_notificar_suscriptores(self, mocker):
        """Prueba que se puedan notificar los eventos a todos los suscriptores"""
        mock_alumno1 = mocker.patch.object(self.alumno1, 'notificar')
        mock_alumno2 = mocker.patch.object(self.alumno2, 'notificar')
        mock_profesor1 = mocker.patch.object(self.profesor1, 'notificar')
        mock_profesor2 = mocker.patch.object(self.profesor2, 'notificar')

        eventos = ["Evento 1", "Evento 2"]
        self.publicador.notificarSuscriptores(eventos)

        mock_alumno1.assert_called_once_with(eventos)
        mock_alumno2.assert_called_once_with(eventos)
        mock_profesor1.assert_called_once_with(eventos)
        mock_profesor2.assert_called_once_with(eventos)

class TestCreacionAsignaciones:
    def test_creacion_asignaciones

