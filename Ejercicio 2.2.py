# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).

# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).

from tkinter import *
listP = []

class Contador(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def añadirPelicula(self):
        p = self.peli.get()
        listP.append(p)
        self.peli.delete(0, END)
        self.lista.delete(0, END)
        self.lista.insert(0, str(listP))
            

    def createWidgets(self):

        self.p = Label(self, text="Escribe el titulo de la película:")
        self.p.grid(row=1, column=1, sticky="sew")

        self.peli = Entry(self)
        self.peli.grid(row=2, column=1, sticky="sew")

        self.añadir = Button(self, text="Añadir",command=lambda: self.añadirPelicula())
        self.añadir.grid(row=3, column=1, sticky="sew")

        self.p = Label(self, text="Peliculas", state=DISABLED)
        self.p.grid(row=2, column=2, sticky="sew")

        self.lista = Listbox(self)
        self.lista.grid(row=2, column=5, sticky="sew")
        
ventana = Tk()
ventana.title("Películas")
ventana.resizable(False, False)
ventana.geometry("400x260")
root = Contador(ventana).grid()

ventana.mainloop()
