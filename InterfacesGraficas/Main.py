import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.botonForrester = tk.Button(self)
        self.botonTabla = tk.Button(self)
        self.botonComportamiento = tk.Button(self)
        self.botonForrester["text"] = "FORRESTER"
        self.botonForrester["command"] = self.say_hi
        self.botonForrester.pack(side="top")
        self.botonTabla["text"] = "TABLA"
        self.botonTabla["command"] = self.say_hi
        self.botonTabla.pack(side="top")
        self.botonComportamiento["text"] = "COMPORTAMIENTO"
        self.botonComportamiento["command"] = self.say_hi
        self.botonComportamiento.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        root = tk.Tk()
        app = Forrester(master=root)
        app.mainloop()

class Forrester(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.mensaje = tk.Label(self,text="Bienvenido al Forrester").pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()