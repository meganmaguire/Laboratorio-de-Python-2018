from tkinter import Toplevel
from Complementos.TableScroll import *


class ListadoMaterias:
    def __init__(self,padre,bd):
        self.root = Toplevel(padre)
        self.bd = bd
        tablas = self.bd.getTablas()

        self.table = Table(self.root, ["Nro de Registro","Código de Materia","Nombre","Nota 1C", "Nota 2C", "Nota 3C"], column_minwidths=[None, None, None, None, None, None],height=700)
        self.table.pack(expand=True, fill=X,padx=10, pady=10)

        for materia in tablas[1]:
            notas = materia.getNotas()
            registro = materia.getCodigoAlumno()
            codigo = materia.getCodigoMateria()
            nombre = materia.getNombre()
            self.table.insert_row([registro,codigo,nombre,notas[0],notas[1],notas[2]])


        self.root.update()
        self.root.geometry("%sx%s" % (self.root.winfo_reqwidth(), 250))

        self.root.mainloop()