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
from wsgiref.validate import validator

class Calculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Contador")
        self.resizable(False, False)
        self.geometry("250x200")
        self.Widgets()

    def validar(self,n):
        try:
            float(n)
            return True
        except:
            return False    

    def sumar(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            sum = float(p) + float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(sum))
            self.res.config(state='readonly')

    def restar(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            res = float(p) - float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(res))
            self.res.config(state= 'readonly')        

    def multiplicar(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            m = float(p) * float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(m))  
            self.res.config(state= 'readonly')      

    def dividir(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            d = float(p) / float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(d)) 
            self.res.config(state= 'readonly')   

    def modulo(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            m = float(p) % float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(m))
            self.res.config(state= 'readonly')
        
    def eliminar(self):
        self.res.config(state=tk.NORMAL)
        self.entrada1.delete(0, END)
        self.entrada2.delete(0, END)
        self.res.delete(0, END)
        self.res.config(state='readonly')
            

    def Widgets(self):
        self.e = Label(self, text="Primer número")
        self.e.grid(column=0, row=0, sticky=tk.E, padx=0, pady=5)

        self.entrada1 = Entry(self)
        self.entrada1.grid(column=1, row=0, sticky=tk.E, padx=0, pady=5)

        self.e2 = Label(self, text="Segundo número")
        self.e2.grid(column=0, row=1, sticky=tk.E, padx=0, pady=5)

        self.entrada2 = Entry(self)
        self.entrada2.grid(column=1, row=1, sticky=tk.E, padx=0, pady=5)

        self.r = Label(self, text="Resultado")
        self.r.grid(column=0, row=2, sticky=tk.E, padx=0, pady=5)

        self.res = Entry(self,state=tk.DISABLED)
        self.res.grid(column=1, row=2, sticky=tk.E, padx=0, pady=5)

        self.suma = Button(self, text="+",command=lambda: self.sumar())
        self.suma.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

        self.resta = Button(self, text="-",command=lambda: self.restar())
        self.resta.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        self.mult = Button(self, text="*",command=lambda: self.multiplicar())
        self.mult.grid(column=0, row=4, sticky=tk.EW, padx=5, pady=5)

        self.div = Button(self, text="/",command=lambda: self.dividir())
        self.div.grid(column=1, row=4, sticky=tk.EW, padx=5, pady=5)

        self.mod = Button(self, text="%",command=lambda: self.modulo())
        self.mod.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

        self.borra = Button(self, text="CLEAR",command=lambda: self.eliminar())
        self.borra.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)

root = Calculadora()
root.mainloop()
