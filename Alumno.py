class Alumno():
    #Atributos

    #(registro,nombre,apellido,dni,direccion,telefono,email,fechaNac,curso)
    __datosPersonales = (0,"","",0,"","","",(0,0,0),0)

    #(fechaAlta,fechaBaja)
    __fechas = ((0,0,0),(0,0,0))

    #(usuario,contraseña)
    __userpass = ("","")

    __concepto = ""
    __inasistencias = 0

    #lista de materias
    __materias = []

    def __init__(self):

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
