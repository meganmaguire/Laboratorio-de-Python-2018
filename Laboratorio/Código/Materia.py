class Materia:

    def __init__(self,codigoMateria=0,codigoAlumno=0,nombre="",notas=(0,0,0)):
        self.__codigoMateria = codigoMateria
        self.__codigoAlumno = codigoAlumno
        self.__nombre = nombre
        self.__notas = notas
    def __iter__(self):
        return iter(self.__lista)

    def getCodigoMateria(self):
        return self.__codigoMateria
    def setCodigoMateria(self,codigoMateria):
        self.__codigoMateria = codigoMateria
    def getCodigoAlumno(self):
        return self.__codigoAlumno
    def setCodigoAlumno(self,codigoAlumno):
        self.__codigoAlumno = codigoAlumno
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNotas(self):
        return self.__notas
    def setNotas(self,notas):
        self.__notas = notas 