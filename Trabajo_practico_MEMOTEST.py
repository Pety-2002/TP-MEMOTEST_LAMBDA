import random
from tkinter import *
from time import time
import os

lista_cartas = ["a","a","b","b","c","c","d","d"]
LISTA_VACIA = [1, 2, 3, 4, 5, 6, 7, 8]
lista_juego = [1, 2, 3, 4, 5, 6, 7, 8]

def mezclar_cartas(lista_original):
    '''
    Cambia posicion de valores por partidas (etapa 4)
    Creada por: ...
    '''
    lista_mezclada = lista_original
    random.shuffle(lista_mezclada)
    return lista_mezclada

def validar_ingreso(numero):
    '''
    Filtrar los valores que deben ingresar en el juego (etapa 2).
    Creada por: JuanP
    '''
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas):
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada en el tablero: ")
    return int(numero)

def imprimir_tablero(lista_juego):
    '''
    Imprime el tablero
    Creada por: JuanP
    '''
    #me ahorro todo esto -> print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])
    return
    
def juego(lista_juego, lista_cartas):
    '''
    Ingreso de las posiciones y verificar que los valores sean iguales

    Creada por: ...
    '''
    #lista_cartas= mezclar_cartas(lista_cartas)
    contador_intentos=0
    fichas_distintas=False

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
        
    if lista_juego[primera_posicion-1] != lista_juego[segunda_posicion-1]:
        
        lista_juego[primera_posicion-1] = LISTA_VACIA[primera_posicion-1]
        lista_juego[segunda_posicion-1] = LISTA_VACIA[segunda_posicion-1]
        fichas_distintas=True
        contador_intentos+=1

    os.system("cls")
        
    resultados = [contador_intentos, fichas_distintas]
    return resultados

def cambio_jugador(jugador1, jugador2):
    #Esta funcion cambia el turno del jugador-Yenny/Eva Agregar al final el random
    turno_jugador_1=True
    INTENTOS=0
    FICHAS_DIF=1
    ganador = 0
    contador_puntos1 = 0
    contador_puntos2 = 0
    resultados_jugador_1=[0,0,0]
    resultados_jugador_2=[0,0,0]


    while lista_cartas!=lista_juego:
        flag=True
        

        while turno_jugador_1 and flag:
            contador_puntos1 += 1
            print("Turno de ", jugador1)
            resultados_jugador_1=juego(lista_juego, lista_cartas)
            if resultados_jugador_1[FICHAS_DIF]==True:
                turno_jugador_1=False  
                contador_puntos1 -= 1
            if lista_cartas==lista_juego:
                flag=False 
        
        while turno_jugador_1==False and flag:
            contador_puntos2 += 1
            print("Turno de ", jugador2)
            resultados_jugador_2=juego(lista_juego, lista_cartas)
            if resultados_jugador_2[2]==True:
                turno_jugador_1=True
            if lista_cartas==lista_juego:
                flag=False    

    if contador_puntos1 > contador_puntos2:
        ganador=(f"El ganador fue {jugador1}, con {contador_puntos1} puntos ")

    elif contador_puntos1 < contador_puntos2:
        ganador=(f"El ganador fue {jugador2}, con {contador_puntos2} puntos ")
    
    elif contador_puntos1 == contador_puntos2:
        if resultados_jugador_1[INTENTOS] < resultados_jugador_2[INTENTOS]:
            ganador = (f"El ganador fue {jugador1}, con {resultados_jugador_1[INTENTOS]} intentos, dado que los puntos fueron equivalentes")

        else: ganador = (f"El ganador fue {jugador2}, con {resultados_jugador_2[INTENTOS]} intentos, dado que los puntos fueron equivalentes")

    return ganador

def main():
    seguir = "s"
    while seguir == "s":
        nombre_jugador_1=input("Ingrese su nombre ")
        nombre_jugador_2=input("Ingrese su nombre ")
        resultados = cambio_jugador(nombre_jugador_1, nombre_jugador_2)
        print(resultados) 
        seguir= input("¿Seguir jugando?(s/n): ")

inicio = time()
main()
tiempo_partida = time() - inicio
print("El tiempo de la partida fue de", round(tiempo_partida), "segundos")