from tkinter import *
from tkinter import ttk, font
from Código.BD import BD
from Interfaz.Menu import *


class Login:

    def __init__(self,bd):
        self.raiz = Tk()
        self.bd=bd
        self.raiz.title('Acceso')
        self.raiz.resizable(0, 0)
        self.raiz.geometry("380x240")
        negrita = font.Font(weight='bold', size=10)
        self.label1 = ttk.Label(self.raiz, text="Usuario:", font=negrita, padding=(5, 5))
        self.label2 = ttk.Label(self.raiz, text="Constraseña:", font=negrita, padding=(5, 5))
        self.label3 = ttk.Label(self.raiz, text="Tipo de usuario", font=negrita, padding=(5, 5))
        self.user = StringVar()
        self.pword = StringVar()
        self.mensaje = StringVar()
        self.label4 = ttk.Label(self.raiz, textvariable=self.mensaje, font=negrita, padding=(5, 5))

        self.tipo = ttk.Combobox(self.raiz, width=27, state="readonly")
        self.tipo["values"] = ["Alumno", "Docente", "Administrador"]
        self.tipo.set("Administrador")
        self.field1 = ttk.Entry(self.raiz, textvariable=self.user, width=30)
        self.field2 = ttk.Entry(self.raiz, textvariable=self.pword, width=30, show="*")

        self.bAceptar = ttk.Button(self.raiz, text="Aceptar", padding=(5, 5), command=lambda: self.aceptar())
        self.bCancelar = ttk.Button(self.raiz, text="Cancelar", padding=(5, 5), command=quit)

        self.label1.place(x=30, y=40)
        self.field1.place(x=150, y=42)
        self.label2.place(x=30, y=80)
        self.field2.place(x=150, y=82)
        self.label3.place(x=30, y=120)
        self.tipo.place(x=150, y=124)
        self.label4.place(x=30, y=155)
        self.bAceptar.place(x=250, y=190)
        self.bCancelar.place(x=150, y=190)

        self.field1.focus_set()
        self.raiz.mainloop()

    def aceptar(self):
        acceso= self.bd.getAcceso()
        if self.tipo.get()=="Alumno" :
            usuario = "A-"+self.user.get()
            if usuario in acceso:
                if acceso[usuario]==self.pword.get():
                    self.raiz.destroy()
                    menu = Menu(self.bd)
                else:
                    self.label4.configure(foreground = "red")
                    self.mensaje.set("Contraseña incorrecta")
            else:
                self.label4.configure(foreground="red")
                self.mensaje.set("Usuario incorrecto")
        elif self.tipo.get()=="Docente":
            usuario = "D-" + self.user.get()
            if usuario in acceso:
                if acceso[usuario] == self.pword.get():
                    self.raiz.destroy()
                    menu = Menu(self.bd)
                else:
                    self.label4.configure(foreground = "red")
                    self.mensaje.set("Contraseña incorrecta")
            else:
                self.label4.configure(foreground="red")
                self.mensaje.set("Usuario incorrecto")
        else:
            usuario = "P-" + self.user.get()
            if usuario in acceso:
                if acceso[usuario] == self.pword.get():
                    self.raiz.destroy()
                    menu = Menu(self.bd)

                else:
                    self.label4.configure(foreground = "red")
                    self.mensaje.set("Contraseña incorrecta")
            else:
                self.label4.configure(foreground="red")
                self.mensaje.set("Usuario incorrecto")