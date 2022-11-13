import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.abrirVentana1()

    def abrirVentana1(self):
        self.lbl3=tk.Label(text=" ",font=("Arial",20), width=24, height=14, bg="firebrick3", fg="firebrick3")
        self.lbl3.place(x=5,y=5)
        self.lbl4=tk.Label(text=" ", font=("Arial", 20), width=1, height=14, bg="gray", fg="gray")
        self.lbl4.place(x=50,y=5)
        self.lbl5=tk.Label(text=" ", font=("Arial",20), width=1, height=14, bg="gray", fg="gray")
        self.lbl5.place(x=330,y=5)
        self.lbl6=tk.Label(text="MENÚ", font=("Times New Roman", 25), width=5, height=1, bg="firebrick3", fg="white")
        self.lbl6.place(x=155,y=20)
        self.boton2=tk.Button(text="DIAGRAMAS", font=("Times New Roman", 25), bg="snow", fg="gray")
        self.boton2.place(x=100,y=90,width=200,height=30)
        self.boton3=tk.Button(text="STELLA", font=("Times New Roman", 25), bg="snow", fg="gray")
        self.boton3.place(x=100,y=150,width=200,height=30)
        self.boton4=tk.Button(text="TABLAS", font=("Times New Roman", 25), bg="snow", fg="gray")
        self.boton4.place(x=100,y=210,width=200,height=30)
        self.boton4["command"] = self.abrirTabla
        
    def abrirTabla(self):
        self.newWindow = tk.Toplevel()
        self.newWindow.title("TABLA")
        # self.newWindow.geometry("400x450")
        lst = [ (1,'Raj','Mumbai',19), 
                        (2,'Aaryan','Pune',18), 
                        (3,'Vaishnavi','Mumbai',20), 
                        (4,'Rachna','Mumbai',21), 
                        (5,'Shubham','Delhi',21)] 
        for i in range(5):
            for j in range(4):
                celda = tk.Entry(self.newWindow, width=20, fg="blue", font=("Arial","16","bold"))
                celda.grid(row=i,column=j)
                
                celda.insert(tk.END,lst[i][j])

class Tabla(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.abrirVentana1()

    def abrirVentana1(self):
        self.lbl=tk.Label(text="hola")
        self.lbl.place(x=5,y=5)
        self.lbl.pack()

win1=tk.Tk()
win1.title("MENÚ")
win1.geometry("400x450")
win1.configure(background="snow")
app = Application(master = win1)
app.mainloop()