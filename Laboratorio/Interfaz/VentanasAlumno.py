from tkinter import *
from tkinter import ttk,font
import time

from Código.Alumno import Alumno
from Código.Materia import Materia


class AltaAlumno:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.resizable(0,0)
        self.raiz.title("Alta de Alumno")
        self.raiz.geometry("690x580")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.aviso = StringVar()
        self.labeltitulo = ttk.Label(self.raiz, text="Ingrese los datos del Alumno", font=titulo, padding=(5, 5))
        self.labeldpersonales = ttk.Label(self.raiz, text="Datos Personales", font=titulo, padding=(5, 5))
        self.labeldacademicos = ttk.Label(self.raiz, text="Datos académicos", font=titulo,)
        self.labelaviso = ttk.Label(self.raiz, textvariable = self.aviso, font=titulo, padding=(5, 5))
        self.label1 = ttk.Label(self.raiz, text="Nombre:", font=negrita, padding=(5, 5))
        self.label2 = ttk.Label(self.raiz, text="Apellido:", font=negrita, padding=(5, 5))
        self.label3 = ttk.Label(self.raiz, text="DNI:", font=negrita, padding=(5, 5))
        self.label4 = ttk.Label(self.raiz, text="Dirección:", font=negrita, padding=(5, 5))
        self.label5 = ttk.Label(self.raiz, text="Teléfono:", font=negrita, padding=(5, 5))
        self.label6 = ttk.Label(self.raiz, text="Email:", font=negrita, padding=(5, 5))
        self.label7 = ttk.Label(self.raiz, text="F. Nacim.:", font=negrita, padding=(5, 5))
        self.label8 = ttk.Label(self.raiz, text="Curso:", font=negrita, padding=(5, 5))
        self.label9 = ttk.Label(self.raiz, text="Registro:", font=negrita, padding=(5, 5))
        self.label10 = ttk.Label(self.raiz, text="F. Ingreso:", font=negrita, padding=(5, 5))
        self.label11 = ttk.Label(self.raiz, text="Usuario:", font=negrita, padding=(5, 5))
        self.label12 = ttk.Label(self.raiz, text="Contraseña:", font=negrita, padding=(5, 5))
        self.label13 = ttk.Label(self.raiz, text="Inasistencias:", font=negrita, padding=(5, 5))
        self.label14 = ttk.Label(self.raiz, text="Concepto:", font=negrita, padding=(5, 5))

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.direccion = StringVar()
        self.telefono = StringVar()
        self.email = StringVar()
        self.fnac = StringVar()
        self.curso = IntVar()
        self.registro = IntVar()
        self.fingreso = StringVar()
        self.user = StringVar()
        self.pword = StringVar()
        self.inasistencias = IntVar()
        self.concepto = StringVar()

        self.fnombre = ttk.Entry(self.raiz, textvariable=self.nombre, width=30)
        self.fapellido = ttk.Entry(self.raiz, textvariable=self.apellido, width=30)
        self.fdni = ttk.Entry(self.raiz, textvariable=self.dni, width=30)
        self.fdireccion = ttk.Entry(self.raiz, textvariable=self.direccion, width=30)
        self.ftelefono = ttk.Entry(self.raiz, textvariable=self.telefono, width=30)
        self.femail = ttk.Entry(self.raiz, textvariable=self.email, width=30)
        self.ffnac = ttk.Entry(self.raiz, textvariable=self.fnac, width=30)
        self.fcurso = ttk.Entry(self.raiz, textvariable=self.curso, width=30)
        self.fregistro = ttk.Entry(self.raiz, textvariable=self.registro, width=30)
        self.ffingreso = ttk.Entry(self.raiz, textvariable=self.fingreso, width=30)
        self.fuser = ttk.Entry(self.raiz, textvariable=self.user, width=30)
        self.fpword = ttk.Entry(self.raiz, textvariable=self.pword, width=30, show="*")
        self.finasistencias = ttk.Entry(self.raiz, textvariable=self.inasistencias, width=30)
        self.fconcepto = ttk.Entry(self.raiz, textvariable=self.concepto, width=30)

        self.bRegistrar = ttk.Button(self.raiz, text="Registrar", padding=(5, 5), command=lambda: self.registrar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.labeltitulo.place(x=250, y=5)
        self.labeldpersonales.place(x=40, y=60)

        self.label1.place(x=40, y=100)
        self.fnombre.place(x=140, y=102)
        self.label2.place(x=360, y=100)
        self.fapellido.place(x=460, y=102)

        self.label9.place(x=40, y=140)
        self.fregistro.place(x=140, y=142)
        self.label3.place(x=360, y=140)
        self.fdni.place(x=460, y=142)

        self.label4.place(x=40, y=180)
        self.fdireccion.place(x=140, y=182)
        self.label5.place(x=360, y=180)
        self.ftelefono.place(x=460, y=182)

        self.label6.place(x=40, y=220)
        self.femail.place(x=140, y=222)
        self.label7.place(x=40, y=260)
        self.ffnac.place(x=140, y=262)
        self.label8.place(x=360, y=260)
        self.fcurso.place(x=460, y=262)

        self.labeldacademicos.place(x=40, y=320)
        self.label10.place(x=40, y=360)
        self.ffingreso.place(x=140, y=362)
        self.label11.place(x=40, y=400)
        self.fuser.place(x=140, y=402)
        self.label12.place(x=360, y=400)
        self.fpword.place(x=460, y=402)

        self.label13.place(x=40, y=440)
        self.finasistencias.place(x=140, y=442)
        self.label14.place(x=360, y=440)
        self.fconcepto.place(x=460, y=442)

        self.labelaviso.place(x=40, y= 480)
        self.bRegistrar.place(x=560, y=500)
        self.bCancelar.place(x=450, y=500)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def registrar(self):
        registro = self.registro.get()
        tablas = self.bd.getTablas()
        acceso = self.bd.getAcceso()
        repetido = False
        self.aviso.set("")
        for alumno in tablas[0]:
            if alumno.getRegistro() == registro:
                repetido = True
        if repetido:
            self.labelaviso.configure(foreground = "red")
            self.aviso.set("Registro existente")
        else:
            #Transforma en tupla
            string = self.fnac.get()
            lista = string.split("/")
            fnac = (lista[0],lista[1],lista[2])
            string = self.fingreso.get()
            lista = string.split("/")
            fingreso = (lista[0],lista[1],lista[2])
            fbaja = (0,0,0)
            fechas = (fingreso, fbaja)
            #carga los datos en el alumno
            alumno = Alumno(self.registro.get(),self.nombre.get(),self.apellido.get(),self.dni.get(),self.direccion.get(),self.telefono.get(),self.email.get(),fnac,self.curso.get(),fechas,(self.user.get(),self.pword.get()),self.concepto.get(),self.inasistencias.get(),[])
            #crea el usuario
            acceso["A-"+self.user.get()] = self.pword.get()
            #trae las tablas, las carga y se las setea a la bd
            tablas = self.bd.getTablas()
            listaMaterias = tablas[1].inicializarMaterias(self.registro.get())
            alumno.setMaterias(listaMaterias)
            tablas[0].setAlumno(alumno)
            self.bd.setTablas(tablas)
            self.bd.setAcceso(acceso)
            self.labelaviso.configure(foreground="blue")
            self.aviso.set("Registro exitoso")

# ----------------------------------------------------------------------------------------------------------------------

class ModAlumno:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.resizable(0,0)
        self.raiz.title("Modificación de Alumno")
        self.raiz.geometry("690x620")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.aviso = StringVar()
        self.labeltitulo = ttk.Label(self.raiz, text="Modificación de los datos del Alumno", font=titulo, padding=(5, 5))
        self.labeldpersonales = ttk.Label(self.raiz, text="Datos Personales", font=titulo, padding=(5, 5))
        self.labeldacademicos = ttk.Label(self.raiz, text="Datos académicos", font=titulo,)
        self.labelaviso = ttk.Label(self.raiz, textvariable = self.aviso, font=titulo, padding=(5, 5))
        self.labelbusqueda = ttk.Label(self.raiz,text="Ingrese el numero de registro", font=titulo, padding=(5, 5))
        self.label1 = ttk.Label(self.raiz, text="Nombre:", font=negrita, padding=(5, 5))
        self.label2 = ttk.Label(self.raiz, text="Apellido:", font=negrita, padding=(5, 5))
        self.label3 = ttk.Label(self.raiz, text="DNI:", font=negrita, padding=(5, 5))
        self.label4 = ttk.Label(self.raiz, text="Dirección:", font=negrita, padding=(5, 5))
        self.label5 = ttk.Label(self.raiz, text="Teléfono:", font=negrita, padding=(5, 5))
        self.label6 = ttk.Label(self.raiz, text="Email:", font=negrita, padding=(5, 5))
        self.label7 = ttk.Label(self.raiz, text="F. Nacim.:", font=negrita, padding=(5, 5))
        self.label8 = ttk.Label(self.raiz, text="Curso:", font=negrita, padding=(5, 5))
        self.label9 = ttk.Label(self.raiz, text="Registro:", font=negrita, padding=(5, 5))
        self.label10 = ttk.Label(self.raiz, text="F. Ingreso:", font=negrita, padding=(5, 5))
        self.label15 = ttk.Label(self.raiz, text="F. Egreso:", font=negrita, padding=(5, 5))
        self.label11 = ttk.Label(self.raiz, text="Usuario:", font=negrita, padding=(5, 5))
        self.label12 = ttk.Label(self.raiz, text="Contraseña:", font=negrita, padding=(5, 5))
        self.label13 = ttk.Label(self.raiz, text="Inasistencias:", font=negrita, padding=(5, 5))
        self.label14 = ttk.Label(self.raiz, text="Concepto:", font=negrita, padding=(5, 5))

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.direccion = StringVar()
        self.telefono = StringVar()
        self.email = StringVar()
        self.fnac = StringVar()
        self.curso = IntVar()
        self.registro = IntVar()
        self.fingreso = StringVar()
        self.fegreso = StringVar()
        self.user = StringVar()
        self.pword = StringVar()
        self.inasistencias = IntVar()
        self.concepto = StringVar()
        self.regBuscar = IntVar()
        self.sebusco = False

        self.fnombre = ttk.Entry(self.raiz, textvariable=self.nombre, width=30)
        self.fapellido = ttk.Entry(self.raiz, textvariable=self.apellido, width=30)
        self.fdni = ttk.Entry(self.raiz, textvariable=self.dni, width=30)
        self.fdireccion = ttk.Entry(self.raiz, textvariable=self.direccion, width=30)
        self.ftelefono = ttk.Entry(self.raiz, textvariable=self.telefono, width=30)
        self.femail = ttk.Entry(self.raiz, textvariable=self.email, width=30)
        self.ffnac = ttk.Entry(self.raiz, textvariable=self.fnac, width=30)
        self.fcurso = ttk.Entry(self.raiz, textvariable=self.curso, width=30)
        self.fregistro = ttk.Entry(self.raiz, textvariable=self.registro, width=30)
        self.ffingreso = ttk.Entry(self.raiz, textvariable=self.fingreso, width=30)
        self.ffegreso = ttk.Entry(self.raiz, textvariable=self.fegreso, width=30)
        self.fuser = ttk.Entry(self.raiz, textvariable=self.user, width=30)
        self.fpword = ttk.Entry(self.raiz, textvariable=self.pword, width=30, show="*")
        self.finasistencias = ttk.Entry(self.raiz, textvariable=self.inasistencias, width=30)
        self.fconcepto = ttk.Entry(self.raiz, textvariable=self.concepto, width=30)
        self.fbusqueda = ttk.Entry(self.raiz, textvariable=self.regBuscar, width=15)

        self.bModificar = ttk.Button(self.raiz, text="Modificar", padding=(5, 5), command=lambda: self.modificar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())
        self.bBuscar = ttk.Button(self.raiz, text="Buscar", padding=(5, 5), command=lambda: self.buscar())

        self.labeltitulo.place(x=250, y=5)
        self.labelbusqueda.place(x=40, y=55)
        self.fbusqueda.place(x=280, y=62)
        self.bBuscar.place(x=400, y=58)

        self.labeldpersonales.place(x=40, y=100)

        self.label1.place(x=40, y=140)
        self.fnombre.place(x=140, y=142)
        self.label2.place(x=360, y=140)
        self.fapellido.place(x=460, y=142)

        self.label9.place(x=40, y=180)
        self.fregistro.place(x=140, y=182)
        self.label3.place(x=360, y=180)
        self.fdni.place(x=460, y=182)

        self.label4.place(x=40, y=220)
        self.fdireccion.place(x=140, y=222)
        self.label5.place(x=360, y=220)
        self.ftelefono.place(x=460, y=222)

        self.label6.place(x=40, y=260)
        self.femail.place(x=140, y=262)
        self.label7.place(x=40, y=300)
        self.ffnac.place(x=140, y=302)
        self.label8.place(x=360, y=300)
        self.fcurso.place(x=460, y=302)

        self.labeldacademicos.place(x=40, y=360)
        self.label10.place(x=40, y=400)
        self.ffingreso.place(x=140, y=402)
        self.label15.place(x=360, y=400)
        self.ffegreso.place(x=460, y=402)
        self.label11.place(x=40, y=440)
        self.fuser.place(x=140, y=442)
        self.label12.place(x=360, y=440)
        self.fpword.place(x=460, y=442)

        self.label13.place(x=40, y=480)
        self.finasistencias.place(x=140, y=482)
        self.label14.place(x=360, y=480)
        self.fconcepto.place(x=460, y=482)

        self.labelaviso.place(x=40, y= 520)
        self.bModificar.place(x=560, y=540)
        self.bCancelar.place(x=450, y=540)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def buscar(self):
        registro = self.regBuscar.get()
        lista = []
        encontrado = False
        self.aviso.set("")
        if registro == "":
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Ingrese un registro")
        else:
            tablas = self.bd.getTablas()
            for alumno in tablas[0]:
                if alumno.getRegistro() == registro:
                    self.sebusco = True
                    encontrado = True
                    self.registro.set(alumno.getRegistro())
                    self.nombre.set(alumno.getNombre())
                    self.apellido.set(alumno.getApellido())
                    self.dni.set(alumno.getDni())
                    self.direccion.set(alumno.getDireccion())
                    self.telefono.set(alumno.getTelefono())
                    self.email.set(alumno.getEmail())
                    lista = '/'.join(str(v) for v in list(alumno.getFNac()))
                    self.fnac.set(lista)
                    self.curso.set(alumno.getCurso())
                    fechas = alumno.getFechas()
                    lista = '/'.join(str(v) for v in list(fechas[0]))
                    self.fingreso.set(lista)
                    lista = '/'.join(str(v) for v in list(fechas[1]))
                    self.fegreso.set(lista)
                    self.user.set(alumno.getUserPass()[0])
                    self.pword.set(alumno.getUserPass()[1])
                    self.inasistencias.set(alumno.getInasistencias())
                    self.concepto.set(alumno.getConcepto())
                    break
            if not encontrado:
                self.labelaviso.configure(foreground="red")
                self.aviso.set("Registro inexistente")

    def modificar(self):
        self.aviso.set("")
        if self.sebusco:
            tablas = self.bd.getTablas()
            for alumno in tablas[0]:
                if alumno.getRegistro() == self.registro.get():
                    # Transforma en tupla
                    string = self.fnac.get()
                    lista = string.split("/")
                    fnac = (lista[0], lista[1], lista[2])
                    string = self.fingreso.get()
                    lista = string.split("/")
                    fingreso = (lista[0], lista[1], lista[2])
                    string = self.fegreso.get()
                    lista = string.split("/")
                    fbaja = (lista[0], lista[1], lista[2])
                    fechas = (fingreso, fbaja)
                    # modifica el alumno
                    alumno.setRegistro(self.registro.get())
                    alumno.setNombre(self.nombre.get())
                    alumno.setApellido(self.apellido.get())
                    alumno.setDni(self.dni.get())
                    alumno.setDireccion(self.direccion.get())
                    alumno.setTelefono(self.telefono.get())
                    alumno.setEmail(self.email.get())
                    alumno.setFNac(fnac)
                    alumno.setCurso(self.curso.get())
                    alumno.setFechas(fechas)
                    alumno.setUserPass((self.user.get(),self.pword.get()))
                    alumno.setInasistencias(self.inasistencias.get())
                    alumno.setConcepto(self.concepto.get())
                    self.labelaviso.configure(foreground="blue")
                    self.aviso.set("Modificación exitosa")

        else:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Debe buscar un alumno")

# ----------------------------------------------------------------------------------------------------------------------

class ConsultaAlumno:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.resizable(0,0)
        self.raiz.title("Consulta de Alumno")
        self.raiz.geometry("690x580")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.aviso = StringVar()
        self.labeltitulo = ttk.Label(self.raiz, text="Consulta de los datos del Alumno", font=titulo, padding=(5, 5))
        self.labeldpersonales = ttk.Label(self.raiz, text="Datos Personales", font=titulo, padding=(5, 5))
        self.labeldacademicos = ttk.Label(self.raiz, text="Datos académicos", font=titulo,)
        self.labelaviso = ttk.Label(self.raiz, textvariable = self.aviso, font=titulo, padding=(5, 5))
        self.labelbusqueda = ttk.Label(self.raiz,text="Ingrese el numero de registro", font=titulo, padding=(5, 5))
        self.label1 = ttk.Label(self.raiz, text="Nombre:", font=negrita, padding=(5, 5))
        self.label2 = ttk.Label(self.raiz, text="Apellido:", font=negrita, padding=(5, 5))
        self.label3 = ttk.Label(self.raiz, text="DNI:", font=negrita, padding=(5, 5))
        self.label4 = ttk.Label(self.raiz, text="Dirección:", font=negrita, padding=(5, 5))
        self.label5 = ttk.Label(self.raiz, text="Teléfono:", font=negrita, padding=(5, 5))
        self.label6 = ttk.Label(self.raiz, text="Email:", font=negrita, padding=(5, 5))
        self.label7 = ttk.Label(self.raiz, text="F. Nacim.:", font=negrita, padding=(5, 5))
        self.label8 = ttk.Label(self.raiz, text="Curso:", font=negrita, padding=(5, 5))
        self.label9 = ttk.Label(self.raiz, text="Registro:", font=negrita, padding=(5, 5))
        self.label10 = ttk.Label(self.raiz, text="F. Ingreso:", font=negrita, padding=(5, 5))
        self.label15 = ttk.Label(self.raiz, text="F. Egreso:", font=negrita, padding=(5, 5))
        self.label11 = ttk.Label(self.raiz, text="Usuario:", font=negrita, padding=(5, 5))
        self.label12 = ttk.Label(self.raiz, text="Contraseña:", font=negrita, padding=(5, 5))
        self.label13 = ttk.Label(self.raiz, text="Inasistencias:", font=negrita, padding=(5, 5))
        self.label14 = ttk.Label(self.raiz, text="Concepto:", font=negrita, padding=(5, 5))

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.direccion = StringVar()
        self.telefono = StringVar()
        self.email = StringVar()
        self.fnac = StringVar()
        self.curso = IntVar()
        self.registro = IntVar()
        self.fingreso = StringVar()
        self.fegreso = StringVar()
        self.user = StringVar()
        self.pword = StringVar()
        self.inasistencias = IntVar()
        self.concepto = StringVar()
        self.regBuscar = IntVar()
        self.sebusco = False

        self.fnombre = ttk.Entry(self.raiz, textvariable=self.nombre, width=30)
        self.fapellido = ttk.Entry(self.raiz, textvariable=self.apellido, width=30)
        self.fdni = ttk.Entry(self.raiz, textvariable=self.dni, width=30)
        self.fdireccion = ttk.Entry(self.raiz, textvariable=self.direccion, width=30)
        self.ftelefono = ttk.Entry(self.raiz, textvariable=self.telefono, width=30)
        self.femail = ttk.Entry(self.raiz, textvariable=self.email, width=30)
        self.ffnac = ttk.Entry(self.raiz, textvariable=self.fnac, width=30)
        self.fcurso = ttk.Entry(self.raiz, textvariable=self.curso, width=30)
        self.fregistro = ttk.Entry(self.raiz, textvariable=self.registro, width=30)
        self.ffingreso = ttk.Entry(self.raiz, textvariable=self.fingreso, width=30)
        self.ffegreso = ttk.Entry(self.raiz, textvariable=self.fegreso, width=30)
        self.fuser = ttk.Entry(self.raiz, textvariable=self.user, width=30)
        self.fpword = ttk.Entry(self.raiz, textvariable=self.pword, width=30, show="*")
        self.finasistencias = ttk.Entry(self.raiz, textvariable=self.inasistencias, width=30)
        self.fconcepto = ttk.Entry(self.raiz, textvariable=self.concepto, width=30)
        self.fbusqueda = ttk.Entry(self.raiz, textvariable=self.regBuscar, width=15)

        self.bBuscar = ttk.Button(self.raiz, text="Buscar", padding=(5, 5), command=lambda: self.buscar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.labeltitulo.place(x=250, y=5)
        self.labelbusqueda.place(x=40, y=55)
        self.fbusqueda.place(x=280, y=62)
        self.bBuscar.place(x=400, y=58)

        self.labeldpersonales.place(x=40, y=100)

        self.label1.place(x=40, y=140)
        self.fnombre.place(x=140, y=142)
        self.label2.place(x=360, y=140)
        self.fapellido.place(x=460, y=142)

        self.label9.place(x=40, y=180)
        self.fregistro.place(x=140, y=182)
        self.label3.place(x=360, y=180)
        self.fdni.place(x=460, y=182)

        self.label4.place(x=40, y=220)
        self.fdireccion.place(x=140, y=222)
        self.label5.place(x=360, y=220)
        self.ftelefono.place(x=460, y=222)

        self.label6.place(x=40, y=260)
        self.femail.place(x=140, y=262)
        self.label7.place(x=40, y=300)
        self.ffnac.place(x=140, y=302)
        self.label8.place(x=360, y=300)
        self.fcurso.place(x=460, y=302)

        self.labeldacademicos.place(x=40, y=360)
        self.label10.place(x=40, y=400)
        self.ffingreso.place(x=140, y=402)
        self.label15.place(x=360, y=400)
        self.ffegreso.place(x=460, y=402)
        self.label11.place(x=40, y=440)
        self.fuser.place(x=140, y=442)
        self.label12.place(x=360, y=440)
        self.fpword.place(x=460, y=442)

        self.label13.place(x=40, y=480)
        self.finasistencias.place(x=140, y=482)
        self.label14.place(x=360, y=480)
        self.fconcepto.place(x=460, y=482)

        self.labelaviso.place(x=40, y= 520)
        self.bCancelar.place(x=560, y=520)
        self.raiz.grab_set()
        self.raiz.mainloop()

    def buscar(self):
        registro = self.regBuscar.get()
        lista = []
        encontrado = False
        self.aviso.set("")
        if registro == "":
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Ingrese un registro")
        else:
            tablas = self.bd.getTablas()
            for alumno in tablas[0]:
                if alumno.getRegistro() == registro:
                    self.sebusco = True
                    encontrado = True
                    self.registro.set(alumno.getRegistro())
                    self.nombre.set(alumno.getNombre())
                    self.apellido.set(alumno.getApellido())
                    self.dni.set(alumno.getDni())
                    self.direccion.set(alumno.getDireccion())
                    self.telefono.set(alumno.getTelefono())
                    self.email.set(alumno.getEmail())
                    lista = '/'.join(str(v) for v in list(alumno.getFNac()))
                    self.fnac.set(lista)
                    self.curso.set(alumno.getCurso())
                    fechas = alumno.getFechas()
                    lista = '/'.join(str(v) for v in list(fechas[0]))
                    self.fingreso.set(lista)
                    lista = '/'.join(str(v) for v in list(fechas[1]))
                    self.fegreso.set(lista)
                    self.user.set(alumno.getUserPass()[0])
                    self.pword.set(alumno.getUserPass()[1])
                    self.inasistencias.set(alumno.getInasistencias())
                    self.concepto.set(alumno.getConcepto())
                    break
            if not encontrado:
                self.labelaviso.configure(foreground="red")
                self.aviso.set("Registro inexistente")

# ----------------------------------------------------------------------------------------------------------------------

class ElimAlumno:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.bd=bd
        self.raiz.geometry("400x180")
        self.raiz.title("Baja de Alumno")
        self.raiz.resizable(0,0)
        negrita = font.Font(weight='bold', size=10)

        self.registro = IntVar()
        self.aviso = StringVar()

        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, padding=(5, 5))
        self.label1 = ttk.Label(self.raiz, text="Ingrese el numero de registro del alumno", padding=(5,5), font=negrita)
        self.registro = ttk.Entry(self.raiz, textvariable=self.registro, width=45)
        self.beliminar = ttk.Button(self.raiz, text="Eliminar", padding=(5,5), command=lambda: self.eliminar())
        self.bsalir = ttk.Button(self.raiz, text="Salir", padding=(5,5), command=lambda: self.raiz.destroy())

        self.label1.place(x=35, y=20)
        self.registro.place(x=40, y=60)
        self.labelaviso.place(x=40, y=90)
        self.beliminar.place(x=260, y=120)
        self.bsalir.place(x=160, y=120)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def eliminar(self):
        registro = int(self.registro.get())
        self.aviso.set("")
        encontrado = False
        if registro == 0:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Ingrese un registro")
        else:
            tablas = self.bd.getTablas()
            acceso = self.bd.getAcceso()
            for alumno in tablas[0]:
                if alumno.getRegistro() == registro and alumno.getFechas()[1] == (0,0,0):
                    encontrado = True
                    fechas = alumno.getFechas()
                    fechaActual = time.strftime("%d/%m/%y")
                    listaaux = fechaActual.split("/")
                    fbaja = (listaaux[0], listaaux[1], listaaux[2])
                    fechas = (fechas[0],fbaja)
                    alumno.setFechas(fechas)
                    user = "A-"+alumno.getUserPass()[0]
                    del acceso[user]
                    self.bd.setTablas(tablas)
                    self.labelaviso.configure(foreground="blue")
                    self.aviso.set("Eliminación exitosa")
                    break
            if  not encontrado:
                self.labelaviso.configure(foreground="red")
                self.aviso.set("Registro inexistente")
