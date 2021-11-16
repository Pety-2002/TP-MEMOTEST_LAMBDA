import random
from tkinter import *
import time
import os


cartas = ['A','B','C','D','E','F','G','H']
LISTA_VACIA = [[1],[2],[3],[4]]
#lista_cartas = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H"]
#LISTA_VACIA = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16]]
#lista_juego = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16]]

''' Para mezclar las "cartas" y se encuentren en diferentes posiciones en c/partida (se mantienen los caracteres) (etapa 4)
    Creada por: ...'''

def mezclar(lista):
    lista_mezclada = lista
    random.shuffle(lista_mezclada)
    return lista_mezclada


''' Validar que el ingreso no sea una valor fuera de rango/no se encuentre disponible/no sea un numero
    Creada por: Facundo Polech'''
def validar_ingreso(numero,lista_cartas,lista_juego):
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas) or lista_juego[int(numero)-1] == '[*]':
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada en el tablero: ")
    return int(numero)


''' Imprimo el tablero.
    Creada por: JuanP'''

def imprimir_tablero(lista_juego):
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])
    return


""" Crea la interfaz para solicitar el nombre de los jugadores
    Creada por: Milton Fernandez
    NOTA: HACER QUE SE CREEN BLOQUES DE INGRESO DE NOMBRE POR CADA PARTICIPANTE"""

def nombres_jugadores():
    raiz = Tk()
    lista = []
    raiz.title("Ingreso Usuarios")
    raiz.config(bg="red")
    raiz.geometry('300x200')
    mi_frame=Frame(raiz)
    mi_frame.pack()
    mi_frame.config(bg="red")

    #----------------------- Labels ---------------------#
    nombre_usuario1=Label(mi_frame, text="Nombre Usuario 1: ")
    nombre_usuario1.grid(row=0, column=0, padx = 10, pady =10)

    nombre_usuario2=Label(mi_frame, text="Nombre Usuario 2: ")
    nombre_usuario2.grid(row=1, column=0, padx = 10, pady =10)

    #---------------- Entradas de texto -----------------#
    cuadro_nombre1=Entry(mi_frame)
    cuadro_nombre1.grid(row=0,column=1,padx = 10, pady =10)

    cuadro_nombre2=Entry(mi_frame)
    cuadro_nombre2.grid(row=1,column=1,padx = 10, pady =10)

    #Verifica que se ingresaron ambos nombres
    def obtener_nombres():
        if cuadro_nombre1.get() != '' and cuadro_nombre2.get() != '':
            lista.append(cuadro_nombre1.get()), lista.append(cuadro_nombre2.get())
            raiz.destroy()
        
        else: 
            usuarios=Label(mi_frame, text="Por favor \n ingrese ambos usuarios")
            usuarios.grid(row=2, column=0, padx = 10, pady =10)

    #------------------- Botón enviar ------------------#
    boton_enviar=Button(raiz,text="Enviar", command = lambda: [obtener_nombres()])
    boton_enviar.pack()

    raiz.mainloop()
    return lista


''' Crea el diccionario donde se registraran los datos de cada jugador
    Creada por: Juan Pedro Demarco'''

def datos_jugadores(lista_nombres_ingresados):
    diccionario = {}
    lista_nombres_ingresados = mezclar(lista_nombres_ingresados)
    for jugador in lista_nombres_ingresados:
        diccionario[jugador] = [0,0]

    return  diccionario
   

''' Determina si las cartas ingresadas son iguales o no, en caso positivo acredita un punto al jugador
    Creada por: todos los integrantes.'''

def voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, datos_jugadores):
    CANT_PUNTOS=0
    CANT_INTENTOS=1 

    lista_cartas= mezclar(lista_cartas)
    jugadores = datos_jugadores
    diccionario = jugadores[0]
    lista_participantes = jugadores[1]
    
    jugador = 0
    contador_jugadas_totales=0

    while lista_juego != lista_cartas:
        print(f"Turno de :{lista_participantes[jugador]}")
        imprimir_tablero(lista_juego)
        primera_posicion = input("Seleccione una posición: ")  
        primera_posicion = validar_ingreso(primera_posicion,lista_cartas,lista_juego)
        lista_juego[primera_posicion-1] = lista_cartas[primera_posicion-1]
        imprimir_tablero(lista_juego)
                
        segunda_posicion= input("Seleccione una segunda posición: ")
        segunda_posicion = validar_ingreso(segunda_posicion,lista_cartas,lista_juego)
        lista_juego[segunda_posicion-1] = lista_cartas[segunda_posicion-1]
        imprimir_tablero(lista_juego)
            
        #Si las fichas son distintas:
        if lista_juego[primera_posicion-1] != lista_juego[segunda_posicion-1]:
            lista_juego[primera_posicion-1] = LISTA_VACIA[primera_posicion-1]
            lista_juego[segunda_posicion-1] = LISTA_VACIA[segunda_posicion-1]
            print("Los cartas seleccionadas son distintas")

            if jugador == len(jugadores)-1: # Esta funcion es necesaria para que pueda repetir un jugador.
                jugador = 0
            else:
                jugador +=1

            #Si las fichas son iguales:
        elif lista_juego[primera_posicion-1] == lista_juego[segunda_posicion-1]:
            diccionario[lista_participantes[jugador]][CANT_PUNTOS] +=1
            lista_juego[primera_posicion-1] = '[*]'
            lista_juego[segunda_posicion-1] = '[*]'
            lista_cartas[primera_posicion-1] = '[*]'
            lista_cartas[segunda_posicion-1] = '[*]'

        time.sleep(2.5)
        os.system("cls")
        diccionario[lista_participantes[jugador]][CANT_INTENTOS] +=1 
        contador_jugadas_totales += 1
    return diccionario 


''' En calcula quien fue el ganador en base a los puntos obtenidos o ,en caso de empate, por la menor cantidad de intentos realizados.
    Creada por: Juan Pedro.'''

def ganador(resultados):
    NOMBRE=PUNTOS=0
    TUPLA_DATOS=INTENTOS=1

    resultados = [(participante,puntos) for participante,puntos in resultados.items()]
    resultados.sort(key = lambda elemento: elemento[TUPLA_DATOS][PUNTOS] ,reverse = True)
    numero_max = resultados[0][TUPLA_DATOS][PUNTOS] 
    contador = 0
    for player in resultados:
        if numero_max == player[TUPLA_DATOS][PUNTOS]:
            contador +=1
    if contador>1:
        resultados.sort(key = lambda tupla: tupla[TUPLA_DATOS][INTENTOS])
        print(f"El ganador de la partida es {resultados[0][NOMBRE]}, por caso de empate y con una menor cantidad de intentos de valor:{resultados[0][TUPLA_DATOS][INTENTOS]}.")
    else:
        print(f"El ganador de la partida es {resultados[0][NOMBRE]}, con {numero_max} puntos totales.")
    return 


'''Creada por: ...'''

def main():
    seguir = "s"
    lista = nombres_jugadores()
    diccionario = datos_jugadores(lista)
    while seguir == "s":

        lista_juego = [[1],[2],[3],[4]]
        lista_cartas = ["A","A","B","B"]
        resultados = voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, (diccionario,lista))
        ganador(resultados)
        seguir= input("¿Seguir jugando?(s/n): ")
    return  

#------------------------------------- Comienzo del juego -------------------------------------------#
tiempo_inicial = time.time()
main()
tiempo_partida = time.time() - tiempo_inicial

print(f"El tiempo de la partida fue de {round(tiempo_partida)} segundos.")