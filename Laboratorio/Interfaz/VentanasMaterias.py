from tkinter import *
from tkinter import ttk,font


class AltaMateria:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Alta de Materia")
        self.raiz.geometry("430x320")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.registro = IntVar()
        self.codigo = IntVar()
        self.nota1 = IntVar()
        self.nota2 = IntVar()
        self.nota3 = IntVar()
        self.aviso = StringVar()

        self.labeltitulo = ttk.Label(self.raiz, text="Ingrese los datos de la Materia", font=titulo, padding=(5, 5))
        self.labelreg = ttk.Label(self.raiz, text="Registro del alumno", padding=(5,5), font=negrita)
        self.labelcod = ttk.Label(self.raiz, text="Código de materia", padding=(5,5), font=negrita)
        self.labelnotas = ttk.Label(self.raiz, text="Ingrese las notas (0 significa 'sin nota')", padding=(5,5), font=negrita)
        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, font=negrita, padding=(5, 5))

        self.fieldreg = ttk.Entry(self.raiz, textvariable=self.registro, width=25)
        self.fieldcod = ttk.Entry(self.raiz, textvariable=self.codigo, width=25)
        self.fieldnota1 = ttk.Entry(self.raiz, textvariable=self.nota1, width=10)
        self.fieldnota2 = ttk.Entry(self.raiz, textvariable=self.nota2, width=10)
        self.fieldnota3 = ttk.Entry(self.raiz, textvariable=self.nota3, width=10)

        self.bCargar = ttk.Button(self.raiz, text="Cargar", padding=(5, 5), command=lambda: self.cargar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.labeltitulo.place(x=90, y=5)
        self.labelreg.place(x=40, y=60)
        self.fieldreg.place(x=220, y=62)

        self.labelcod.place(x=40, y=100)
        self.fieldcod.place(x=220, y=100)

        self.labelnotas.place(x=40, y=140)
        self.fieldnota1.place(x=50, y=180)
        self.fieldnota2.place(x=130, y=180)
        self.fieldnota3.place(x=210, y=180)

        self.labelaviso.place(x=40, y=220)
        self.bCargar.place(x=300, y=250)
        self.bCancelar.place(x=200, y=250)

        self.raiz.grab_set()
        self.raiz.mainloop()


    def cargar(self):
        encontrado = False
        errormateria = False
        errornotas = False
        tablas = self.bd.getTablas()
        self.aviso.set("")
        if self.codigo.get() < 1 or self.codigo.get() > 9:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Materia inexistente")
            errormateria = True

        if (self.nota1.get() <0 or self.nota1.get()>10) or (self.nota2.get()<0 or self.nota2.get()>10) or (self.nota3.get()<0 or self.nota3.get()>10):
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Notas inválidas")
            errornotas = True

        for alumno in tablas[0]:
            if alumno.getRegistro() == self.registro.get():
                encontrado = True

        if encontrado and not errormateria and not errornotas:
            for materia in tablas[1]:
                if materia.getCodigoMateria() == self.codigo.get() and materia.getCodigoAlumno() == self.registro.get():
                    notas = (self.nota1.get(),self.nota2.get(),self.nota3.get())
                    materia.setNotas(notas)
                    self.bd.setTablas(tablas)
                    self.labelaviso.configure(foreground="blue")
                    self.aviso.set("Notas cargadas")
        elif not encontrado:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Alumno inexistente")

# ----------------------------------------------------------------------------------------------------------------------

class ModMateria:

    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Alta de Materia")
        self.raiz.geometry("430x360")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.registro = IntVar()
        self.codigo = IntVar()
        self.nota1 = IntVar()
        self.nota2 = IntVar()
        self.nota3 = IntVar()
        self.aviso = StringVar()
        self.sebusco = False

        self.labeltitulo = ttk.Label(self.raiz, text="Ingrese los datos de la Materia", font=titulo, padding=(5, 5))
        self.labelreg = ttk.Label(self.raiz, text="Registro del alumno", padding=(5,5), font=negrita)
        self.labelcod = ttk.Label(self.raiz, text="Código de materia", padding=(5,5), font=negrita)
        self.labelnotas = ttk.Label(self.raiz, text="Ingrese las notas (0 significa 'sin nota')", padding=(5,5), font=negrita)
        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, font=negrita, padding=(5, 5))

        self.fieldreg = ttk.Entry(self.raiz, textvariable=self.registro, width=25)
        self.fieldcod = ttk.Entry(self.raiz, textvariable=self.codigo, width=25)
        self.fieldnota1 = ttk.Entry(self.raiz, textvariable=self.nota1, width=10)
        self.fieldnota2 = ttk.Entry(self.raiz, textvariable=self.nota2, width=10)
        self.fieldnota3 = ttk.Entry(self.raiz, textvariable=self.nota3, width=10)

        self.bBuscar = ttk.Button(self.raiz, text="Buscar", padding=(5, 5), command=lambda: self.buscar())
        self.bModificar = ttk.Button(self.raiz, text="Modificar", padding=(5, 5), command=lambda: self.modificar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.labeltitulo.place(x=90, y=5)
        self.labelreg.place(x=40, y=60)
        self.fieldreg.place(x=220, y=62)

        self.labelcod.place(x=40, y=100)
        self.fieldcod.place(x=220, y=100)
        self.bBuscar.place(x=300, y=140)
        self.labelnotas.place(x=40, y=180)
        self.fieldnota1.place(x=50, y=220)
        self.fieldnota2.place(x=130, y=220)
        self.fieldnota3.place(x=210, y=220)

        self.labelaviso.place(x=40, y=260)
        self.bModificar.place(x=300, y=290)
        self.bCancelar.place(x=200, y=290)

        self.raiz.grab_set()
        self.raiz.mainloop()


    def buscar(self):
        encontrado = False
        errormateria = False
        tablas = self.bd.getTablas()
        self.aviso.set("")

        if self.codigo.get() < 1 or self.codigo.get() > 9:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Materia inexistente")
            errormateria = True

        for alumno in tablas[0]:
            if alumno.getRegistro() == self.registro.get():
                encontrado = True

        if encontrado and not errormateria:
            self.sebusco = True
            for materia in tablas[1]:
                if materia.getCodigoMateria() == self.codigo.get() and materia.getCodigoAlumno() == self.registro.get():
                    notas = materia.getNotas()
                    if notas == (0,0,0):
                        self.labelaviso.configure(foreground="red")
                        self.aviso.set("Debe primero cargar la materia")
                    else:
                        self.nota1.set(notas[0])
                        self.nota2.set(notas[1])
                        self.nota3.set(notas[2])

        elif not encontrado:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Alumno inexistente")

    def modificar(self):
        self.aviso.set("")
        if self.sebusco:
            tablas = self.bd.getTablas()
            for materia in tablas[1]:
                if materia.getCodigoMateria() == self.codigo.get() and materia.getCodigoAlumno() == self.registro.get():
                    notas = (self.nota1.get(), self.nota2.get(), self.nota3.get())
                    materia.setNotas(notas)
                    self.bd.setTablas(tablas)
                    self.labelaviso.configure(foreground="blue")
                    self.aviso.set("Notas actualizadas")
        else:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Debe buscar una materia")

# ----------------------------------------------------------------------------------------------------------------------

class ElimMateria:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Alta de Materia")
        self.raiz.geometry("430x220")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.registro = IntVar()
        self.codigo = IntVar()
        self.aviso = StringVar()
        self.sebusco = False

        self.labeltitulo = ttk.Label(self.raiz, text="Ingrese los datos de la Materia", font=titulo, padding=(5, 5))
        self.labelreg = ttk.Label(self.raiz, text="Registro del alumno", padding=(5,5), font=negrita)
        self.labelcod = ttk.Label(self.raiz, text="Código de materia", padding=(5,5), font=negrita)
        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, font=negrita, padding=(5, 5))

        self.fieldreg = ttk.Entry(self.raiz, textvariable=self.registro, width=25)
        self.fieldcod = ttk.Entry(self.raiz, textvariable=self.codigo, width=25)

        self.bEliminar = ttk.Button(self.raiz, text="Modificar", padding=(5, 5), command=lambda: self.eliminar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.labeltitulo.place(x=90, y=5)
        self.labelreg.place(x=40, y=60)
        self.fieldreg.place(x=220, y=62)

        self.labelcod.place(x=40, y=100)
        self.fieldcod.place(x=220, y=100)

        self.labelaviso.place(x=40, y=130)
        self.bEliminar.place(x=290, y=160)
        self.bCancelar.place(x=190, y=160)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def eliminar(self):
        encontrado = False
        errormateria = False
        tablas = self.bd.getTablas()
        self.aviso.set("")

        if self.codigo.get() < 1 or self.codigo.get() > 9:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Materia inexistente")
            errormateria = True

        for alumno in tablas[0]:
            if alumno.getRegistro() == self.registro.get():
                encontrado = True

        if encontrado and not errormateria:
            for materia in tablas[1]:
                if materia.getCodigoMateria() == self.codigo.get() and materia.getCodigoAlumno() == self.registro.get():
                    notas = (0,0,0)
                    if materia.getNotas() == (0,0,0):
                        self.labelaviso.configure(foreground="red")
                        self.aviso.set("La materia no está cargada")
                    else:
                        materia.setNotas(notas)
                        self.bd.setTablas(tablas)
                        self.labelaviso.configure(foreground="blue")
                        self.aviso.set("Materia eliminada")
        elif not encontrado:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Alumno inexistente")

# ----------------------------------------------------------------------------------------------------------------------

class ConsultaMateria:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Alta de Materia")
        self.raiz.geometry("430x360")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.registro = IntVar()
        self.codigo = IntVar()
        self.nota1 = IntVar()
        self.nota2 = IntVar()
        self.nota3 = IntVar()
        self.aviso = StringVar()

        self.labeltitulo = ttk.Label(self.raiz, text="Ingrese los datos de la Materia", font=titulo, padding=(5, 5))
        self.labelreg = ttk.Label(self.raiz, text="Registro del alumno", padding=(5,5), font=negrita)
        self.labelcod = ttk.Label(self.raiz, text="Código de materia", padding=(5,5), font=negrita)
        self.labelnotas = ttk.Label(self.raiz, text="Ingrese las notas (0 significa 'sin nota')", padding=(5,5), font=negrita)
        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, font=negrita, padding=(5, 5))

        self.fieldreg = ttk.Entry(self.raiz, textvariable=self.registro, width=25)
        self.fieldcod = ttk.Entry(self.raiz, textvariable=self.codigo, width=25)
        self.fieldnota1 = ttk.Entry(self.raiz, textvariable=self.nota1, width=10)
        self.fieldnota2 = ttk.Entry(self.raiz, textvariable=self.nota2, width=10)
        self.fieldnota3 = ttk.Entry(self.raiz, textvariable=self.nota3, width=10)

        self.bBuscar = ttk.Button(self.raiz, text="Buscar", padding=(5, 5), command=lambda: self.buscar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.labeltitulo.place(x=90, y=5)
        self.labelreg.place(x=40, y=60)
        self.fieldreg.place(x=220, y=62)

        self.labelcod.place(x=40, y=100)
        self.fieldcod.place(x=220, y=100)
        self.bBuscar.place(x=300, y=140)
        self.labelnotas.place(x=40, y=180)
        self.fieldnota1.place(x=50, y=220)
        self.fieldnota2.place(x=130, y=220)
        self.fieldnota3.place(x=210, y=220)

        self.labelaviso.place(x=40, y=260)
        self.bCancelar.place(x=300, y=290)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def buscar(self):
        encontrado = False
        errormateria = False
        tablas = self.bd.getTablas()
        self.aviso.set("")

        if self.codigo.get() < 1 or self.codigo.get() > 9:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Materia inexistente")
            errormateria = True

        for alumno in tablas[0]:
            if alumno.getRegistro() == self.registro.get():
                encontrado = True

        if encontrado and not errormateria:
            for materia in tablas[1]:
                if materia.getCodigoMateria() == self.codigo.get() and materia.getCodigoAlumno() == self.registro.get():
                    notas = materia.getNotas()
                    if notas == (0,0,0):
                        self.labelaviso.configure(foreground="red")
                        self.aviso.set("Debe primero cargar la materia")
                    else:
                        self.nota1.set(notas[0])
                        self.nota2.set(notas[1])
                        self.nota3.set(notas[2])

        elif not encontrado:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Alumno inexistente")