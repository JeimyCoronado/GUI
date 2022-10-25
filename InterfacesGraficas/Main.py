import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.fondo = tk.PhotoImage(file="uni.png")
        self.background = tk.Label(image=self.fondo, text="hola", bd=0)
        self.fondo.re
        self.botonForrester = tk.Button(self.background)
        self.botonTabla = tk.Button(self.background)
        self.botonComportamiento = tk.Button(self.background)
        self.botonForrester["text"] = "FORRESTER"
        self.botonForrester["command"] = self.abrirForrester
        self.botonForrester.pack(side="top", expand=True)
        self.botonTabla["text"] = "TABLA"
        self.botonTabla["command"] = self.abrirTabla
        self.botonTabla.pack(side="top", expand=True)
        self.botonComportamiento["text"] = "COMPORTAMIENTO"
        self.botonComportamiento["command"] = self.abrirComportamiento
        self.botonComportamiento.pack(side="top", expand=True)

        self.QUIT = tk.Button(self.background, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom", expand=True)
        self.background.pack(expand=True)

    def abrirForrester(self):
        root = tk.Tk()
        app = Forrester(master=root)
        app.mainloop()

    def abrirTabla(self):
        root = tk.Tk()
        app = Tabla(master=root)
        app.mainloop()

    def abrirComportamiento(self):
        root = tk.Tk()
        app = Comportamiento(master=root)
        app.mainloop()

class Forrester(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.mensaje = tk.Label(self, text="Bienvenido al Forrester").pack()

class Tabla(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.mensaje = tk.Label(self,text="Bienvenido a la Tabla").pack()

class Comportamiento(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.mensaje = tk.Label(self,text="Bienvenido al Comportamiento").pack()

root = tk.Tk()
root.geometry("475x468")
app = Application(master=root)
app.mainloop()


# from tkinter import *
#
# root = Tk()
#
# imagen= PhotoImage(file="uni.png")
#
# Label(root, image=imagen, bd=0).pack()
#
# root.mainloop()