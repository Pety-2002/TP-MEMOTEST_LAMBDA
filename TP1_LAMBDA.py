from hoja_validaciones import * 
from hoja_datos_partidos import *
import random
from tkinter import *
import time
import os

#----------------- AUXILIARES ----------------
def mezclar(lista):
    '''
    Para mezclar las cartas y/o orden de los jugadores para que se encuentren en diferentes posiciones en c/partida.
    Creada por: Facundo Polech
    '''
    lista_mezclada = lista
    random.shuffle(lista_mezclada)
    return lista_mezclada

#----------------- ARCHIVOS----------------------
def leer_config():
    '''
    Lee el archivo de configuracion solo 1 vez al iniciar el programa
    Creada por: Julieta Margenats
    Si no tienen los valores prestablecidos, se tienen que configurar lo valores "por defecto" usqra ternario
    '''
    ar_config = open('configuracion.csv', 'r')
    linea = leerArchivo(ar_config, ',')

    cantidad_fichas = [int(linea[1]), 'configuracion'] if linea[1] and linea[1] % 2 == 0 and linea[1] < 53 else [8, 'defecto']
    linea = leerArchivo(ar_config, ',')

    max_jugadores = [int(linea[1]), 'configuracion'] if linea[1] else [3, 'defecto']
    linea = leerArchivo(ar_config, ',')

    max_partidas = [int(linea[1]), 'configuracion'] if linea[1] else [2, 'defecto']
    linea = leerArchivo(ar_config, ',')

    reiniciar_ar = [linea[1], 'configuracion'] if linea[1] else ['False', 'defecto']
    ar_config.close()

    return cantidad_fichas, max_jugadores, max_partidas, reiniciar_ar

def agregar_linea(linea):
    """
    Agrega el nombre y contraseña del usuario al archivo
    Creada Por: Yennyfer Garcia
    """
    archivo = open ("registro_usuarios.csv","a")
    archivo.write(linea + "\n")
    archivo.close()

#------------------  EJECUCIONES DE INTERFACES------------------

def guardar_usuarios(nombre, contraseña, contraseña_repetida,mensaje):
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

def inicio(window):
    window.destroy()
    #nombres_jugadores()

def interfaz_registro(raiz):
    '''
    Cierra la interfaz inicial y abre la interfaz de registro.
    Creada por: .
    '''
    registro()

def reiniciar(num_partidas,raiz):
    raiz.destroy()
    main(num_partidas)

#-------------------------- INTERFACES------------------------

def registro():
    """
    Crea la interfaz de registro de los usuarios
    Creada Por: Yennyfer Garcia
    """

    window = Toplevel()
    window.title("Registro Usuarios")
    window.config(bg="#D5D8DC")
    window.geometry('350x250')
    mi_frame=Frame(window)
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

    #----------Botones---------------------------

    boton_crear_ususario=Button(mi_frame,text="Crear Usuario",command = lambda: guardar_usuarios(cuadro_nombre.get(), cuadro_contraseña.get(), contraseña_repetida.get(),mensaje) ,bg="#24CA1C", fg="white",width="15", border=3)
    boton_crear_ususario.grid(row=5,column=0,padx = 10, pady =10)
    
    boton_volver_inicio=Button(mi_frame,text="Volver inicio",command = lambda: window.destroy(),bg="#24CA1C", fg="white",width="15", border=3)
    boton_volver_inicio.grid(row=5,column=1,padx = 10, pady =10)

    window.mainloop()

def nombres_jugadores():
    """
    CREA LA INTERFAZ INICIAL para solicitar el nombre de los jugadores.
    Creada por: Milton Fernandez, Yennyfer Garcia, Juan Pedro Demarco.
    """
    buttonClicked  = False # Antes de apretar el boton jugar.
    raiz = Tk()
    lista = [] #guarda los nombres de los jugadores.
    raiz.title("Ingreso Usuarios")
    raiz.config(bg="#D5D8DC")
    raiz.geometry('500x360')
    raiz.resizable(False, False)
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
    mensaje_validacion.grid(row=4,column=0, columnspan=3 ,padx = 10, pady =5)
    mensaje_validacion.after(4000, lambda: mensaje_principio.set("JUGADORES: "))
    mensaje_validacion.config(bg="#3B7E9E",fg="white")

    jugadores=StringVar() #lista de jugadores
    lista_jugadores=Label(mi_frame,textvariable=jugadores)
    lista_jugadores.grid(row=5,column=0, columnspan=3 ,padx = 10, pady =5)
    lista_jugadores.config(bg="#D5D8DC",fg="blue")

    archivo_config=Label(mi_frame,text="ARCHIVO DE CONFIGURACION:")#Archivo de configuracion
    archivo_config.grid(row=7,column=0, columnspan=3 ,padx = 10, pady =5)
    archivo_config.config(bg="#3B7E9E",fg="white")

    archivo_config=Label(mi_frame,text=f"CANTIDAD_FICHAS:  {CANTIDAD_FICHAS}")#Archivo de configuracion
    archivo_config.grid(row=8,column=0, columnspan=4 ,padx = 2, pady =5)
    archivo_config.config(bg="#2DBCF1",fg="white")

    archivo_config=Label(mi_frame,text=f"MAXIMO_JUGADORES:  {MAXIMO_JUGADORES}")#Archivo de configuracion
    archivo_config.grid(row=9,column=0, columnspan=4 ,padx = 2, pady =5)
    archivo_config.config(bg="#2DBCF1",fg="white")

    archivo_config=Label(mi_frame,text=f"MAXIMO_PARTIDAS:  {MAXIMO_PARTIDAS}")#Archivo de configuracion
    archivo_config.grid(row=10,column=0, columnspan=4 ,padx = 2, pady =5)
    archivo_config.config(bg="#2DBCF1",fg="white")

    archivo_config=Label(mi_frame,text=f"REINICIAR_ARCHIV0_PARTIDAS:  {REINICIAR_ARCHIV0_PARTIDAS}")#Archivo de configuracion
    archivo_config.grid(row=11,column=0, columnspan=4 ,padx = 2, pady =5)
    archivo_config.config(bg="#2DBCF1",fg="white")
    #---------------- Entradas de texto -----------------#

    cuadro_nombre=Entry(mi_frame, border="3")
    cuadro_nombre.grid(row=1,column=1,padx = 10, pady =10)

    cuadro_contraseña=Entry(mi_frame ,border="3")
    cuadro_contraseña.grid(row=2,column=1,padx = 10, pady =10)
    cuadro_contraseña.config(show="*")

    def obtener_nombres(jugadores, username,password,raiz,mensaje,boton ):
        '''
        Guarda el nombre del jugador en una lista, luego de conocer que ya esta registrado. En caso contrario, avisa al participante que
        se registre primero.
        Creada por: Julieta Margenats, Juan Pedro Demarco.
        '''
        usuario_existe = validar_registracion(username, password)

        if usuario_existe[0]:#usuario y contraseña existen
            lista.append(username) #Los usuarios que se encuentran registrados se van sumando a la lista de jugadores.
            jugadores.set(lista)
            maximo_jugadores = validar_maximo_jugadores(MAXIMO_JUGADORES[0], len(lista))#verificacion el maximo de jugadores

            if maximo_jugadores:
                raiz.contador +=1
                mensaje.set('Puede seguir \n ingresando usuarios')
                boton["state"] = NORMAL

            else: #Se destruye despues de 4 segundos si llega al maximo
                mensaje_derecha.set('MAXIMO de jugadores \nalcanzado.El juego \ncomenzara en breve!')
                turnos(lista,lista_jugadores,jugadores)
                

        elif usuario_existe[1]: #usuario existe pero la contraseña no es correcta
            mensaje.set('El usuario existe pero \n la contraseña no es correcta')

        else:
            mensaje.set('El usuario no esta registrado.\nPor favor, registrese primero.')

    def agregar_jugador(lista,label_usuario,label_contraseña,caja_nombre,caja_contraseña,boton):
        '''
        Funcion que se llama cada vez que queremos agregar un jugador. Actualiza la interfaz en el proceso. Se verifica que el jugador 
        este registrado anteriormente.
        Creada por: Juan Pedro Demarco.
        '''
        jugadores, nombre, contraseña, raiz, mensaje = lista
        obtener_nombres(jugadores, nombre, contraseña, raiz, mensaje, boton)
        label_usuario.set(f'Nombre usuario {raiz.contador}:')
        label_contraseña.set(f'Contraseña usuario {raiz.contador}:')
        caja_nombre.delete(0, END)
        caja_contraseña.delete(0, END)

    def turnos(lista,label_jugadores,jugadores):
        '''
        Muestra como van a ser los turnos despues de presionar el boton jugar.
        Creada por: Juan Pedro Demarco.
        '''
        mensaje_principio.set("Orden por turnos!!!:")
        mensaje_validacion.config(bg="#D5D8DC",fg="green")
        mezclar(lista)
        jugadores.set(lista)
        label_jugadores.config(bg="#D5D8DC",fg="green")
        label_jugadores.after(4000, lambda: raiz.destroy())
        
    #------------------- Botón enviar ------------------#
    boton_agregar_jugador=Button(mi_frame,text="Agregar jugador",command = lambda: agregar_jugador([jugadores,cuadro_nombre.get(),cuadro_contraseña.get(),raiz,mensaje_derecha],users_label, contra_label,cuadro_nombre,cuadro_contraseña,boton_enviar),bg="#2DBCF1", fg="white",width="15", border=3)
    boton_agregar_jugador.grid(row=3,column=1,padx = 10, pady =10)

    boton_registro=Button(mi_frame,text="Registrarse",command = lambda: interfaz_registro(raiz),bg="#2DBCF1", fg="white",width="15", border=3)
    boton_registro.grid(row=3,column=2,padx = 10, pady =10)

    boton_enviar=Button(mi_frame,text="Jugar!", command = lambda: turnos(lista,lista_jugadores,jugadores) ,bg="#24CA1C", fg="white",width="15", border=3)
    boton_enviar.grid(row=3,column=0,padx = 10, pady =10)
    boton_enviar["state"] = DISABLED

    raiz.mainloop()

    return lista

def interfaz_ganador(resultados,num_partidas):
    raiz = Tk()
    raiz.title("Ranking")
    raiz.config(bg="#D5D8DC")
    raiz.geometry('700x250')
    mi_frame=Frame(raiz)
    mi_frame.pack()
    mi_frame.config(bg="#D5D8DC")
    filas = len(resultados)

    NOMBRE=PUNTOS=0
    TUPLA_DATOS=INTENTOS=1

    for j in range (filas):
        
        fondo="#EABE3F" if j == 0 else "#D5D8DC"

        nombre_usuario=Label(mi_frame, text=f"Nombre de Jugador: {resultados[j][NOMBRE]}",bg=fondo)
        nombre_usuario.grid(row=j, column=0, padx = 10, pady =10)
            
        puntos=Label(mi_frame, text=f"Cantidad de aciertos: {resultados[j][TUPLA_DATOS][PUNTOS]}",bg=fondo)
        puntos.grid(row=j, column=1, padx = 10, pady =10)

        intentos=Label(mi_frame, text=f"Cantidad de intentos: {resultados[j][TUPLA_DATOS][INTENTOS]}",bg=fondo)
        intentos.grid(row=j, column=2, padx = 10, pady =10)

        promedio_intentos=Label(mi_frame, text=f"Cantidad promedio de intentos: {resultados[j][TUPLA_DATOS][INTENTOS]/filas}",bg=fondo)
        promedio_intentos.grid(row=j, column=3, padx = 10, pady =10)
    
    boton_continuar=Button(mi_frame,text="Volver a jugar",command= lambda: reiniciar(num_partidas,raiz), bg="#24CA1C", fg="white",width="15", border=3)
    boton_continuar.grid(row=filas + 1,column=1,padx = 10, pady =10)
    
    boton_abandonar=Button(mi_frame,text="Terminar",command= lambda: raiz.destroy(), bg="#24CA1C", fg="white",width="15", border=3)
    boton_abandonar.grid(row=filas + 1,column=2,padx = 10, pady =10)

    validar_maximo_partidas(MAXIMO_PARTIDAS[0], num_partidas, mi_frame, raiz,filas) #Interfaz de control de partidas máximas.
    raiz.mainloop()

#-------------------- JUEGO --------------------
def imprimir_tablero(lista_juego):
    '''
    Imprimo el tablero. Creo slices de 4 para imprimir por linea 4 fichas.
    Creada por: Juan Pedro Demarco
    '''
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])

def datos_jugadores(lista_nombres_ingresados):
    ''' 
    Crea el diccionario donde se registraran los datos de cada jugador.
    Creada por: Juan Pedro Demarco
    '''
    diccionario = {}
    for jugador in lista_nombres_ingresados:
        diccionario[jugador] = [0,0] #[cantidad de puntos, cantidad de intentos]
    return  diccionario 

def crear_listas_juego():
    '''
    Creada por: Milton Fernández
    '''

    lista_juego = []
    lista_cartas = []
    LISTA_VACIA = []
    cantidad_de_letras = CANTIDAD_FICHAS[0]//2
    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abecedario_cortado = abecedario[0:cantidad_de_letras]

    for i in range (CANTIDAD_FICHAS[0]):
        lista_juego.append([i+1])
        LISTA_VACIA.append([i+1])
    
    for j in abecedario_cortado:
        lista_cartas.append([j])
        lista_cartas.append([j])
    
    return lista_juego, lista_cartas, LISTA_VACIA

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
            
        #time.sleep(2.5)
        os.system("cls")
        contador_jugadas_totales += 1
    return diccionario 

def ganador(resultados, num_partidas):
    '''
    En calcula quien fue el ganador en base a los puntos obtenidos o ,en caso de empate, por la menor cantidad de intentos realizados.
    Creada por: Juan Pedro, Facundo Polech
    Interfaz y archivo partidas: Milton Fernández
    '''
    PUNTOS=0
    TUPLA_DATOS=INTENTOS=1

    resultados = [(participante,puntos) for participante , puntos in resultados.items()] #lista de tuplas a partir de diccionario.

    resultados.sort(key = lambda elemento: elemento[TUPLA_DATOS][PUNTOS] ,reverse = True)
    numero_max = resultados[0][TUPLA_DATOS][PUNTOS]
    contador = 0

    for player in resultados: #Este loop funciona para saber si existen mas jugadores que comparten la mayor cantidad de puntos.
        if numero_max == player[TUPLA_DATOS][PUNTOS]:
            contador +=1

    if contador>1:
        resultados.sort(key = lambda tupla: tupla[TUPLA_DATOS][INTENTOS]) #Se considera ganador al jugador con menor cantidad de intentos
    
    interfaz_ganador(resultados,num_partidas)
    #--------------------------------------- Partidas.csv ---------------------------------------------#

    reiniciar_archivo_partidas(REINICIAR_ARCHIV0_PARTIDAS[0]) #En caso de que el archivo de configuración lo requiera se reiniciará el archivo partidas
    escritura_nombre_puntos_intentos(resultados) #Escribe los datos en Partidas.csv

#------------------------------------- COMIENZO DEL JUEGO -------------------------------------------#

def main(num_partidas):
    '''
    Creada por: Julieta Margenats
    '''
    num_partidas += 1 #Se incrementa el numero de partidas
    lista_nombres_usuarios = nombres_jugadores() #Llamo a la interfaz de inicio, me devuelve la lista desordenada con los jugadores.
    diccionario = datos_jugadores(lista_nombres_usuarios) #Creo diccionario para cada uno de los jugadores.
    lista_juego, lista_cartas, LISTA_VACIA = crear_listas_juego()
    tiempo_inicial = time.time() #Inicializo el tiempo para arrancar a contar
    resultados = voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, (diccionario,lista_nombres_usuarios))
    tiempo_partida = time.time() - tiempo_inicial
    print(f'El tiempo de la partida es de {int(tiempo_partida)} segundos')
    time.sleep(1.5)
    os.system("cls")
    ganador(resultados, num_partidas) #Se calcula y muestra el ganador del juego en una interfaz.
    #escritura_fecha_hora()

CANTIDAD_FICHAS, MAXIMO_JUGADORES, MAXIMO_PARTIDAS, REINICIAR_ARCHIV0_PARTIDAS = leer_config()
num_partidas = 0 #para controlar cuantas partidas se jugaron
main(num_partidas)
resumen_total()
os.remove('resumen_total.csv')
