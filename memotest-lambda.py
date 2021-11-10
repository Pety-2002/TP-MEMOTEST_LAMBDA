import random
from tkinter import *
import time
import os

lista_cartas = ["a","a","b","b","c","c","d","d","e","e","f","f","g","g","h","h"]
LISTA_VACIA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
lista_juego = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def mezclar_cartas(lista_original):
    '''
    para mezclar las "cartas" y se encuentren en diferentes posiciones en c/partida (se mantienen los caracteres) (etapa 4)
    Creada por: ...
    '''
    lista_mezclada = lista_original
    random.shuffle(lista_mezclada)
    return lista_mezclada

def validar_ingreso(numero):
    '''
    Filtrar los valores que deben ingresar en el juego (etapa 2).
    Si el participante ingresa:
    ● un valor que no corresponda a una posición
    ● o el mismo no se encuentre disponible,
    ● o no se trata de un valor numérico,
    se le debe mostrar un mensaje acorde y solicitar el ingreso de un nuevo valor. 
    Creada por: (algun otro), JuanP
    '''
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas):
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada en el tablero: ")
    return int(numero)

def imprimir_tablero(lista_juego):
    '''
    Imprimo el tablero
    Creada por: JuanP
    '''
    #me ahorro todo esto -> print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])
    return

def mezclar_jugadores():
    lista = [cuadro_nombre1.get(), cuadro_nombre2.get()]
    random.shuffle(lista)
    return var.set(f"Es el turno de {lista[0]}")


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

raiz.mainloop()


    
def juego(lista_juego, lista_cartas):
    '''
    juego base
    Creada por: ...
    '''
    lista_cartas= mezclar_cartas(lista_cartas)
    contador_intentos=0
    tiempo_inicial = time.time()

    while lista_juego != lista_cartas:

        #comienzo del juego
        imprimir_tablero(lista_juego)
        primera_posicion= input("Seleccione una posición: ")  
        primera_posicion = validar_ingreso(primera_posicion)
        lista_juego[primera_posicion-1] = lista_cartas[primera_posicion-1]
        imprimir_tablero(lista_juego)
        
        segunda_posicion= input("Seleccione una segunda posición: ")
        segunda_posicion = validar_ingreso(segunda_posicion)
        lista_juego[segunda_posicion-1] = lista_cartas[segunda_posicion-1]
        imprimir_tablero(lista_juego)
        
        #Si las fichas son distintas:
        if lista_juego[primera_posicion-1] != lista_juego[segunda_posicion-1]:
            lista_juego[primera_posicion-1] = LISTA_VACIA[primera_posicion-1]
            lista_juego[segunda_posicion-1] = LISTA_VACIA[segunda_posicion-1]
        
        #borra resultados anteriores
        time.sleep(5)
        os.system("cls")
        
        print("")
        contador_intentos+=1
        
    tiempo_final = time.time()
    tiempo_transcurrido = int(tiempo_final - tiempo_inicial)

    # resultados[intentos, tiempo]
    resultados = [contador_intentos, tiempo_transcurrido]

    #para contar la cantidad de intentos requeridos (etapa 3)
    return resultados

def main():
    '''Creada por: ...'''
    seguir = "s"
    while seguir == "s":
        resultados = juego(lista_juego, lista_cartas)
        print(f"Usted gano en {resultados[0]} intentos y {resultados[1]} segundos") #usar f print
        seguir= input("¿Seguir jugando?(s/n): ")

main()