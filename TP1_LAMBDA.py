"""
Objetivo
Construir un programa en etapas, que permita jugar al Memotest, teniendo en cuenta las reglas que se detallan en cada una de las etapas. 
"""
"""
Instrucciones Adaptadas del Juego a un único participante
● El Memotest se compone de fichas repetidas de a pares, que mezcladas se colocan sobre la mesa con la figura hacia abajo formando un cuadro.
● El participante comienza dando vuelta primero una ficha y luego otra tratando que sean iguales, si lo consigue toma las dos fichas para sí.
● Si las figuras son distintas las vuelve a dar vuelta en la misma posición que se encontraban y vuelve a elegir un nuevo par.
● El juego finaliza cuando no quedan más fichas por dar vuelta.
Es recomendable que juegues para que te familiarices con la operatoria, a continuación, encontrarás un enlace a un sitio que te permitirá jugar online.
https://cardsimages.info-tuparada.com/1143/20172-2-juego-memotest.html
"""
"""
Etapa 1- Versión reducida
En esta etapa el objetivo es programar una pequeña parte del juego. Vamos a simplificar y adaptar la programación de nuestro juego a los siguientes requerimientos:
● Las fichas por adivinar sólo serán 4, o sea 2 pares de fichas iguales. Por ejemplo: “D”, ”D”, “s”, “s”.
● El contenido de cada ficha será una letra, por ejemplo, las letras: D (mayúscula) y s (minúscula). Cada una de las cuales estará asociada a una posición en nuestro tablero de 4 fichas.
● Se le mostrará al jugador las posiciones disponibles, y se le solicitará el ingreso de una de ellas. Algo similar al siguiente ejemplo:
 Fichas y Posiciones: [1] [2] [3] [4]
 1er. Posición: _
En esta etapa, no debemos preocuparnos por validar el ingreso de los valores.
● A continuación, debemos mostrar que letra hay en la posición ingresada, y solicitar el ingreso de la siguiente posición en la que supone estará la letra
gemela. Por ejemplo si el jugador había ingresado como 1er. Posición, 2; entonces veríamos algo parecido a lo siguiente:
 Fichas y Posiciones: [1] D [3] [4]
 2da. Posición: _
 ● Si la segunda posición elegida contiene la letra gemela de la primer posición, entonces se mostrará al usuario la dos posiciones con sus respectivas letras, y se volverá a solicitar una primer posición:
 Fichas y Posiciones: [1] D [3] D
 1er. Posición: _
● En cambio, si la posición elegida como segunda posición, no contiene la letra gemela de la primera posición, se vuelve a mostrar el tablero con todas las posiciones disponibles:
 Fichas y Posiciones: [1] [2] [3] [4]
 1er. Posición: _
● Esta etapa del juego termina, cuando el usuario adivina todos los pares de posiciones con letras gemelas. 
"""
"""
Etapa 2 - Validación de ingresos
En esta etapa, sumaremos a los requerimientos de la etapa anterior, el de validar el ingreso de las posiciones. Si el participante ingresa:
● un valor que no corresponda a una posición
● o el mismo no se encuentre disponible,
● o no se trata de un valor numérico,
se le debe mostrar un mensaje acorde y solicitar el ingreso de un nuevo valor. 
"""
"""
Etapa 3 - Aumentando y generalizando la cantidad de fichas
En esta etapa debemos aumentar la cantidad de fichas intervinientes. Sumaremos a los requerimientos de la etapa anterior los siguientes:
● La cantidad de fichas intervinientes será ahora de 8 fichas, o sea 4 pares de fichas iguales.
● Debemos mostrar 4 fichas por línea.
● Además, debemos informar al terminar el juego, cuantos intentos tuvo que realizar el participante para terminar la partida.
"""
"""
Etapa 4 - Aleatoriedad y tiempos
Hasta aquí ya hemos logrado que nuestro juego se parezca bastante al real, por ello le daremos unos toques finales, sumando los siguientes requerimientos:
● Es hora de agregar aleatoriedad a las ubicaciones de las fichas. En cada ejecución del juego, debemos lograr que nuestras fichas sean asignadas a distintas posiciones.
● También, debemos informar el tiempo que ha tomado la partida.
● Por último, es hora de ampliar la cantidad de fichas a 16, mostrando 4 por línea
"""
"""
Etapa 5 - Extensión a Dos participantes
En el juego de mesa, los participantes pueden ser 2 ó más. Lo que cambia respecto de lo que hemos hecho, es lo siguiente:
● Comienza un participante dando vuelta primero una ficha y luego otra tratando que sean iguales,
si lo consigue toma las dos fichas para sí.
● Si las figuras son distintas las vuelve a dar vuelta en la misma posición que se encontraban y entonces 
dar lugar al otro participante a que haga lo mismo; y así sucesivamente.
● El juego finaliza cuando no quedan más fichas y se declara ganador al jugador con mayor cantidad de fichas iguales. 
En caso de empate, ganará el jugador que tuvo menor cantidad de intentos.
Entonces, en esta etapa debemos dar la posibilidad a que el juego sea entre dos participantes. Para ello, debemos:
● Solicitar los nombres de los dos jugadores al inicio de la partida. 
La solicitud de los nombres se debe hacer mediante una interfaz gráfica.
● Elegir de forma aleatoria, el jugador que jugará primero; y antes del comienzo del juego informar el orden.
 Cada vez que un jugador recibe su turno, se debe indicar claramente “Turno de: (Nombre del Jugador)”.
● Adaptar nuestra aplicación para que la lógica siga con esta nueva dinámica de juego. O sea, cuando un jugador no acierta 
la posición de la segunda ficha, le tocará el turno de elección de la posición de la primera ficha al siguiente jugador.
"""
"""
Condiciones de Entrega
Las siguientes condiciones deben ser respetadas para que la entrega sea considerada
válida:
1. El programa debe ser desarrollado en Python, aplicando correctamente los conceptos dados en clase y respetando las buenas prácticas descriptas en el PEP de la cátedra.
Cada función que forma parte del código debe tener debajo de su firma, una descripción corta de cuál es su objetivo y quien es el autor ó responsable de dicha función.
2. El código correspondiente a la Parte 1, debe ser subido al campus. El nombre a dar al archivo será TP1_NombreGrupo.py. Deberán reemplazar NombreGrupo, por el nombre dado a su grupo.
Si la entrega está compuesta por más de un archivo .py, generar un .zip con todos los archivos .py, y nombrarlo de igual modo, pero con extensión zip.
3. Deberán grabar 2 videos y subirlos a un canal de Youtube, ó a Google Drive. El primer video, cada integrante del equipo, deberá contar mostrando el código,
qué parte estuvo bajo su responsabilidad y los puntos de solución dados, que considere más relevantes. El video total no debe superar los 10 minutos.
Comenzar cada uno de los relatos, diciendo el nombre y apellido del quien relata. La calidad del video debe ser buena, y debe haber homogeneidad en las presentaciones.
4. Deberán grabar un segundo video, en el que se muestre al menos una jugada completa, y que contemple distintos casos que muestran que la aplicación responde según lo esperado.
Deberán ir relatando los eventos de la jugada. En este caso el video puede estar realizado por 1 único integrante. 
"""
        
# en el caso de que las "cartas" con las que jugar esten predefinidas con 2 pares (etapa 1)
"""lista_cartas=["A","B","A","B"]"""

# en el caso de que las "cartas" con las que jugar esten predefinidas con 4 pares (etapa 4)
"""lista_cartas=["A","A","B","B","C","C","D","D"]"""

import random
from time import time
import os

#lista_cartas = ["a","a","b","b","c","c","d","d","e","e","f","f","g","g","h","h"]
#LISTA_VACIA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#lista_juego = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

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
    Imprimo el tablero.
    Creada por: JuanP
    '''
    #me ahorro todo esto -> print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])
    return

def participantes():
    '''
    Creada por: Juan Pedro.
    Esta funcion se encarga de tomar la cantidad de personas que quieran jugar al MEMOTEST.Si el juego es de a mas de 2,
    descomentar las funciones comentadas, vaciar lista_participantes y comentar los nombres de cada jugador.
    '''
    #jugadores = int(input("Cuantos participantes desean jugar:? "))
    jugador1 = input("Nombre del primer jugador: ")
    jugador2 = input("Nombre del segundo jugador: ")

    lista_participantes = [jugador1,jugador2]
    diccionario = {}
    #for i in range(jugadores):
    #    jugador= input("Nombre del jugador: ")
    #    lista_participantes.append(jugador)
    lista_participantes = mezclar(lista_participantes)
    for jugador in lista_participantes:
        diccionario[jugador] = [0,0] #[cantidad de fichas iguales, cantidad de intentos]
    return diccionario,lista_participantes
    

def juego(lista_juego, lista_cartas, LISTA_VACIA, cartas):
    '''
    juego base
    Creada por: ...
    '''

    #lista_cartas= mezclar(lista_cartas)
    jugadores = participantes() #jugadores va a ser una tupla, el primer elemento es un diccionario, el segundo una lista con los nombres de los participantes.
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
            lista_cartas.remove(lista_juego[primera_posicion-1])#Las elimino de mi lista_cartas
            lista_cartas.remove(lista_juego[segunda_posicion-1])
            diccionario[lista_participantes[jugador]][0] +=1 #le sumo un punto
            

        while i < len(lista_juego): #por cada letra q aparezca, la elimino de la lista.
            if lista_juego[i] in cartas:
                lista_juego.pop(i)
            else: i+=1

        #os.system("cls")
        diccionario[lista_participantes[jugador]][1] +=1 #le sumo los intentos totales de cada uno
        contador_jugadas_totales += 1
    return diccionario 

def winner(resultados):
    '''
    Creada por: Juan Pedro.
    Esta funcion se encarga de calcular en base al puntaje quien fue el ganador en base a los puntos obtenidos o ,en caso de empate,
    muestra el ganador por la menor cantidad de intentos realizados.
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
        lista_cartas = ["A","A","B","B","C","C","D","D"]
        #lista_cartas = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H"]
        cartas = ['A','B','C','D','E','F','G','H']
        LISTA_VACIA = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]']
        #LISTA_VACIA = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]','[10]','[11]','[12]','[13]','[14]','[15]','[16]']
        lista_juego = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]']
        #lista_juego = ['[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]','[10]','[11]','[12]','[13]','[14]','[15]','[16]']
        resultados = juego(lista_juego, lista_cartas, LISTA_VACIA, cartas)
        winner(resultados)
        seguir= input("¿Seguir jugando?(s/n): ")

inicio = time()
main()
tiempo_partida = time() - inicio
print(f"El tiempo de la partida fue de {round(tiempo_partida)} segundos.")