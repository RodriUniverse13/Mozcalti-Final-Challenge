class Asignacion:
    def __init__(self):
        self.archivos_permitidos = []
        self.descripcion = ""
        self.nombre = ""
        self.questions = []
    
    def agregar_archivo_permitido(self, archivo):
        self.archivos_permitidos.append(archivo)
    

class Creador:
    def __init__(self):
        self.asignacion = Asignacion()
        
    def per_pdf(self):
        self.asignacion.agregar_archivo_permitido("PDF")
        return self
        
    def per_pptx(self):
        self.asignacion.agregar_archivo_permitido("PPTX")
        return self
        
    def per_xls(self):
        self.asignacion.agregar_archivo_permitido("XLS")
        return self
    
    def per_docx(self):
        self.asignacion.agregar_archivo_permitido("DOCX")
        return self
    
    def per_jpg(self):
        self.asignacion.agregar_archivo_permitido("JPG")
        return self
    
    def per_zip(self):
        self.asignacion.agregar_archivo_permitido("ZIP")
        return self
    
    def add_desc(self, desc):
        self.asignacion.descripcion = desc
        return self
    
    def add_name(self, name):
        self.asignacion.nombre = name
        return self
    
    def per_form(self):
        self.asignacion.agregar_archivo_permitido("FORM")
        return self
        
    def add_question(self, question):
        self.asignacion.questions.append(question)
        return self
    
class Asignador:
    def __init__(self, creador):
        self.creador = creador
        
    def asignar_tarea(self,name,desc):
        return self.creador.per_pdf().per_jpg().per_docx().per_xls().per_pptx().add_desc(desc).add_name(name)

    def asignar_examen(self,name,desc):
        return self.creador.per_pdf().per_jpg().per_docx().per_form().add_desc(desc).add_name(name)
    
    def asignar_proyecto(self,name,desc):
        return self.creador.per_pdf().per_jpg().per_zip().add_desc(desc).add_name(name)


if __name__ == "__main__":
    creadortareas = Creador()
    asignador = Asignador(creadortareas)
    tarea = asignador.asignar_tarea()