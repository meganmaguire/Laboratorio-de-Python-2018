from tkinter import *
from tkinter import ttk, font
from Interfaz.MenuAdmin import *
from Interfaz.MenuGral import *


class Menu(Toplevel):

    def __init__(self,bd):
        self.raiz = Tk()
        self.raiz.title("Menu")
        self.raiz.resizable(0, 0)
        self.raiz.geometry("320x150")
        self.bd=bd
        self.botonadmin = ttk.Button(self.raiz, text="Administrar Alumnos y Materias", padding=(5, 5), command=lambda: self.admin(), width = 30)
        self.botongral = ttk.Button(self.raiz, text="Operaciones Generales", padding=(5, 5), command=lambda: self.gral(), width = 30)
        self.botonsalir = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=quit)

        self.botonadmin.place(x=60, y=20)
        self.botongral.place(x=60, y=60)
        self.botonsalir.place(x=115, y=100)

        self.raiz.mainloop()


    def admin(self):
        menu=MenuAdmin(self.raiz,self.bd)

    def gral(self):
        menu=MenuGral(self.raiz,self.bd)