from Código.TablaAlumnos import TablaAlumnos
from Código.TablaMaterias import TablaMaterias


class BD:

    def __init__(self, cantUsuarios=1, acceso={"P-Admin":"Ad1"}, nbreTablas={"T_Alumnos":0, "T_Materias":1}, tablas=[TablaAlumnos(),TablaMaterias()]):
        self.__cantUsuarios = cantUsuarios
        self.__acceso = acceso
        self.__nbreTablas = nbreTablas
        self.__tablas = tablas

    def getCantUsuarios(self):
        return self.__cantUsuarios

    def setCantUsuarios(self,cantUsuarios):
        self.__cantUsuarios = cantUsuarios

    def getAcceso(self):
        return self.__acceso

    def setAcceso(self,acceso):
        self.__acceso = acceso

    def getNbreTablas(self):
        return self.__nbreTablas

    def setNbreTablas(self,nbreTablas):
        self.__nbreTablas = nbreTablas

    def getTablas(self):
        return self.__tablas

    def setTablas(self,tablas):
        self.__tablas = tablas
