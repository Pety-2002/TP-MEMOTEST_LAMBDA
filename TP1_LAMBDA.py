import random
from time import time
import os
from tkinter import *

lista_cartas = ["A","A","B","B","C","C","D","D"]
cartas = ['A','B','C','D','E','F','G','H']
LISTA_VACIA = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]']
lista_juego = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]']
#lista_cartas = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H"]
#LISTA_VACIA = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]','[10]','[11]','[12]','[13]','[14]','[15]','[16]']
#lista_juego = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]','[10]','[11]','[12]','[13]','[14]','[15]','[16]']

CANT_FICHAS_IGUALES=0
CANT_INTENTOS=1

def mezclar(lista):
    '''
    para mezclar las "cartas" y se encuentren en diferentes posiciones en c/partida (se mantienen los caracteres) (etapa 4)
    Creada por: ...
    '''
    lista_mezclada = lista
    random.shuffle(lista_mezclada)
    return lista_mezclada

def validar_ingreso(numero,lista_cartas):
    '''
    Validar que el ingreso no sea una valor fuera de rango/no se encuentre disponible/no sea un numero
    Creada por: Facundo Polech
    '''
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas):
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada en el tablero: ")
    return int(numero)

def imprimir_tablero(lista_juego):
    '''
    Imprimo el tablero.
    Creada por: JuanP
    '''
    #me ahorro todo esto -> print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])
    return

def nombres_jugadores():
    """
    Crea la interfaz para solicitar el nombre de los jugadores
    Creada por: Milton Fernandez
    NOTA: HACER QUE SE CREEN BLOQUES DE INGRESO DE NOMBRE POR CADA PARTICIPANTE
    """
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

    boton=Button(raiz,text="Enviar", command =lambda: datos_jugadores([cuadro_nombre1.get(), cuadro_nombre2.get()]))
    boton.pack()

    raiz.mainloop()

def datos_jugadores(lista_nombres_ingresados):
    '''
    Crea el diccionario donde se registraran los datos de cada jugador
    Creada por: Juan Pedro Demarco
    '''
    #jugadores = int(input("Cuantos participantes desean jugar:? "))
    diccionario = {}
    #for i in range(jugadores):
    #    jugador= input("Nombre del jugador: ")
    #    lista_participantes.append(jugador)
    lista_nombres_ingresados = mezclar(lista_nombres_ingresados)
    for jugador in lista_nombres_ingresados:
        diccionario[jugador] = [0,0] #[cantidad de fichas iguales, cantidad de intentos]
    
    resultados = voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, cartas,(diccionario,lista_nombres_ingresados))
    ganador(resultados)
    
    

def voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, cartas,tupla):
    '''
    Determina si las cartas ingresadas son iguales o no, en caso positivo acredita un punto al jugador
    Creada por: Juan Pedro Demarco
    '''

    lista_cartas= mezclar(lista_cartas)
    jugadores = tupla#jugadores va a ser una tupla, el primer elemento es un diccionario, el segundo una lista con los nombres de los participantes.
    diccionario = jugadores[0]
    lista_participantes = jugadores[1]
    jugador = 0
    contador_jugadas_totales=0

    while lista_juego != lista_cartas:
        #comienzo del juego
        i = 0 #index de la lista, lo utilizo para eliminar elementos cuando el jugador acierta el par.
        print(f"Turno de :{lista_participantes[jugador]}")
        imprimir_tablero(lista_juego)
        primera_posicion= input("Seleccione una posición: ")  
        primera_posicion = validar_ingreso(primera_posicion,lista_cartas)
        lista_juego[primera_posicion-1] = lista_cartas[primera_posicion-1]
        imprimir_tablero(lista_juego)
                
        segunda_posicion= input("Seleccione una segunda posición: ")
        segunda_posicion = validar_ingreso(segunda_posicion,lista_cartas)
        lista_juego[segunda_posicion-1] = lista_cartas[segunda_posicion-1]
        imprimir_tablero(lista_juego)
            
        #Si las fichas son distintas:
        if lista_juego[primera_posicion-1] != lista_juego[segunda_posicion-1]:
            lista_juego[primera_posicion-1] = LISTA_VACIA[primera_posicion-1]
            lista_juego[segunda_posicion-1] = LISTA_VACIA[segunda_posicion-1]

            if jugador == len(jugadores)-1: # Esta funcion es necesaria para que pueda repetir un jugador.
                jugador = 0
            else:
                jugador +=1

            #Si las fichas son iguales:
        elif lista_juego[primera_posicion-1] == lista_juego[segunda_posicion-1]:
            diccionario[lista_participantes[jugador]][0] +=1 #le sumo un punto

        os.system("cls")
        diccionario[lista_participantes[jugador]][1] +=1 #le sumo los intentos totales de cada uno
        contador_jugadas_totales += 1
    return diccionario 

def ganador(resultados):
    '''
    En calcula quien fue el ganador en base a los puntos obtenidos o ,en caso de empate, por la menor cantidad de intentos realizados.
    Creada por: Juan Pedro.
    '''
    resultados = [(participante,puntos) for participante,puntos in resultados.items()] #hago una lista en base a los items del diccionario
    resultados.sort(key = lambda tupla: tupla[1][0] ,reverse = True) #se ordenan todos los resultados,mayor a menor
    numero_max = resultados[0][1][0] #numero_max es el primer elemento, del segundo elemento(lista), de mi primer tupla.
    contador = 0
    for player in resultados:
        if numero_max == player[1][0]:#agarro cada primer elemento de la lista de cada tupla.
            contador +=1
    if contador>1:
        resultados.sort(key = lambda tupla: tupla[1][1])#se ordenan todos los resultados en base a la cantidad de intentos.
        print(f"El ganador de la partida es {resultados[0][0]}, por caso de empate y con una menor cantidad de intentos de valor:{resultados[0][1][1]}.")
    else:
        print(f"El ganador de la partida es {resultados[0][0]}, con {numero_max} puntos totales.")

def main():
    '''Creada por: ...'''
    seguir = "s"
    while seguir == "s":
        nombres_jugadores()
        seguir= input("¿Seguir jugando?(s/n): ")

inicio = time()
main()
tiempo_partida = time() - inicio
print(f"El tiempo de la partida fue de {round(tiempo_partida)} segundos.")