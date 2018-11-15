class Alumno():
    
    def __init__(self,registro = 0,nombre="",apellido="",dni=0,direccion="",telefono=0,email="",fNac=(0,0,0),curso=0,fechas = ((0,0,0),(0,0,0)),userpass = ("",""),concepto = "",inasistencias = 0,materias = []):
        #Atributos
        #datos personales
        self.__registro = registro
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__fNac = fNac
        self.__curso = curso
        #(fechaAlta,fechaBaja)
        self.__fechas = fechas
        #(usuario,contraseña)
        self.__userpass = userpass
        self.__concepto = concepto
        self.__inasistencias = inasistencias
        #lista de materias
        self.__materias = materias
    def __iter__(self):
        return iter(self.__lista)

    #datos personales
    def getRegistro(self):
        return self.__registro    
    def setRegistro(self,registro):
        self.__registro = registro    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getApellido(self):
        return self.__apellido
    def setApellido(self,apellido):
        self.__apellido = apellido
    def getDni(self):
        return self.__dni
    def setDni(self,dni):
        self.__dni = dni
    def getDireccion(self):
        return self.__direccion
    def setDireccion(self,direccion):
        self.__direccion = direccion
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,telefono):
        self.__telefono = telefono
    def getEmail(self):
        return self.__email
    def setEmail(self,email):
        self.__email = email
    def getFNac(self):
        return self.__fNac
    def setFNac(self,fNac):
        self.__fNac = fNac
    def getCurso(self):
        return self.__curso
    def setCurso(self,curso):
        self.__curso = curso 
    #fechas de alta y baja del colegio
    def getFechas(self):
        return self.__fechas
    def setFechas(self,fechas):
        self.__fechas = fechas
    #Usuario y contraseña
    def getUserPass(self):
        return self.__userpass
    def setUserPass(self,userpass):
        self.__userpass = userpass
    #Concepto (comportamiento)
    def getConcepto(self):
        return self.__concepto
    def setConcepto(self,concepto):
        self.__concepto=concepto
    #Inasistencias
    def getInasistencias(self):
        return self.__inasistencias
    def setInasistencias(self,inasistencias):
        self.__inasistencias = inasistencias
    #Materias
    def getMaterias(self):
        return self.__materias        
    def setMaterias(self,materias):
        self.__materias = materias