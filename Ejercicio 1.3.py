# Escribir una aplicación GUI (llamada Factorial) como la que se ve en
# la figura. Cada ves que se haga clic en el botón "Siguiente", debe
# calcular el factorial del primer lineEdit y mostrarlo en el segundo. Al
# dar siguiente (n se incrementa en 1) n = 2 con su factorial
# correspondiente.

from tkinter import *
import tkinter as tk

class Factorial(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Factorial")
        self.resizable(False, False)
        self.geometry("400x160")
        self.columnconfigure(0, weight=4)
        self.columnconfigure(2, weight=5)
        self.Widgets()

    def numero(self):
        self.num.config(state=tk.NORMAL)
        self.num2.config(state=tk.NORMAL)
        num = self.num.get()
        numlen = len(str(num))
        if numlen == 0:
            numN = 0
            numN += 1
            self.num.delete(0, END)
            self.num.insert(0, str(numN))
            f = self.factor(numN)
            self.num2.delete(0, END)
            self.num2.insert(0, str(f))
            self.num.config(state= 'readonly')
            self.num2.config(state= 'readonly')
        else:
            num = int(num)
            num += 1
            self.num.delete(0, END)
            self.num.insert(0, str(num))
            f = self.factor(num)
            self.num2.delete(0, END)
            self.num2.insert(0, str(f))
            self.num.config(state= 'readonly')
            self.num2.config(state= 'readonly')
        
            
    def factor(self,n):
        return 1 if (n==1 or n==0) else n * self.factor(n - 1); 

    def Widgets(self):

        self.n = Label(self, text="n")
        self.n.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        self.num = Entry(self,state= 'readonly')
        self.num.grid(column=1, row=0, sticky=tk.W, padx=0, pady=5)

        self.factorial = Label(self, text="Factorial (n)")
        self.factorial.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.num2 = Entry(self,state= 'readonly')
        self.num2.grid(column=1, row=1, sticky=tk.W, padx=0, pady=5)

        self.siguiente = Button(self, text="Siguiente",command=lambda: self.numero())
        self.siguiente.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)
        

root = Factorial()
root.mainloop()
