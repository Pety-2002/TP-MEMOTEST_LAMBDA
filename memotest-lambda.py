    
# en el caso de que las "cartas" con las que jugar esten predefinidas con 2 pares (etapa 1)
"""lista_cartas=["A","B","A","B"]"""

# en el caso de que las "cartas" con las que jugar esten predefinidas con 4 pares (etapa 4)
"""lista_cartas=["A","A","B","B","C","C","D","D"]"""



lista_cartas = ["a","a","b","b","c","c","d","d","e","e","f","f","g","g","h","h"]
LISTA_VACIA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
lista_juego = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#para mezclar las "cartas" y se encuentren en diferentes posiciones en c/partida (se mantienen los caracteres) (etapa 4)
def mezclar_cartas (lista_original):
    lista_mezclada = lista_original
    import random
    random.shuffle(lista_mezclada)
    return lista_mezclada

#para filtrar los valores que deben ingresar en el juego (etapa 2) (me da error en el filatrado de numeros "numero.isnumeric")
def validar_ingreso(numero):
    if numero.isdigit():
        if 0<int(numero)<len(lista_cartas)+1:
            devolver=True
        else:
            devolver=False
    else:
        devolver=False
    return devolver

#juego base
def juego(lista_juego, lista_cartas):
    
    lista_cartas= mezclar_cartas(lista_cartas)
    contador_intentos=0
        
    while lista_juego != lista_cartas:
        #comienzo del juego
        print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
        primera_posicion= input("Seleccione una posición: ")
        while validar_ingreso(primera_posicion) == False:
            print("Seleccione un numero del 1 al",len(lista_cartas))
            primera_posicion= input("Seleccione una posición: ")
        primera_posicion = int(primera_posicion)
        lista_juego[primera_posicion-1] = lista_cartas[primera_posicion-1]
        print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
        #1er opcion
        
        segunda_posicion= input("Seleccione una segunda posición: ")
        while validar_ingreso(segunda_posicion) == False:
            print("Seleccione un numero del 1 al",len(lista_cartas))
            segunda_posicion= input("Seleccione una posición: ")
        segunda_posicion = int(segunda_posicion)
        lista_juego[segunda_posicion-1] = lista_cartas[segunda_posicion-1]
        print(lista_juego[:4], "\n", lista_juego[4:8], "\n", lista_juego[8:12], "\n", lista_juego[12:16], sep = "")
        #2da opcion
        
        if lista_juego[primera_posicion-1] != lista_juego[segunda_posicion-1]:
            lista_juego[primera_posicion-1] = LISTA_VACIA[primera_posicion-1]
            lista_juego[segunda_posicion-1] = LISTA_VACIA[segunda_posicion-1]
        #condicion de que ambas opciones sean iguales
        
        contador_intentos+=1
        #para contar la cantidad de intentos requeridos (etapa 3)
    return contador_intentos

def main():
    seguir = "s"
    while seguir == "s":
        print("usted gano en",juego(lista_juego, lista_cartas),"intentos")
        seguir= input("¿Seguir jugando?(s/n): ")

main()
