""""
from tkinter import *
import random

lista = ['milton']


def mezclar_jugadores():
    lista = [cuadro_nombre1.get(), cuadro_nombre2.get()]
    random.shuffle(lista)
    return var.set(lista)

raiz = Tk()
raiz.title("Login Lambda")
raiz.resizable(0,0)
raiz.config(bg="black")
mi_frame=Frame(raiz,width=300, height=130)
mi_frame.pack()
mi_frame.config(bg="red")

nombre_usuario1=Label(mi_frame, text="Nombre Usuario 1: ")
nombre_usuario1.grid(row=0, column=0, padx = 10, pady =10)

nombre_usuario2=Label(mi_frame, text="Nombre Usuario 2: ")
nombre_usuario2.grid(row=1, column=0, padx = 10, pady =10)

cuadro_nombre1=Entry(mi_frame)
cuadro_nombre1.grid(row=0,column=1,padx = 10, pady =10)

cuadro_nombre2=Entry(mi_frame)
cuadro_nombre2.grid(row=1,column=1,padx = 10, pady =10)
var = StringVar()

Dicc_show=Label(mi_frame, textvariable = var)
Dicc_show.grid(row=2, column=0, padx = 10, pady =10)
Dicc_show.config(bg = "red", fg = "white")

boton=Button(raiz,text="Enviar", command = mezclar_jugadores)
boton.pack()



def main():
    print(raiz.mainloop()) 

main()
"""

