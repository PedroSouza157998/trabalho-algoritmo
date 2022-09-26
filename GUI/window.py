from tkinter import *

window = Tk()

window.title('Algoritmo prim')

def print_contents():
    print('olá mundo',label.get())

title = Label(window, text="Algoritmo de Prim", padx=70, pady=10)
title.grid(column=0, row=0)

label=Entry(window)
label.grid(column=0, row=1)

button=Button(window, text="pesquisar", command=print_contents)
button.grid(column=0, row=2)


window.mainloop()