# Escribir una aplicación GUI (llamada ContCreciente) como la que se
# ve en la figura. Cada vez que se haga clic en el botón "+", el valor del
# contador se incrementa en 1.

# Escribir una aplicación GUI (llamada ContCreciente) como la que se
# ve en la figura. Cada vez que se haga clic en el botón "+", el valor del
# contador se incrementa en 1.

from tkinter import *
import tkinter as tk

class Contador(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("ContCreciente")
        self.resizable(False, False)
        self.geometry("300x160")
        self.columnconfigure(0, weight=4)
        self.columnconfigure(2, weight=3)
        self.rowconfigure(1, weight=5)
        self.Widgets()

    def sumar(self):
        self.entrada.config(state=tk.NORMAL)
        num = self.entrada.get()
        numlen = len(str(num))
        if numlen == 0:
            numN = 0
            numN += 1
            self.entrada.delete(0, END)
            self.entrada.insert(0, str(numN))
            self.entrada.config(state='readonly')
        else:
            num = int(num)
            num += 1
            self.entrada.delete(0, END)
            self.entrada.insert(0, str(num))
            self.entrada.config(state='readonly')
            

    def Widgets(self):

        self.cont = Label(self, text="Contador:")
        self.cont.grid(column=0, row=1, sticky=tk.E, padx=5, pady=10)

        self.entrada = Entry(self,state= 'readonly')
        self.entrada.grid(column=1, row=1, sticky=tk.W, padx=0, pady=10)

        self.mas = Button(self, text="+",command=lambda: self.sumar())
        self.mas.grid(column=2, row=1, sticky=tk.W, padx=5, pady=10)
        
root = Contador()
root.mainloop()
