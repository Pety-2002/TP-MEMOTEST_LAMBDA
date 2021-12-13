from hoja_validaciones import * 
from hoja_interfaces import *
import random
from tkinter import *
import time
import os
import datetime


def mezclar(lista):
    '''
    Para mezclar las cartas y/o orden de los jugadores para que se encuentren en diferentes posiciones en c/partida.
    Creada por: Facundo Polech
    '''
    lista_mezclada = lista
    random.shuffle(lista_mezclada)
    return lista_mezclada

def agregar_linea(linea):
    """
    Agrega el nombre y contraseña del usuario al archivo
    Creada Por: Yennyfer Garcia
    """
    archivo = open ("registro_usuarios.csv","r+")
    archivo.write(linea + "\n")
    archivo.close()

def imprimir_tablero(lista_juego):
    '''
    Imprimo el tablero. Creo slices de 4 para imprimir por linea 4 fichas.
    Creada por: Juan Pedro Demarco
    '''
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])

def registro(num_partidas):
    """
    Crea la interfaz de registro de los usuarios
    Creada Por: Yennyfer Garcia
    """

    raiz = Tk()
    raiz.title("Registro Usuarios")
    raiz.config(bg="#D5D8DC")
    raiz.geometry('350x250')
    mi_frame=Frame(raiz)
    mi_frame.pack()
    mi_frame.config(bg="#D5D8DC")
    
    #---------- Labels ------------------

    nombre_usuario=Label(mi_frame, text="Nombre Usuario",bg="#D5D8DC")
    nombre_usuario.grid(row=1, column=0, padx = 10, pady =10)

    contraseña_usuario1=Label(mi_frame, text="Contraseña",bg="#D5D8DC")
    contraseña_usuario1.grid(row=2, column=0, padx = 10, pady =10)
    
    contraseña_usuario2=Label(mi_frame, text="Repetir Contraseña",bg="#D5D8DC")
    contraseña_usuario2.grid(row=3, column=0, padx = 10, pady =10)

    #---------- Entry-------------------------
    
    cuadro_nombre=Entry(mi_frame, border="3")
    cuadro_nombre.grid(row=1,column=1,padx = 10, pady =10)

    cuadro_contraseña=Entry(mi_frame ,border="3")
    cuadro_contraseña.grid(row=2,column=1,padx = 10, pady =10)
    cuadro_contraseña.config(show="*")


    contraseña_repetida=Entry(mi_frame,  border="3")
    contraseña_repetida.grid(row=3,column=1,padx = 10, pady =10)
    contraseña_repetida.config(show="*")


    mensaje=StringVar()
    mensaje_validacion=Label(mi_frame,textvariable=mensaje)
    mensaje_validacion.grid(row=4,column=0, columnspan=2 ,padx = 10, pady =10)
    mensaje_validacion.config(bg="#D5D8DC",fg="red")

    
    def guardar_usuarios(nombre, contraseña, contraseña_repetida):
        """
        Agrega a los usuarios al archivo
        Creada Por: Yennyfer Garcia
        """
        nombre_valido=validar_nombre_usuario(nombre)
        contraseña_valida=validar_contraseña_usuario(contraseña)

        if contraseña_valida and nombre_valido and contraseña == contraseña_repetida:
            
            usuario_existe=validar_registracion(nombre, contraseña)
            
            if usuario_existe[0]:
                mensaje.set("Usted ya se encuentra registrado")
            else:
                linea=(f"{nombre},{contraseña}")
                agregar_linea(linea)
                mensaje.set("Se ha registrado exitosamente")

        elif contraseña_valida==False:
            mensaje.set("La contraseña debe contener: Entre 8 y 12 caracteres,\n una letra mayuscula, una letra minuscula (sin acentos)\ny tener un guion (bajo o medio)")

        elif nombre_valido == False:
            mensaje.set("El nombre de usuario debe contener: Entre 4 y 15 caracteres,\n estar formado sólo por letras, números y el bajo guion.")

        elif contraseña != contraseña_repetida:
            mensaje.set("Las contraseñas son distintas")
    def inicio(num_partidas):
        raiz.destroy()
        main(num_partidas)
                
    #----------Botones---------------------------

    boton_crear_ususario=Button(mi_frame,text="Crear Usuario",command = lambda: guardar_usuarios(cuadro_nombre.get(), cuadro_contraseña.get(), contraseña_repetida.get()) ,bg="#24CA1C", fg="white",width="15", border=3)
    boton_crear_ususario.grid(row=5,column=0,padx = 10, pady =10)
    
    boton_volver_inicio=Button(mi_frame,text="Volver inicio",command = lambda: inicio(num_partidas),bg="#24CA1C", fg="white",width="15", border=3)
    boton_volver_inicio.grid(row=5,column=1,padx = 10, pady =10)

    raiz.mainloop()


def nombres_jugadores(num_partidas):
    """
    CREA LA INTERFAZ para solicitar el nombre de los jugadores 
    Creada por: Milton Fernandez, Yennyfer Garcia, Juan Pedro Demarco.
    """
    raiz = Tk()
    lista = [] #guarda los nombres de los jugadores.
    raiz.title("Ingreso Usuarios")
    raiz.config(bg="#D5D8DC")
    raiz.geometry('460x250')
    mi_frame=Frame(raiz)
    mi_frame.pack()
    mi_frame.config(bg="#D5D8DC")

    #----------------------- Labels ---------------------#
    raiz.contador = 1 #variable is stored in the root object

    users_label = StringVar()
    users_label.set(f'Nombre usuario {raiz.contador}:')

    contra_label = StringVar()
    contra_label.set(f'Contraseña usuario {raiz.contador}:')   

    nombre_usuario=Label(mi_frame, textvariable = users_label,bg="#D5D8DC")
    nombre_usuario.grid(row=1, column=0, padx = 10, pady =10)

    contraseña_usuario=Label(mi_frame, textvariable = contra_label,bg="#D5D8DC")
    contraseña_usuario.grid(row=2, column=0, padx = 10, pady =10)

    mensaje_derecha = StringVar() #mensaje que aparece a la derecha
    mensaje_derecha_label=Label(mi_frame, textvariable= mensaje_derecha)
    mensaje_derecha_label.grid(row=0, column=2,rowspan= 3,padx = 10, pady =10)
    mensaje_derecha_label.config(bg="#D5D8DC",fg="red")

    mensaje_principio=StringVar() #mensaje que aparece abajo
    mensaje_principio.set("Para empezar a jugar, se necesita agregar al menos 1 jugador!")
    mensaje_validacion=Label(mi_frame,textvariable=mensaje_principio)
    mensaje_validacion.grid(row=7,column=0, columnspan=3 ,padx = 10, pady =10)
    mensaje_validacion.config(bg="#D5D8DC",fg="red")
    mensaje_validacion.after(4000, lambda: jugadores1())

    jugadores=StringVar() #lista de jugadores
    lista_jugadores=Label(mi_frame,textvariable=jugadores)
    lista_jugadores.grid(row=8,column=0, columnspan=3 ,padx = 10, pady =10)
    lista_jugadores.config(bg="#D5D8DC",fg="blue")
    #---------------- Entradas de texto -----------------#

    cuadro_nombre=Entry(mi_frame, border="3")
    cuadro_nombre.grid(row=1,column=1,padx = 10, pady =10)

    cuadro_contraseña=Entry(mi_frame ,border="3")
    cuadro_contraseña.grid(row=2,column=1,padx = 10, pady =10)
    cuadro_contraseña.config(show="*")

    def jugadores1():
        '''
        Cambia el mensaje de inicio.
        Creada por: Juan Pedro Demarco.
        '''
        mensaje_principio.set("Jugadores:")
        mensaje_validacion.config(bg="#D5D8DC",fg="blue")

    def obtener_nombres(jugadores):
        '''
        Guarda el nombre del jugador en una lista, luego de conocer que ya esta registrado. En caso contrario, avisa al participante que
        se registre primero.
        Creada por: Julieta Margenats, Juan Pedro Demarco.
        '''
        username=cuadro_nombre.get()
        password = cuadro_contraseña.get()

        usuario_existe = validar_registracion(username, password)

        if usuario_existe[0]:#usuario y contraseña existen
            lista.append(username) #Los usuarios que se encuentran registrados se van sumando a la lista de jugadores.
            jugadores.set(lista)
            maximo_jugadores = validar_maximo_jugadores(len(lista))#verificacion el maximo de jugadores

            if maximo_jugadores:
                raiz.contador +=1
                mensaje_derecha.set('Puede seguir \n ingresando usuarios')
            
            else: #Se destruye despues de 4 segundos si llega al maximo
                mensaje_derecha.set('MAXIMO de jugadores \nalcanzado.El juego \ncomenzara en breve!')
                turnos(lista,jugadores)

        elif usuario_existe[1]: #usuario existe pero la contraseña no es correcta
            mensaje_derecha.set('El usuario existe pero \n la contraseña no es correcta')

        else:
            mensaje_derecha.set('El usuario no esta registrado.\nPor favor, registrese primero.')

    def agregar_jugador():
        '''
        Funcion que se llama cada vez que queremos agregar un jugador. Actualiza la interfaz en el proceso. Se verifica que el jugador 
        este registrado anteriormente.
        Creada por: Juan Pedro Demarco.
        '''
        obtener_nombres(jugadores)
        users_label.set(f'Nombre usuario {raiz.contador}:')
        contra_label.set(f'Contraseña usuario {raiz.contador}:')
        cuadro_nombre.delete(0, END)
        cuadro_contraseña.delete(0, END)
        boton_enviar["state"] = NORMAL

    def interfaz_registro(num_partidas):
        '''
        Cierra la interfaz inicial y abre la interfaz de registro.
        Creada por: .
        '''
        raiz.destroy()
        registro(num_partidas)
        

    def turnos(lista,jugadores):
        '''
        Muestra como van a ser los turnos despues de presionar el boton jugar.
        Creada por: Juan Pedro Demarco.
        '''
        mensaje_principio.set("Orden por turnos!!!:")
        mensaje_validacion.config(bg="#D5D8DC",fg="green")
        mezclar(lista)
        jugadores.set(lista)
        lista_jugadores.after(5000, lambda: raiz.destroy())
        lista_jugadores.config(bg="#D5D8DC",fg="green")
        
    #------------------- Botón enviar ------------------#
    boton_agregar_jugador=Button(mi_frame,text="Agregar jugador",command = lambda: agregar_jugador(),bg="#2DBCF1", fg="white",width="15", border=3)
    boton_agregar_jugador.grid(row=6,column=1,padx = 10, pady =10)

    boton_registro=Button(mi_frame,text="Registrarse",command = lambda: interfaz_registro(num_partidas),bg="#2DBCF1", fg="white",width="15", border=3)
    boton_registro.grid(row=6,column=2,padx = 10, pady =10)

    boton_enviar=Button(mi_frame,text="Jugar!", command = lambda:turnos(lista,jugadores) ,bg="#24CA1C", fg="white",width="15", border=3)
    boton_enviar.grid(row=6,column=0,padx = 10, pady =10)
    boton_enviar["state"] = DISABLED

    raiz.mainloop()

    return lista

def datos_jugadores(lista_nombres_ingresados):
    ''' 
    Crea el diccionario donde se registraran los datos de cada jugador.
    Creada por: Juan Pedro Demarco
    '''
    diccionario = {}
    for jugador in lista_nombres_ingresados:
        diccionario[jugador] = [0,0] #[cantidad de puntos, cantidad de intentos]
    return  diccionario 

def voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, datos_jugadores): #datos_jugadores es una tupla!
    '''
    Determina si las cartas ingresadas son iguales o no, en caso positivo acredita un punto al jugador y elimina las cartas del tablero.
    Si no son iguales, la cantidad de intentos del jugador se incrementa en uno y las cartas se dan vuelta.
    Creada por: Evangelina Zurita, Yennyfer Garcia
    '''
    CANT_PUNTOS=0
    CANT_INTENTOS=1 

    #lista_cartas= mezclar(lista_cartas)

    diccionario = datos_jugadores[0] #divido mi tupla en diccionario y nombre de usuarios.
    lista_participantes = datos_jugadores[1]
    
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
            lista_juego[primera_posicion-1] = LISTA_VACIA[primera_posicion-1] # Les asigno a las fichas el valor que tenian antes de darse vuelta.
            lista_juego[segunda_posicion-1] = LISTA_VACIA[segunda_posicion-1] # Les asigno a las fichas el valor que tenian antes de darse vuelta.
            print("Los cartas seleccionadas son distintas!")

            diccionario[lista_participantes[jugador]][CANT_INTENTOS] +=1

            if jugador == len(lista_participantes)-1: # Esta funcion es necesaria para que pueda repetir un jugador.
                jugador = 0
            else:
                jugador +=1

            #Si las fichas son iguales:
        elif lista_juego[primera_posicion-1] == lista_juego[segunda_posicion-1]:
            diccionario[lista_participantes[jugador]][CANT_PUNTOS] +=1
            diccionario[lista_participantes[jugador]][CANT_INTENTOS] +=1

            lista_juego[primera_posicion-1] = '[*]'
            lista_juego[segunda_posicion-1] = '[*]'
            lista_cartas[primera_posicion-1] = '[*]'
            lista_cartas[segunda_posicion-1] = '[*]'
            
        time.sleep(2.5)
        os.system("cls")
        contador_jugadas_totales += 1
    return diccionario 

def ganador(resultados, num_partidas):
    '''
    En calcula quien fue el ganador en base a los puntos obtenidos o ,en caso de empate, por la menor cantidad de intentos realizados.
    Creada por: Juan Pedro, Facundo Polech
    Interfaz y archivo partidas: Milton Fernández
    '''
    raiz = Tk()
    raiz.title("Registro Usuarios")
    raiz.config(bg="#D5D8DC")
    raiz.geometry('700x250')
    mi_frame=Frame(raiz)
    mi_frame.pack()
    mi_frame.config(bg="#D5D8DC")

    NOMBRE=PUNTOS=0
    TUPLA_DATOS=INTENTOS=1

    resultados = [(participante,puntos) for participante , puntos in resultados.items()] #lista de tuplas a partir de diccionario.

    resultados.sort(key = lambda elemento: elemento[TUPLA_DATOS][PUNTOS] ,reverse = True)
    numero_max = resultados[0][TUPLA_DATOS][PUNTOS]
    contador = 0
    raiz.partidas = 1

    for player in resultados:
        if numero_max == player[TUPLA_DATOS][PUNTOS]:
            contador +=1

    if contador>1:
        resultados.sort(key = lambda tupla: tupla[TUPLA_DATOS][INTENTOS]) #Se considera ganador al jugador con menor cantidad de intentos
        for j in range (len(resultados)):
            if j == 0:
                fondo = "#EABE3F" #Fondo del ganador
            else: fondo = "#D5D8DC"

            nombre_usuario=Label(mi_frame, text=f"Nombre de Jugador: {resultados[j][NOMBRE]}",bg=fondo)
            nombre_usuario.grid(row=j, column=0, padx = 10, pady =10)
                
            puntos=Label(mi_frame, text=f"Cantidad de aciertos: {resultados[j][TUPLA_DATOS][PUNTOS]}",bg=fondo)
            puntos.grid(row=j, column=1, padx = 10, pady =10)

            intentos=Label(mi_frame, text=f"Cantidad de intentos: {resultados[j][TUPLA_DATOS][INTENTOS]}",bg=fondo)
            intentos.grid(row=j, column=2, padx = 10, pady =10)

            promedio_intentos=Label(mi_frame, text=f"Cantidad promedio de intentos: {resultados[j][TUPLA_DATOS][INTENTOS]/len(resultados)}",bg=fondo)
            promedio_intentos.grid(row=j, column=3, padx = 10, pady =10)

    else:
        for i in range (len(resultados)):
            if i == 0:
                fondo = "#EABE3F"
            else: fondo = "#D5D8DC"

            nombre_usuario=Label(mi_frame, text=f"Nombre de Jugador: {resultados[i][NOMBRE]}",bg=fondo)
            nombre_usuario.grid(row=i, column=0, padx = 10, pady =10)

            puntos=Label(mi_frame, text=f"Cantidad de aciertos: {resultados[i][TUPLA_DATOS][PUNTOS]}",bg=fondo)
            puntos.grid(row=i, column=1, padx = 10, pady =10)

            intentos=Label(mi_frame, text=f"Cantidad de intentos: {resultados[i][TUPLA_DATOS][INTENTOS]}",bg=fondo)
            intentos.grid(row=i, column=2, padx = 10, pady =10)

            promedio_intentos=Label(mi_frame, text=f"Cantidad promedio de intentos: {resultados[i][TUPLA_DATOS][INTENTOS]/len(resultados)}",bg=fondo)
            promedio_intentos.grid(row=i, column=3, padx = 10, pady =10)

    def reiniciar(num_partidas):

        raiz.destroy()
    
        main(num_partidas)

    
    boton_continuar=Button(mi_frame,text="Volver a jugar",command= lambda: reiniciar(num_partidas), bg="#24CA1C", fg="white",width="15", border=3)
    boton_continuar.grid(row=len(resultados) + 1,column=1,padx = 10, pady =10)
    
    boton_abandonar=Button(mi_frame,text="Terminar",command= lambda: quit(), bg="#24CA1C", fg="white",width="15", border=3)
    boton_abandonar.grid(row=len(resultados) + 1,column=2,padx = 10, pady =10)
    
    #--------------------------------------- Partidas.csv ---------------------------------------------#

    reiniciar_archivo_partidas() #En caso de que el archivo de configuración lo requiera se reiniciará el archivo partidas
    
    validar_maximo_partidas(num_partidas, mi_frame, raiz) #Interfaz de control de partidas máximas.

    resultados.sort(key = lambda tupla: tupla[TUPLA_DATOS][INTENTOS])
    escritura_nombre_puntos_intentos(resultados) #Escribe los datos en Partidas.csv

    raiz.mainloop()

def crear_listas_juego():
    '''
    Creada por: Milton Fernández
    '''
    archivo = open('configuracion.csv', 'r')

    linea = leerArchivo(archivo,',')

    while linea[0] != 'CANTIDAD_FICHAS' and linea:
        linea = leerArchivo(archivo, ',')

    cantidad_de_fichas = int(linea[1])
        
    archivo.close()

    lista_juego = []
    lista_cartas = []
    LISTA_VACIA = []
    cantidad_de_letras = cantidad_de_fichas//2
    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abecedario_cortado = abecedario[0:cantidad_de_letras]

    for i in range (cantidad_de_fichas):
        lista_juego.append([i+1])
        LISTA_VACIA.append([i+1])
    
    for j in abecedario_cortado:
        lista_cartas.append([j])
        lista_cartas.append([j])
    
    return lista_juego, lista_cartas, LISTA_VACIA

#---------------Modificacion partidas_file -----------#   
def escritura_fecha_hora():
    '''
    Creada por: Milton Fernández
    '''
    fecha = datetime.datetime.now()
    fecha_de_partida = fecha.strftime('%d/%m/%Y')
    hora_de_finalizacion = fecha.strftime('%H:%M:%S')
    archivo = open("partidas.csv", "a")
    archivo.write("fecha_de_partida:")
    archivo.write(fecha_de_partida)
    archivo.write("; ")
    archivo.write("Hora de finalizacion:")
    archivo.write(hora_de_finalizacion)
    archivo.write("\n")
    archivo.write("----------------------")
    archivo.write("\n")

def escritura_nombre_puntos_intentos(resultados):
    NOMBRE=PUNTOS=0
    TUPLA_DATOS=INTENTOS=1
    for j in range (len(resultados)):
        archivo = open("partidas.csv", "a")
        fecha = datetime.datetime.now()
        fecha_de_partida = fecha.strftime('%d/%m/%Y')
        hora_de_finalizacion = fecha.strftime('%H:%M:%S')
        archivo.write(fecha_de_partida)
        archivo.write(",")
        archivo.write(hora_de_finalizacion)
        archivo.write(",")
        archivo.write(str(resultados[j][NOMBRE]))
        archivo.write(",")
        archivo.write(str(resultados[j][TUPLA_DATOS][PUNTOS]))
        archivo.write(",")
        archivo.write(str(resultados[j][TUPLA_DATOS][INTENTOS]))
        archivo.write(",")
        archivo.write(str(resultados[j][TUPLA_DATOS][INTENTOS]//len(resultados)))
        archivo.write("\n")

def reiniciar_archivo_partidas():
    '''
    Creada por: Milton Fernández
    '''
    archivo = open('configuracion.csv', 'r')

    linea = leerArchivo(archivo,',')

    while linea[0] != 'REINICIAR_ARCHIV0_PARTIDAS' and linea:
        linea = leerArchivo(archivo, ',')

    if str(linea[1]) == 'False':
        pass

    else:#si es diferente de False
        os.remove('partidas.csv')
    archivo.close()


#------------------------------------- Comienzo del juego -------------------------------------------#

def main(num_partidas):
    '''
    Creada por: Julieta Margenats
    '''
    lista_nombres_usuarios = nombres_jugadores(num_partidas) #ya me devuelve la lista desordenada
    diccionario = datos_jugadores(lista_nombres_usuarios)
    lista_juego, lista_cartas, LISTA_VACIA = crear_listas_juego()
    tiempo_inicial = time.time()
    resultados = voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, (diccionario,lista_nombres_usuarios))
    tiempo_partida = time.time() - tiempo_inicial
    num_partidas += 1
    ganador(resultados, num_partidas)
    print(f"El tiempo de la partida fue de {round(tiempo_partida)} segundos.")
    #escritura_fecha_hora()

num_partidas = 0        
main(num_partidas)
