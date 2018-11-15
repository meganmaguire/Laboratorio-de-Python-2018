class Alumno:
    
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


    def getDatosPersonales(self):
        return self.__datosPersonales

    def setDatosPersonales(self,datos):
        self.__datosPersonales = datos

    def getFechas(self):
        return self.__fechas

    def setFechas(self,fechas):
        self.__fechas = fechas

    def getUserPass(self):
        return self.__userpass

    def setUserPass(self,userpass):
        self.__userpass = userpass

    def getConcepto(self):
        return self.__concepto

    def setConcepto(self,concepto):
        self.__concepto=concepto

    def getInasistencias(self):
        return self.__inasistencias

    def setInasistencias(self,inasistencias):
        self.__inasistencias = inasistencias

    def getMaterias(self):
        return self.__materias
        
    def setMaterias(self,materias):
        self.__materias = materias