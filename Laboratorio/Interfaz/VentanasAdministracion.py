from tkinter import *
from tkinter import ttk,font
from Código.BD import *
from Código.Alumno import *
from Código.Materia import *


class RegistrarUsuario:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title('Acceso')
        self.raiz.resizable(0, 0)
        self.raiz.geometry("380x240")
        negrita = font.Font(weight='bold', size=10)
        self.bd=bd

        self.label1 = ttk.Label(self.raiz, text="Usuario:", font=negrita, padding=(5, 5))
        self.label2 = ttk.Label(self.raiz, text="Constraseña:", font=negrita, padding=(5, 5))
        self.label3 = ttk.Label(self.raiz, text="Tipo de usuario", font=negrita, padding=(5, 5))
        self.user = StringVar()
        self.pword = StringVar()
        self.mensaje = StringVar()
        self.label4 = ttk.Label(self.raiz, textvariable=self.mensaje, font=negrita, padding=(5, 5))
        self.label5 = ttk.Label(self.raiz, text="Ingrese los datos", font=negrita, padding=(5, 5))
        self.tipo = ttk.Combobox(self.raiz, width=27, state="readonly")
        self.tipo["values"] = ["Alumno", "Docente", "Administrador"]
        self.tipo.set("Administrador")
        self.field1 = ttk.Entry(self.raiz, textvariable=self.user, width=30)
        self.field2 = ttk.Entry(self.raiz, textvariable=self.pword, width=30, show="*")

        self.bRegistrar = ttk.Button(self.raiz, text="Registrar", padding=(5, 5), command=lambda: self.registrar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.label5.place(x=120, y=5)
        self.label1.place(x=30, y=50)
        self.field1.place(x=150, y=52)
        self.label2.place(x=30, y=90)
        self.field2.place(x=150, y=92)
        self.label3.place(x=30, y=130)
        self.tipo.place(x=150, y=134)
        self.label4.place(x=30, y=155)
        self.bRegistrar.place(x=250, y=190)
        self.bCancelar.place(x=150, y=190)

        self.field1.focus_set()
        self.raiz.grab_set()
        self.raiz.mainloop()

    def registrar(self):
        acceso = self.bd.getAcceso()
        if self.user.get() == "" or self.pword.get() == "":
            self.mensaje.set("Campos vacíos")
            self.label4.configure(foreground="red")
        else:
            usuarioA = "A-" + self.user.get()
            usuarioD = "D-" + self.user.get()
            usuarioP = "P-" + self.user.get()

            if usuarioA in acceso or usuarioD in acceso or usuarioP in acceso:
                self.mensaje.set("Usuario en uso")
                self.label4.configure(foreground="red")
            else:
                self.mensaje.set("Registrado exitosamente")
                self.label4.configure(foreground="blue")
                if self.tipo.get() == "Alumno":
                    usuario = usuarioA
                elif self.tipo.get() == "Docente":
                    usuario = usuarioD
                else:
                    usuario = usuarioP
                acceso[usuario] = self.pword.get()
                self.bd.setAcceso(acceso)

# ----------------------------------------------------------------------------------------------------------------------

class EliminarUsuario:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.raiz.title('Acceso')
        self.raiz.resizable(0, 0)
        self.raiz.geometry("380x240")
        negrita = font.Font(weight='bold', size=10)
        self.bd=bd

        self.label1 = ttk.Label(self.raiz, text="Usuario:", font=negrita, padding=(5, 5))
        self.label2 = ttk.Label(self.raiz, text="Constraseña:", font=negrita, padding=(5, 5))
        self.label3 = ttk.Label(self.raiz, text="Tipo de usuario", font=negrita, padding=(5, 5))
        self.user = StringVar()
        self.pword = StringVar()
        self.mensaje = StringVar()
        self.label4 = ttk.Label(self.raiz, textvariable=self.mensaje, font=negrita, padding=(5, 5))
        self.label5 = ttk.Label(self.raiz, text="Ingrese los datos", font=negrita, padding=(5, 5))
        self.tipo = ttk.Combobox(self.raiz, width=27, state="readonly")
        self.tipo["values"] = ["Alumno", "Docente", "Administrador"]
        self.tipo.set("Administrador")
        self.field1 = ttk.Entry(self.raiz, textvariable=self.user, width=30)
        self.field2 = ttk.Entry(self.raiz, textvariable=self.pword, width=30, show="*")

        self.bEliminar = ttk.Button(self.raiz, text="Eliminar", padding=(5, 5), command=lambda: self.eliminar())
        self.bCancelar = ttk.Button(self.raiz, text="Salir", padding=(5, 5), command=lambda: self.raiz.destroy())

        self.label5.place(x=120, y=5)
        self.label1.place(x=30, y=50)
        self.field1.place(x=150, y=52)
        self.label2.place(x=30, y=90)
        self.field2.place(x=150, y=92)
        self.label3.place(x=30, y=130)
        self.tipo.place(x=150, y=134)
        self.label4.place(x=30, y=155)
        self.bEliminar.place(x=250, y=190)
        self.bCancelar.place(x=150, y=190)

        self.field1.focus_set()
        self.raiz.grab_set()
        self.raiz.mainloop()

    def eliminar(self):
        acceso = self.bd.getAcceso()
        if self.user.get() == "" or self.pword.get() == "":
            self.mensaje.set("Campos vacíos")
            self.label4.configure(foreground="red")
        else:
            usuarioA = "A-" + self.user.get()
            usuarioD = "D-" + self.user.get()
            usuarioP = "P-" + self.user.get()

            if usuarioA in acceso or usuarioD in acceso or usuarioP in acceso:
                if self.tipo.get() == "Alumno":
                    usuario = usuarioA
                elif self.tipo.get() == "Docente":
                    usuario = usuarioD
                else:
                    usuario = usuarioP

                if acceso[usuario] == self.pword.get():
                    self.mensaje.set("Eliminado exitosamente")
                    self.label4.configure(foreground="blue")
                    del acceso[usuario]
                    self.bd.setAcceso(acceso)
                else:
                    self.mensaje.set("Contraseña incorrecta")
                    self.label4.configure(foreground="red")
            else:
                self.mensaje.set("Usuario inexistente")
                self.label4.configure(foreground="red")

# ----------------------------------------------------------------------------------------------------------------------

class Inicializar:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.bd=bd
        self.raiz.geometry("400x180")
        self.raiz.title("Inciar sesion de trabajo")
        self.raiz.resizable(0,0)
        negrita = font.Font(weight='bold', size=10)

        self.archivo = StringVar()
        self.aviso = StringVar()

        self.labelaviso = ttk.Label(self.raiz, textvariable = self.aviso, padding=(5, 5))
        self.label1 = ttk.Label(self.raiz, text="Ingrese el nombre del archivo que quiere cargar", padding=(5,5), font=negrita)
        self.nombre = ttk.Entry(self.raiz, textvariable=self.archivo, width=50)
        self.bcarga = ttk.Button(self.raiz, text="Cargar", padding=(5,5), command=lambda: self.carga())
        self.bsalir = ttk.Button(self.raiz, text="Salir", padding=(5,5), command=lambda: self.raiz.destroy())

        self.label1.place(x=35, y=20)
        self.nombre.place(x=40, y=60)
        self.labelaviso.place(x=40, y=90)
        self.bcarga.place(x=260, y=120)
        self.bsalir.place(x=160, y=120)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def carga(self):
        nombre = self.archivo.get()
        self.aviso.set("")
        try:
            arch = open( nombre + ".txt","r")
        except FileNotFoundError:
            arch = open(nombre + ".txt", "a")
            arch.close()
            arch = open( nombre + ".txt","r")
        alumno = Alumno()
        materia = Materia()
        listaAlumno = []
        listMateria = []
        acceso = {}
        nombreTablas = {}
        i=0
        # mientras no termine el archivo y llegue al salto de línea donde termina la tabla
        linea = arch.readline().rstrip('\n')
        if linea == "":
            self.labelaviso.configure(foreground="red")
            self.aviso.set("El archivo está vacío")
        else:
            cantUsuarios = int(linea)
            linea = arch.readline().rstrip('\n')
            while True and linea != "":
                #lee la cantidad de usuarios
                try:
                    aux = linea.split(",")
                    acceso[aux[0]] = aux[1]
                    linea = arch.readline().rstrip('\n')
                except EOFError:
                    break
            linea = arch.readline().rstrip('\n')
            while True and linea!="":
                try:
                    nombreTablas[linea] = i
                    i=i+1
                    linea = arch.readline().rstrip('\n')
                except EOFError:
                    break
            linea = arch.readline().rstrip('\n')
            while True and linea!="":
                #lee la tabla alumnos
                try:
                    aux = linea.split(",")
                    fechaAux1 = aux[7].split("-")
                    fechaNac = (int(fechaAux1[0]),int(fechaAux1[1]),int(fechaAux1[2]))
                    fechaAux2 = aux[9].split("-")
                    fechaAlta = (int(fechaAux2[0]), int(fechaAux2[1]), int(fechaAux2[2]))
                    fechaAux3 = aux[10].split("-")
                    fechaBaja = (int(fechaAux3[0]), int(fechaAux3[1]), int(fechaAux3[2]))
                    fechas = (fechaAlta, fechaBaja)
                    userpass = (aux[11], aux[12])

                    alumno = Alumno(int(aux[0]), aux[1], aux[2], int(aux[3]),
                                    aux[4], int(aux[5]), aux[6], fechaNac, int(aux[8]),
                                    fechas, userpass,aux[13],int(aux[14]), [])
                    listaAlumno.append(alumno)
                    linea = arch.readline().rstrip('\n')
                except EOFError:
                    break
            linea = arch.readline().rstrip('\n')
            while True and linea!="":
                #lee la tabla materias
                try:
                    aux = linea.split(",")
                    notasAux = aux[3].split("-")
                    notas = (int(notasAux[0]), int(notasAux[1]), int(notasAux[2]))
                    materia = Materia(int(aux[1]),int(aux[0]),aux[2],notas)

                    listMateria.append(materia)
                    for alumno in listaAlumno:
                        if alumno.getRegistro() == materia.getCodigoAlumno():
                            listaMaterias = alumno.getMaterias()
                            listaMaterias.append(materia)
                            alumno.setMaterias(listaMaterias)
                    linea = arch.readline().rstrip('\n')
                except EOFError:
                    break
            tablaMateria = TablaMaterias()
            tablaMateria.setLista(listMateria)
            tablaAlumno = TablaAlumnos()
            tablaAlumno.setLista(listaAlumno)
            tablas = (tablaAlumno,tablaMateria)
            self.bd.setCantUsuarios(cantUsuarios)
            self.bd.setAcceso(acceso)
            self.bd.setNbreTablas(nombreTablas)
            self.bd.setTablas(tablas)
            self.labelaviso.configure(foreground="blue")
            self.aviso.set("Archivo cargado")

# ----------------------------------------------------------------------------------------------------------------------

class Backup:
    def __init__(self,padre,bd):
        self.raiz = Toplevel(padre)
        self.bd=bd
        self.raiz.geometry("400x180")
        self.raiz.title("Almacenar en disco (Backup)")
        self.raiz.resizable(0,0)
        negrita = font.Font(weight='bold', size=10)

        self.archivo = StringVar()
        self.aviso = StringVar()

        self.labelaviso = ttk.Label(self.raiz, textvariable=self.aviso, padding=(5, 5))
        self.label1 = ttk.Label(self.raiz, text="Ingrese el nombre del archivo donde desea guardar", padding=(5,5), font=negrita)
        self.nombre = ttk.Entry(self.raiz, textvariable=self.archivo, width=50)
        self.bguardar = ttk.Button(self.raiz, text="Guardar", padding=(5,5), command=lambda: self.backup())
        self.bsalir = ttk.Button(self.raiz, text="Salir", padding=(5,5), command=lambda: self.raiz.destroy())

        self.label1.place(x=35, y=20)
        self.nombre.place(x=40, y=60)
        self.labelaviso.place(x=40, y=90)
        self.bguardar.place(x=260, y=120)
        self.bsalir.place(x=160, y=120)

        self.raiz.grab_set()
        self.raiz.mainloop()

    def backup(self):
        nombre = self.archivo.get()
        self.aviso.set("")
        try:
            arch = open(nombre + ".txt", "w")
        except FileNotFoundError:
            arch = open(nombre + ".txt", "a")
            arch.close()
            arch = open(nombre + ".txt", "w")
        tablas = self.bd.getTablas()
        acceso = self.bd.getAcceso()
        nombreTablas = self.bd.getNbreTablas()
        # escriba la tabla alumnos
        linea = str(self.bd.getCantUsuarios()) + "\n"
        arch.write( linea)
        for user,pword in acceso.items():
            linea = user+","+pword
            arch.write(linea+"\n")
        arch.write("\n")
        for nombre in nombreTablas:
            arch.write(nombre +"\n")
        arch.write("\n")
        for alumno in tablas[0]:
            fechaNac = alumno.getFNac()
            fechaAlta = alumno.getFechas()[0]
            fechaBaja = alumno.getFechas()[1]
            user = alumno.getUserPass()[0]
            pword = alumno.getUserPass()[1]
            linea = str(alumno.getRegistro()) + "," + alumno.getNombre() + "," + alumno.getApellido() + "," + str(alumno.getDni()) + "," + \
                    alumno.getDireccion() + "," + str(alumno.getTelefono()) + "," + alumno.getEmail() + "," + str(fechaNac[0]) + "-" + str(fechaNac[1]) + "-" + \
                    str(fechaNac[2]) + "," + str(alumno.getCurso()) + "," + str(fechaAlta[0]) + "-" + str(fechaAlta[1]) + "-" + \
                    str(fechaAlta[2]) + "," + str(fechaBaja[0]) + "-" + str(fechaBaja[1]) + "-" + str(fechaBaja[2]) + "," + user + "," +\
                    pword + "," + alumno.getConcepto()+ "," + str(alumno.getInasistencias())
            arch.write(linea+"\n")
        # Escribe un salto de línea para diferenciar donde empieza una tabla y termina la otra
        arch.write("\n")
        # Escribe la tabla materias
        for materia in tablas[1]:
            notas = materia.getNotas()
            linea = str(materia.getCodigoAlumno()) + "," + str(materia.getCodigoMateria()) + "," + materia.getNombre() + "," + \
                    str(notas[0]) + "-" + str(notas[1]) + "-" + str(notas[2])
            arch.write(linea + "\n")
        arch.close()
        self.labelaviso.configure(foreground="blue")
        self.aviso.set("Archivo cargado")

# ----------------------------------------------------------------------------------------------------------------------

def main():
    menu = RegistrarUsuario()
    return 0

if __name__ == '__main__':
    main()