# Escribir una aplicación GUI (llamada Contador) como la que se ve en
# la figura. Con 3 botones (Count Up - Para incrementar, Count Down -
# Para restar y Reset - Para comenzar de cero).

from tkinter import *
import tkinter as tk

class Contador(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Contador")
        self.resizable(False, False)
        self.geometry("440x70")
        self.Widgets()

    def aumentar(self):
        self.entrada.config(state=tk.NORMAL)
        num = self.entrada.get()
        numlen = len(str(num))
        if numlen == 0:
            numN = 0
            numN += 1
            self.entrada.delete(0, END)
            self.entrada.insert(0, str(numN))
            self.entrada.config(state=tk.DISABLED)
        else:
            num = int(num)
            num += 1
            self.entrada.delete(0, END)
            self.entrada.insert(0, str(num))
            self.entrada.config(state=tk.DISABLED)
    
    def restar(self):
        self.entrada.config(state=tk.NORMAL)
        num = self.entrada.get()
        numlen = len(str(num))
        if numlen == 0:
            numN = 0
            numN -= 1
            self.entrada.delete(0, END)
            self.entrada.insert(0, str(numN))
            self.entrada.config(state=tk.DISABLED)
        else:
            num = int(num)
            num -= 1
            self.entrada.delete(0, END)
            self.entrada.insert(0, str(num))
            self.entrada.config(state=tk.DISABLED)

    def reset(self):
        self.entrada.config(state=tk.NORMAL)
        self.entrada.delete(0, END)
        self.entrada.insert(0, 0)
        self.entrada.config(state=tk.DISABLED)

    def Widgets(self):

        self.cont = Label(self, text="Contador:")
        self.cont.grid(column=0, row=0, sticky=tk.E, padx=10, pady=20)

        self.entrada = Entry(self,state=tk.DISABLED)
        self.entrada.grid(column=1, row=0, sticky=tk.W, padx=0, pady=20)

        self.mas = Button(self, text="Count Up",command=lambda: self.aumentar())
        self.mas.grid(column=2, row=0, sticky=tk.W, padx=5, pady=20)

        self.menos = Button(self, text="Count Down",command=lambda: self.restar())
        self.menos.grid(column=3, row=0, sticky=tk.W, padx=5, pady=20)

        self.borrar = Button(self, text="Reset",command=lambda: self.reset())
        self.borrar.grid(column=4, row=0, sticky=tk.W, padx=5, pady=20)

        

root = Contador()
root.mainloop()