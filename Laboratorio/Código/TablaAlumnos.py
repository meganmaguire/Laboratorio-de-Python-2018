class TablaAlumnos:

    def __init__(self,lista=[]):
        self.__lista = lista

    def __iter__(self):
        return iter(self.__lista)

    def getLista(self):
        return self.__lista
    def setLista(self,lista):
        self.__lista = lista

    def setAlumno(self,alumno):
        lista = self.getLista()
        self.setLista(lista + [alumno])