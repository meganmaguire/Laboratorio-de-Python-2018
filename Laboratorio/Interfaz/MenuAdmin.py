from tkinter import *
from tkinter import ttk, font
from Interfaz.Menu import *
from Interfaz.VentanasAdministracion import *
from Interfaz.VentanasAlumno import *
from Interfaz.VentanasMaterias import *


class MenuAdmin:

    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Menu de Operaciones Generales")
        self.raiz.resizable(0, 0)
        self.raiz.geometry("800x300")
        self.bd=bd
        negrita = font.Font(weight='bold', size=10)

        self.label1 = ttk.Label(self.raiz, text="Administración", padding=(5, 5),font=negrita)
        self.bsesion = ttk.Button(self.raiz, text="Iniciar sesión de trabajo", padding=(5, 5), width=30, command=lambda: self.iniciarsesion())
        self.bbackup = ttk.Button(self.raiz, text="Almacenar en disco (Backup)", padding=(5, 5), width=30, command=lambda: self.backup())
        self.bregistro = ttk.Button(self.raiz, text="Registrar Usuario", padding=(5, 5), width=30, command=lambda: self.registro())
        self.beliminar = ttk.Button(self.raiz, text="Eliminar Usuario", padding=(5, 5), width=30, command=lambda: self.eliminar())

        self.label2 = ttk.Label(self.raiz, text="Alumnos", padding=(5, 5), font=negrita)
        self.baalumno = ttk.Button(self.raiz, text="Alta de Alumno", padding=(5, 5), width=30, command=lambda: self.altaAlumno())
        self.bbalumno = ttk.Button(self.raiz, text="Baja de Alumno", padding=(5, 5), width=30, command=lambda: self.elimAlumno())
        self.bmalumno = ttk.Button(self.raiz, text="Modificación de Alumno", padding=(5, 5), width=30, command=lambda: self.modAlumno())
        self.bcalumno = ttk.Button(self.raiz, text="Consulta de Alumno", padding=(5, 5), width=30, command=lambda: self.consultaAlumno())

        self.label3 = ttk.Label(self.raiz, text="Materias", padding=(5, 5), font=negrita)
        self.bamateria = ttk.Button(self.raiz, text="Alta de Materia", padding=(5, 5), width=30, command=lambda: self.altaMateria())
        self.bbmateria = ttk.Button(self.raiz, text="Baja de Materia", padding=(5, 5), width=30, command=lambda: self.elimMateria())
        self.bmmateria = ttk.Button(self.raiz, text="Modificación de Materia", padding=(5, 5), width=30, command=lambda: self.modMateria())
        self.bcmateria = ttk.Button(self.raiz, text="Consulta de Materia", padding=(5, 5), width=30, command=lambda: self.consultaMateria())

        self.bsalir = ttk.Button(self.raiz, text="Salir", padding=(5, 5),command=quit)
        self.bvolver = ttk.Button(self.raiz, text="Volver", padding=(5, 5), command=lambda: self.volver())

        self.label1.place(x=90, y=20)
        self.bsesion.place(x=40, y=60)
        self.bbackup.place(x=40, y=100)
        self.bregistro.place(x=40, y=140)
        self.beliminar.place(x=40, y=180)

        self.label2.place(x=365, y=20)
        self.baalumno.place(x=300, y=60)
        self.bbalumno.place(x=300, y=100)
        self.bmalumno.place(x=300, y=140)
        self.bcalumno.place(x=300, y=180)

        self.label3.place(x=620, y=20)
        self.bamateria.place(x=560, y=60)
        self.bbmateria.place(x=560, y=100)
        self.bmmateria.place(x=560, y=140)
        self.bcmateria.place(x=560, y=180)

        self.bsalir.place(x=560, y=240)
        self.bvolver.place(x=675, y=240)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def volver(self):
        self.raiz.destroy()

    def iniciarsesion(self):
        Inicializar(self.raiz,self.bd)

    def backup(self):
        Backup(self.raiz,self.bd)

    def registro(self):
        RegistrarUsuario(self.raiz,self.bd)

    def eliminar(self):
        EliminarUsuario(self.raiz,self.bd)

    def altaAlumno(self):
        AltaAlumno(self.raiz,self.bd)

    def elimAlumno(self):
        ElimAlumno(self.raiz,self.bd)

    def modAlumno(self):
        ModAlumno(self.raiz,self.bd)

    def consultaAlumno(self):
        ConsultaAlumno(self.raiz,self.bd)

    def altaMateria(self):
        AltaMateria(self.raiz,self.bd)

    def elimMateria(self):
        ElimMateria(self.raiz,self.bd)

    def modMateria(self):
        ModMateria(self.raiz,self.bd)

    def consultaMateria(self):
        ConsultaMateria(self.raiz,self.bd)