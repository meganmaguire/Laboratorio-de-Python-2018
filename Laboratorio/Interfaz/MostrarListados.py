import functools
from tkinter import *
from tkinter import ttk,font

from Complementos.TableScroll import *


class ListadoMaterias:

    def __init__(self,padre,bd):
        self.root = Toplevel(padre)
        self.root.title("Listado de Materias")
        self.root.resizable(0, 0)
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
        #self.root.geometry("%sx%s" % (self.root.winfo_reqwidth(), 500))

        self.root.mainloop()

class ListadoAlumnos:

    def __init__(self,padre,bd):
        self.root = Toplevel(padre)
        self.root.title("Listado de Alumnos")
        self.root.resizable(0,0)
        self.bd=bd
        tablas = self.bd.getTablas()

        self.table = Table(self.root,
                           ["Nro de Registro", "Nombre", "Apellido","DNI","Dirección","Teléfono","Email","F. de Nacimiento","Curso","Fecha Ingreso","Fecha Egreso","Usuario","Concepto","Inasistencias"],
                           column_minwidths=[None, None, None, None, None, None, None, None, None, None, None, None, None, None], height=700)
        self.table.pack(expand=True, fill=X, padx=10, pady=10)

        for alumno in tablas[0]:
            fechas = alumno.getFechas()
            fNac = '/'.join(str(v) for v in list(alumno.getFNac()))
            fIngreso = '/'.join(str(v) for v in list(fechas[0]))
            fEgreso = '/'.join(str(v) for v in list(fechas[1]))
            userpass = alumno.getUserPass()
            self.table.insert_row([alumno.getRegistro(),alumno.getNombre(),alumno.getApellido(),alumno.getDni(),alumno.getDireccion(),alumno.getTelefono(),alumno.getEmail(),fNac,alumno.getCurso(),fIngreso,fEgreso,userpass[0],userpass[1],alumno.getConcepto(),alumno.getInasistencias()])

        self.root.update()
        self.root.mainloop()

class ListadoReadmisiones:

    def __init__(self,padre,bd):
        self.root = Toplevel(padre)
        self.root.title("Listado de Readmisiones")
        self.root.resizable(0, 0)
        self.bd = bd
        tablas = self.bd.getTablas()
        listado = filter(lambda x: x.getInasistencias()>15,tablas[0])

        self.table = Table(self.root,["Nombre","Apellido","Curso","Concepto"], column_minwidths=[None,None,None,None])
        self.table.pack(expand=True, fill=X, padx=10, pady=10)

        for alumno in listado:
            self.table.insert_row([alumno.getNombre(),alumno.getApellido(),alumno.getCurso(),alumno.getConcepto()])

        self.root.update()
        self.root.mainloop()

class ListadoCurso:

    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title("Listado por Curso")
        self.raiz.geometry("400x550")
        self.bd = bd
        negrita = font.Font(weight='bold', size=10)

        self.curso = IntVar()
        self.aviso = StringVar()
        self.labelcurso = ttk.Label(self.raiz, text="Curso", font=negrita, padding=(5, 5))
        self.fieldcurso = ttk.Entry(self.raiz, textvariable=self.curso, width=15)

        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, font=negrita, padding=(5, 5))
        self.bBuscar = ttk.Button(self.raiz, text="Buscar", padding=(5, 5), command=lambda: self.buscar())
        self.table = Table(self.raiz,["Apellido","Nombre","DNI","Nro de Registro"],column_minwidths=[None,None,None,None])
        self.table.pack(expand=True, fill=X, padx=10, pady=10)

        self.labelcurso.place(x=40, y=40)
        self.fieldcurso.place(x=100, y=42)
        self.bBuscar.place(x=250, y=40)
        self.table.place(x=40, y=100)

    def buscar(self):
        errorcurso = False
        self.aviso.set("")
        if self.curso.get()<1 or self.curso.get()>6:
            self.labelaviso.configure(foreground="red")
            self.aviso.set("Curso erróneo")
        else:
            tablas = self.bd.getTablas()
            listaordenada = list(functools.reduce(sortAlf,tablas[0],[]))
            listamap = list(map(lambda x :[x.getApellido(),x.getNombre(),x.getDni(),x.getRegistro()], listaordenada))

            for alumno in listamap:
                self.table.insert_row([alumno[0],alumno[1],alumno[2],alumno[3]])
            self.raiz.update()



class ListarLegajo:

    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.resizable(0,0)
        self.raiz.title("Modificación de Alumno")
        self.raiz.geometry("1160x560")
        negrita = font.Font(weight='bold', size=10)
        titulo = font.Font(weight="bold", size=12)
        self.bd = bd

        self.aviso = StringVar()
        self.labeltitulo = ttk.Label(self.raiz, text="Modificación de los datos del Alumno", font=titulo, padding=(5, 5))
        self.labeldpersonales = ttk.Label(self.raiz, text="Datos Personales", font=titulo, padding=(5, 5))
        self.labeldacademicos = ttk.Label(self.raiz, text="Datos académicos", font=titulo,)
        self.labelaviso = ttk.Label(self.raiz, textvariable = self.aviso, font=titulo, padding=(5, 5))
        self.labelbusqueda = ttk.Label(self.raiz,text="Ingrese el numero de registro", font=titulo, padding=(5, 5))
        self.labelNotas = ttk.Label(self.raiz,text="Notas del alumno", font=titulo, padding=(5, 5))
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

        self.fnombre = ttk.Label(self.raiz, textvariable=self.nombre)
        self.fapellido = ttk.Label(self.raiz, textvariable=self.apellido)
        self.fdni = ttk.Label(self.raiz, textvariable=self.dni)
        self.fdireccion = ttk.Label(self.raiz, textvariable=self.direccion)
        self.ftelefono = ttk.Label(self.raiz, textvariable=self.telefono)
        self.femail = ttk.Label(self.raiz, textvariable=self.email)
        self.ffnac = ttk.Label(self.raiz, textvariable=self.fnac)
        self.fcurso = ttk.Label(self.raiz, textvariable=self.curso)
        self.fregistro = ttk.Label(self.raiz, textvariable=self.registro)
        self.ffingreso = ttk.Label(self.raiz, textvariable=self.fingreso)
        self.ffegreso = ttk.Label(self.raiz, textvariable=self.fegreso)
        self.fuser = ttk.Label(self.raiz, textvariable=self.user)
        self.fpword = ttk.Label(self.raiz, textvariable=self.pword)
        self.finasistencias = ttk.Label(self.raiz, textvariable=self.inasistencias)
        self.fconcepto = ttk.Label(self.raiz, textvariable=self.concepto)
        self.fbusqueda = ttk.Entry(self.raiz, textvariable=self.regBuscar, width=15)

        self.bBuscar = ttk.Button(self.raiz, text="Buscar", padding=(5, 5), command=lambda: self.buscar())

        self.table = Table(self.raiz,
                           ["Nro de Registro", "Código de Materia", "Nombre", "Nota 1C", "Nota 2C", "Nota 3C"],
                           column_minwidths=[None, None, None, None, None, None], height=700)
        self.table.pack(expand=True, fill=X, padx=10, pady=10)

        self.labeltitulo.place(x=250, y=5)
        self.labelbusqueda.place(x=40, y=55)
        self.fbusqueda.place(x=280, y=62)
        self.bBuscar.place(x=400, y=58)

        self.labeldpersonales.place(x=40, y=100)
        self.labelNotas.place(x=600,y=100)

        self.label1.place(x=40, y=140)
        self.fnombre.place(x=140, y=144)
        self.label2.place(x=360, y=140)
        self.fapellido.place(x=460, y=144)
        self.table.place(x=600, y=140)

        self.label9.place(x=40, y=180)
        self.fregistro.place(x=140, y=184)
        self.label3.place(x=360, y=180)
        self.fdni.place(x=460, y=184)

        self.label4.place(x=40, y=220)
        self.fdireccion.place(x=140, y=224)
        self.label5.place(x=360, y=220)
        self.ftelefono.place(x=460, y=224)

        self.label6.place(x=40, y=260)
        self.femail.place(x=140, y=264)
        self.label7.place(x=40, y=300)
        self.ffnac.place(x=140, y=3040)
        self.label8.place(x=360, y=300)
        self.fcurso.place(x=460, y=304)

        self.labeldacademicos.place(x=40, y=360)
        self.label10.place(x=40, y=400)
        self.ffingreso.place(x=140, y=404)
        self.label15.place(x=360, y=400)
        self.ffegreso.place(x=460, y=404)
        self.label11.place(x=40, y=440)
        self.fuser.place(x=140, y=4440)
        self.label12.place(x=360, y=440)
        self.fpword.place(x=460, y=444)

        self.label13.place(x=40, y=480)
        self.finasistencias.place(x=140, y=484)
        self.label14.place(x=360, y=480)
        self.fconcepto.place(x=460, y=484)

        self.labelaviso.place(x=40, y= 520)

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

                    for materia in tablas[1]:
                        notas = materia.getNotas()
                        registro = materia.getCodigoAlumno()
                        codigo = materia.getCodigoMateria()
                        nombre = materia.getNombre()
                        self.table.insert_row([registro, codigo, nombre, notas[0], notas[1], notas[2]])

                    break
            if not encontrado:
                self.labelaviso.configure(foreground="red")
                self.aviso.set("Registro inexistente")


def sortAlf(lista,e):
    i = 0
    n = len(lista)
    while i < n and e.getApellido().upper() > lista[i].getApellido().upper():
        i = i + 1
    lista.insert(i,e)
    return lista