class ConexionServer:
    _instancia = None  #Instancia unica de la conexion al servidor 

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(ConexionServer, cls).__new__(cls) #Si no existe crea una conexion
            print("Conexion a servidor exitosa!")
        return cls._instancia
    