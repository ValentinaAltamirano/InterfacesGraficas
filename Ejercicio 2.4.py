# Escribir una aplicación GUI (llamada Calculadora 2) como la que se ve
# en la figura y que funcione como una calculadora.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculadora 2")
        self.resizable(False, False)
        self.geometry("370x220")
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
        else:
            messagebox.showinfo(message="Ingrese un numero porfavor.", title="Error")

    def restar(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            res = float(p) - float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(res))
            self.res.config(state= 'readonly')    
        else:
            messagebox.showinfo(message="Ingrese un numero porfavor.", title="Error")    

    def multiplicar(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            m = float(p) * float(s)
            self.res.delete(0, END)
            self.res.insert(0, str(m))  
            self.res.config(state= 'readonly')  
        else:
            messagebox.showinfo(message="Ingrese un numero porfavor.", title="Error")

    def dividir(self):
        self.res.config(state=tk.NORMAL)
        p = self.entrada1.get()
        s = self.entrada2.get()
        if self.validar(p) and self.validar(s):
            if int(s) == 0:
                messagebox.showinfo(message="No se puede dividir por cero.", title="Error")
            else:
                d = float(p) / float(s)
                self.res.delete(0, END)
                self.res.insert(0, str(d)) 
                self.res.config(state= 'readonly')   
        else:
            messagebox.showinfo(message="Ingrese un numero porfavor.", title="Error")

    def calcular(self):
        num = self.radioValue.get()
        if num == 1:
            self.sumar()
        elif num == 2:
            self.restar()
        elif num == 3:
            self.multiplicar()
        elif num == 4:
            self.dividir()
        else:
            messagebox.showinfo(message="Ingrese una operacion.", title="Error")
            

    def Widgets(self):
        self.radioValue = tk.IntVar() 

        self.e = Label(self, text="Valor 1")
        self.e.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.entrada1 = Entry(self)
        self.entrada1.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
        self.entrada1.insert(0,'0')

        self.e2 = Label(self, text="Valor 2")
        self.e2.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        self.entrada2 = Entry(self)
        self.entrada2.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
        self.entrada2.insert(0,'0')
        
        self.r = Label(self, text="Resultado")
        self.r.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

        self.res = Entry(self)
        self.res.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
        self.res.insert(0,'0')
        self.res.config(state='readonly')

        self.op = Label(self, text="Operaciones")
        self.op.grid(column=3, row=0, sticky=tk.EW, padx=20, pady=5)

        self.suma = Radiobutton(self, text="Sumar",variable=self.radioValue, value=1)
        self.suma.grid(column=3, row=1, sticky=tk.EW, padx=5, pady=5)

        self.resta = Radiobutton(self, text="Restar",variable=self.radioValue, value=2)
        self.resta.grid(column=3, row=2, sticky=tk.EW, padx=5, pady=5)

        self.mult = Radiobutton(self, text="Multiplicar",variable=self.radioValue, value=3)
        self .mult.grid(column=3, row=3, sticky=tk.E, padx=5, pady=5)

        self.div = Radiobutton(self, text="Dividir",variable=self.radioValue, value=4)
        self.div.grid(column=3, row=4, sticky=tk.EW, padx=5, pady=5)

        self.calculo = Button(self, text="Calcular",command=lambda: self.calcular())
        self.calculo.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)

root = Calculadora()
root.mainloop()
