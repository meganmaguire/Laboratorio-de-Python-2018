from tkinter import *
from tkinter import ttk
from Interfaz.Menu import *
from Interfaz.Table import *

class MenuGral:

    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Menu de Operaciones Generales")
        self.raiz.resizable(0, 0)
        self.raiz.geometry("320x300")
        self.bd=bd

        self.btalumnos = ttk.Button(self.raiz, text="Listado de alumnos", padding=(5, 5), width=30)
        self.btmaterias = ttk.Button(self.raiz, text="Listado de materias", padding=(5, 5), width=30, command=lambda: self.listado_materias())
        self.blegajo = ttk.Button(self.raiz, text="Legajo de alumno", padding=(5, 5), width=30)
        self.breadmision = ttk.Button(self.raiz, text="Alumnos para readmisión", padding=(5, 5), width=30)
        self.bcurso = ttk.Button(self.raiz, text="Listado de alumnos por curso", padding=(5, 5), width=30)
        self.bsalir = ttk.Button(self.raiz, text="Salir", padding=(5, 5),command=quit)
        self.bvolver = ttk.Button(self.raiz, text="Volver", padding=(5, 5), command=lambda: self.volver())

        self.btalumnos.place(x=60, y=20)
        self.btmaterias.place(x=60, y=60)
        self.blegajo.place(x=60, y=100)
        self.breadmision.place(x=60, y=140)
        self.bcurso.place(x=60, y=180)
        self.bsalir.place(x=60, y=240)
        self.bvolver.place(x=170, y=240)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def volver(self):
        self.raiz.destroy()

    def listado_materias(self):
        tablas = self.bd.getTablas()
        raiz = Tk()
        table = Table(raiz, ["Nro Registro", "Código de Materia", "Nombre","Nota 1C","Nota 2C", "Nota 3C"], column_minwidths=[None, None, None, None, None, None])
        table.pack(expand=True, fill=X, padx=10, pady=10)

        for materia in tablas[1]:
            notas = materia.getNotas()
            table.set_data([[str(materia.getCodigoAlumno()),str(materia.getCodigoMateria()),str(materia.getNombre()),str(notas[0]),str(notas[1]),str(notas[2])]])

        raiz.mainloop()