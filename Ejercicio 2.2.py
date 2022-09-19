# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).

from tkinter import *
from tkinter import messagebox
listP = []

class Contador(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def añadirPelicula(self):
        p = self.peli.get()
        numlen = len(str(p))
        if numlen == 0:
            messagebox.showinfo(message="Por favor ingrese el nombre de una pelicula.", title="Error")
        else:
            listP.append(p)
            for i in range(len(listP)):
                self.lista.insert(0, str(listP[i]))
                listP.pop(i)
            

    def createWidgets(self):

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
        
ventana = Tk()
ventana.title("Películas")
ventana.resizable(False, False)
ventana.geometry("400x200")
root = Contador(ventana).grid()

ventana.mainloop()
