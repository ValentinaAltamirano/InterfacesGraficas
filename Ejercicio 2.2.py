# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).

from tkinter import *
import tkinter as tk
from tkinter import messagebox

class Peliculas(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Películas")
        self.resizable(False, False)
        self.geometry("400x200")
        self.Widgets()

    def añadirPelicula(self):
        p = self.peli.get()
        numlen = len(str(p))
        if numlen == 0:
            messagebox.showinfo(message="Por favor ingrese el nombre de una pelicula.", title="Error")
        else:
            self.lista.insert(END, p)
            self.peli.delete(0, END)

    def Widgets(self):

        self.p = Label(self, text="Escribe el titulo de la película:")
        self.p.grid(row=1, column=1, sticky="sew", padx = 15)

        self.peli = Entry(self)
        self.peli.grid(row=2, column=1, sticky="sew", padx = 15)

        self.añadir = Button(self, text="Añadir",command=lambda: self.añadirPelicula())
        self.añadir.grid(row=3, column=1, sticky="sew", padx = 15)

        self.p = Label(self, text="Peliculas")
        self.p.grid(row=2, column=2, sticky="sew", padx = 5)

        self.lista = Listbox(self)
        self.lista.insert(0, 'Tom y Jerry')
        self.lista.insert(1, '7 Almas')
        self.lista.grid(row=0, column=5, sticky=EW, rowspan=5,pady = 5)
        

root = Peliculas()

root.mainloop()
