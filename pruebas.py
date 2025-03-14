import pytest
from main import ConexionServer, Publicador, SuscriptorAlumno, SuscriptorProfesor
from builder_tareas import Asignacion, Creador, Asignador
from strategy_mostrarasig import Estrategia, EstrategiaVerExamen, EstrategiaVerProyecto, EstrategiaVerTarea, Manager


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
        if(self.publicador.suscriptores == []): #Si no existen los suscriptores se añaden
            self.suscribir(self.alumno1)
            self.suscribir(self.alumno2)
            self.suscribir(self.profesor1)
            self.suscribir(self.profesor2)
        self.desuscribir(self.alumno1)      #Se eliminan todos los suscriptores
        self.desuscribir(self.alumno2)
        self.desuscribir(self.profesor1)
        self.desuscribir(self.profesor2)
        assert self.publicador.suscriptores == [], "No se eliminaron todos los suscriptores"       #assert si se eliminaron

    def test_notificar_suscriptores(self, mocker):
        """Prueba que se puedan notificar los eventos a todos los suscriptores"""
        mock_alumno1 = mocker.patch.object(self.alumno1, 'notificar')
        mock_alumno2 = mocker.patch.object(self.alumno2, 'notificar')
        mock_profesor1 = mocker.patch.object(self.profesor1, 'notificar')
        mock_profesor2 = mocker.patch.object(self.profesor2, 'notificar')  
        #Se crean objetos mock para poder hacer pruebas y comprobar que sean llamados

        eventos = ["Evento 1", "Evento 2"]
        self.publicador.notificarSuscriptores(eventos)
        #Se llama al metodo notificarSuscriptores con los eventos

        mock_alumno1.assert_called_once_with(eventos)
        mock_alumno2.assert_called_once_with(eventos)
        mock_profesor1.assert_called_once_with(eventos)
        mock_profesor2.assert_called_once_with(eventos)
        #se hacen asserts para comprobar que los metodos notificar de los suscriptores fueron llamados

class TestCreacionTareas:
    def setup_method(self):
        self.creador = Creador()
        self.asignador = Asignador(self.creador)
        #Se instancian las clases creador y asignador, necesarias para el builder

    def test_asignar_tarea(self):
        nombre = "Tarea 1"
        descripcion = "Descripción de la tarea 1"
        asignacion = self.asignador.asignar_tarea(nombre, descripcion).asignacion
        #se crea una asignacion y se asignan nombre y descripcion

        assert asignacion.nombre == nombre, "El nombre de la asignación no es correcto"
        assert asignacion.descripcion == descripcion, "La descripción de la asignación no es correcta"
        assert asignacion.fecha_entrega == "", "La fecha de entrega debería estar vacía"
        assert asignacion.archivos == [], "La lista de archivos debería estar vacía"
        assert asignacion.questions == [], "La lista de preguntas debería estar vacía"
        #se hacen pruebas para checar que los atributos de la tearea sean correctos

    def test_asignar_examen(self):
        nombre = "Examen 1"
        descripcion = "Descripción del examen 1"
        fecha_entrega = "2025-03-20"
        asignacion = self.asignador.asignar_examen(nombre, descripcion, fecha_entrega).asignacion
        #se crea una asignacion y se asignan nombre, descripcion y fecha de entrega

        assert asignacion.nombre == nombre, "El nombre de la asignación no es correcto"
        assert asignacion.descripcion == descripcion, "La descripción de la asignación no es correcta"
        assert asignacion.fecha_entrega == fecha_entrega, "La fecha de entrega no es correcta"
        assert asignacion.archivos == [], "La lista de archivos debería estar vacía"
        assert asignacion.questions == [], "La lista de preguntas debería estar vacía"
        #se comprueba que los valores de las propiedades de la asignacion sean los asignados

    def test_asignar_proyecto(self):
        nombre = "Proyecto 1"
        descripcion = "Descripción del proyecto 1"
        fecha_entrega = "2025-04-01"
        asignacion = self.asignador.asignar_proyecto(nombre, descripcion, fecha_entrega).asignacion
        #se crea una asignacion y se asignan nombre, descripcion y fecha de entrega

        assert asignacion.nombre == nombre, "El nombre de la asignación no es correcto"
        assert asignacion.descripcion == descripcion, "La descripción de la asignación no es correcta"
        assert asignacion.fecha_entrega == fecha_entrega, "La fecha de entrega no es correcta"
        assert asignacion.archivos == [], "La lista de archivos debería estar vacía"
        assert asignacion.questions == [], "La lista de preguntas debería estar vacía"
        #se comprueba que los valores de las propiedades de la asignacion sean los asignados

    def test_agregar_archivo(self):
        nombre = "Tarea con archivo"
        descripcion = "Descripción de la tarea con archivo"
        archivo = "archivo1.txt"
        asignacion = self.asignador.asignar_tarea(nombre, descripcion).agregar_archivo(archivo).asignacion
        #se crea una asignacion y se asignan nombre y descripcion, se agrega un archivo

        assert asignacion.archivos == [archivo], "El archivo no se agregó correctamente"
        #se comprueba que la asignacion contenga el archivo que se agrego

    def test_agregar_pregunta(self):
        nombre = "Tarea con pregunta"
        descripcion = "Descripción de la tarea con pregunta"
        pregunta = "¿Cuál es la capital de Francia?"
        asignacion = self.asignador.asignar_tarea(nombre, descripcion).agregar_pregunta(pregunta).asignacion
        #se crea una asignacion y se asignan nombre y descripcion, se agrega una pregunta

        assert asignacion.questions == [pregunta], "La pregunta no se agregó correctamente"
        #se comprueba que la asignacion contenga la pregunta que se agrego

class TestMostrarAsignaciones:
    def setup_method(self):
        """
        Se crean 3 asignaciones para probar, una que representa una tarea, otra que 
        representa un examen y otra que representa un proyecto, cada una con atributos
        distintos. Estas asignaciones se usaran para las pruebas
        """
        self.asignacion_tarea = Asignacion()
        self.asignacion_tarea.nombre = "Tarea 1"
        self.asignacion_tarea.descripcion = "Descripción de la tarea 1"
        self.asignacion_tarea.archivos = ["archivo1.txt", "archivo2.txt"]

        self.asignacion_examen = Asignacion()
        self.asignacion_examen.nombre = "Examen 1"
        self.asignacion_examen.descripcion = "Descripción del examen 1"
        self.asignacion_examen.fecha_entrega = "2025-03-20"
        self.asignacion_examen.preguntas = ["Pregunta 1", "Pregunta 2"]

        self.asignacion_proyecto = Asignacion()
        self.asignacion_proyecto.nombre = "Proyecto 1"
        self.asignacion_proyecto.descripcion = "Descripción del proyecto 1"
        self.asignacion_proyecto.fecha_entrega = "2025-04-01"
        self.asignacion_proyecto.archivos = ["archivo1.txt", "archivo2.txt"]

    def test_estrategia_ver_tarea(self):
        #Se prueba la estrategia de mostrar tarea, y tambien mostrar sus archivos.
        estrategia = EstrategiaVerTarea(self.asignacion_tarea)
        manager = Manager(estrategia)
        assert manager.mostrar() == "El nombre de la tarea es: Tarea 1 y su descripcion es: Descripción de la tarea 1"
        assert estrategia.ver_archivos() == "Los archivos de la tarea son: ['archivo1.txt', 'archivo2.txt']"

    def test_estrategia_ver_examen(self):
        #Se prueba la estrategia de mostrar examen y sus preguntas
        estrategia = EstrategiaVerExamen(self.asignacion_examen)
        manager = Manager(estrategia)
        assert manager.mostrar() == "El examen es: Examen 1, descripcion: Descripción del examen 1, fecha: 2025-03-20"
        assert estrategia.mostrar_preguntas() == "Las preguntas son: ['Pregunta 1', 'Pregunta 2']"

    def test_estrategia_ver_proyecto(self):
        #Se prueba la estrategia de mostrar proyecto y sus archivos
        estrategia = EstrategiaVerProyecto(self.asignacion_proyecto)
        manager = Manager(estrategia)
        assert manager.mostrar() == "El proyecto es: Proyecto 1, descripcion: Descripción del proyecto 1, fecha: 2025-04-01"
        assert estrategia.mostrar_archivos() == "Los archivos son: ['archivo1.txt', 'archivo2.txt']"
