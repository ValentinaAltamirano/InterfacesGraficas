# Escribir una aplicación GUI (llamada Calculadora) que funcione como
# una simple calculadora.
# La aplicación lleva:
# 1 - Tres etiquetas (Primer número, Segundo número y Resultado)
# 2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar)
# 3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
# 3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica
# es Resultado.

# Escribir una aplicación GUI (llamada Calculadora) que funcione como
# una simple calculadora.
# La aplicación lleva:
# 1 - Tres etiquetas (Primer número, Segundo número y Resultado)
# 2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar)
# 3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los
# 3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica
# es Resultado.

from tkinter import *
import tkinter as tk
import random

class Contador(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Generador de números")
        self.resizable(False, False)
        self.geometry("400x180")
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=3)
        self.Widgets()

    def validar(self,n):
        try:
            int(n)
            return True
        except:
            return False  

    def generarNumero(self):
        self.res.config(state=tk.NORMAL)
        n1 = self.entrada1.get()
        n2 = self.entrada2.get()
        if self.validar(n1) and self.validar(n2):
            num = random.randint(int(n1), int(n2))
            self.res.delete(0, END)
            self.res.insert(0, str(num))
            self.res.config(state='readonly')
            

    def Widgets(self):
        self.e = Label(self, text="Primer número")
        self.e.grid(column=0, row=0, sticky=tk.E, padx=5, pady=10)

        self.entrada1 = Spinbox(self)
        self.entrada1.grid(column=1, row=0, sticky=tk.W, padx=0, pady=10)

        self.e2 = Label(self, text="Segundo número")
        self.e2.grid(column=0, row=1, sticky=tk.E, padx=5, pady=10)

        self.entrada2 = Spinbox(self)
        self.entrada2.grid(column=1, row=1, sticky=tk.W, padx=0, pady=10)

        self.r = Label(self, text="Número generado")
        self.r.grid(column=0, row=3, sticky=tk.E, padx=5, pady=10) 

        self.res = Entry(self,state= 'readonly')
        self.res.grid(column=1, row=3, sticky=tk.W, padx=0, pady=5) 

        self.gen = Button(self,text="Añadir",command=lambda: self.generarNumero())
        self.gen.grid(column=1, row=4, sticky=tk.SW, padx=35, pady=5)

root = Contador()
root.mainloop()
