import pytest
from main import ConexionServer, Publicador, SuscriptorAlumno, SuscriptorProfesor
from builder_tareas import Asignacion, Creador, Asignador


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

class TestCreacionTareas:
    def setup_method(self):
        self.creador = Creador()
        self.asignador = Asignador(self.creador)

    def test_asignar_tarea(self):
        nombre = "Tarea 1"
        descripcion = "Descripción de la tarea 1"
        asignacion = self.asignador.asignar_tarea(nombre, descripcion).asignacion

        assert asignacion.nombre == nombre, "El nombre de la asignación no es correcto"
        assert asignacion.descripcion == descripcion, "La descripción de la asignación no es correcta"
        assert asignacion.fecha_entrega == "", "La fecha de entrega debería estar vacía"
        assert asignacion.archivos == [], "La lista de archivos debería estar vacía"
        assert asignacion.questions == [], "La lista de preguntas debería estar vacía"

    def test_asignar_examen(self):
        nombre = "Examen 1"
        descripcion = "Descripción del examen 1"
        fecha_entrega = "2025-03-20"
        asignacion = self.asignador.asignar_examen(nombre, descripcion, fecha_entrega).asignacion

        assert asignacion.nombre == nombre, "El nombre de la asignación no es correcto"
        assert asignacion.descripcion == descripcion, "La descripción de la asignación no es correcta"
        assert asignacion.fecha_entrega == fecha_entrega, "La fecha de entrega no es correcta"
        assert asignacion.archivos == [], "La lista de archivos debería estar vacía"
        assert asignacion.questions == [], "La lista de preguntas debería estar vacía"

    def test_asignar_proyecto(self):
        nombre = "Proyecto 1"
        descripcion = "Descripción del proyecto 1"
        fecha_entrega = "2025-04-01"
        asignacion = self.asignador.asignar_proyecto(nombre, descripcion, fecha_entrega).asignacion

        assert asignacion.nombre == nombre, "El nombre de la asignación no es correcto"
        assert asignacion.descripcion == descripcion, "La descripción de la asignación no es correcta"
        assert asignacion.fecha_entrega == fecha_entrega, "La fecha de entrega no es correcta"
        assert asignacion.archivos == [], "La lista de archivos debería estar vacía"
        assert asignacion.questions == [], "La lista de preguntas debería estar vacía"

    def test_agregar_archivo(self):
        nombre = "Tarea con archivo"
        descripcion = "Descripción de la tarea con archivo"
        archivo = "archivo1.txt"
        asignacion = self.asignador.asignar_tarea(nombre, descripcion).agregar_archivo(archivo).asignacion

        assert asignacion.archivos == [archivo], "El archivo no se agregó correctamente"

    def test_agregar_pregunta(self):
        nombre = "Tarea con pregunta"
        descripcion = "Descripción de la tarea con pregunta"
        pregunta = "¿Cuál es la capital de Francia?"
        asignacion = self.asignador.asignar_tarea(nombre, descripcion).agregar_pregunta(pregunta).asignacion

        assert asignacion.questions == [pregunta], "La pregunta no se agregó correctamente"

