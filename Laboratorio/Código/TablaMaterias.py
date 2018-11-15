from Código.Materia import Materia


class TablaMaterias:
    
    def __init__(self,lista=[]):
        self.__lista = lista
    def __iter__(self):
        return iter(self.__lista)

    def getLista(self):
        return self.__lista
    def setLista(self,lista):
        self.__lista = lista

    def inicializarMaterias(self,registro):
        listaMaterias = []
        materia = Materia(1,registro, "Matemática", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(2, registro, "Lengua", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(3, registro, "Física", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(4, registro, "Química", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(5, registro, "Biología", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(6, registro, "Ética", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(7, registro, "Historia", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(8, registro, "Geografía", (0, 0, 0))
        listaMaterias.append(materia)
        materia = Materia(9, registro, "Computación", (0, 0, 0))
        listaMaterias.append(materia)
        lista = self.getLista()
        self.setLista(lista+listaMaterias)

        return listaMaterias
