# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).

from tkinter import *
import tkinter as tk
listP = []

class Contador(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Contador")
        self.resizable(False, False)
        self.geometry("400x260")
        self.Widgets()

    def añadirPelicula(self):
        p = self.peli.get()
        listP.append(p)
        self.peli.delete(0, END)
        for i in range(len(listP)):
            self.lista.delete(i, END)
            self.lista.insert(0, str(listP[i]))
            
    def Widgets(self):

        self.p = Label(self, text="Escribe el titulo de la película:")
        self.p.grid(row=1, column=1, sticky="sew", padx=20, pady=5)

        self.peli = Entry(self)
        self.peli.grid(row=2, column=1, sticky="sew", padx=20, pady=5)

        self.añadir = Button(self, text="Añadir",command=lambda: self.añadirPelicula())
        self.añadir.grid(row=3, column=1, sticky="sew", padx=20, pady=5)

        self.p = Label(self, text="Peliculas")
        self.p.grid(row=0, column=5, sticky="sew", padx=20, pady=5)

        self.lista = Listbox(self)
        self.lista.grid(row=1, column=5,rowspan=4, sticky="sew", padx=20, pady=5)
        

root = Contador()

root.mainloop()