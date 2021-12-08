
import random
from tkinter import *
import time
import os
import datetime

def mezclar(lista):
    '''
    Para mezclar las "cartas" y se encuentren en diferentes posiciones en c/partida (se mantienen los caracteres) (etapa 4)
    Creada por: Facundo Polech
    '''
    lista_mezclada = lista
    random.shuffle(lista_mezclada)
    return lista_mezclada

def validar_ingreso(numero,lista_cartas,lista_juego):
    '''
    Validar que el ingreso no sea una valor fuera de rango/no se encuentre disponible/no sea un numero/no sea una ficha ya tomada.
    Creada por: Facundo Polech
    '''
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas) or lista_juego[int(numero)-1] == '[*]' or lista_juego[int(numero)-1] in lista_cartas:
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada EXISTENTE en el tablero: ")
    return int(numero)

def imprimir_tablero(lista_juego):
    '''
    Imprimo el tablero. Creo slices de 4 para imprimir por linea 4 fichas.
    Creada por: JuanP
    '''
    for contador in range(0,len(lista_juego),4):
        print(lista_juego[contador:4+contador])

def leerArchivo(archivo, default):
    """
    Devuelve las lineas del archivo
    Creada Por: Yennyfer Garcia
    """
    linea = archivo.readline()
    return linea.rstrip().split(',') if linea else default.split(',')

def agregar_linea(archivo,linea):
    """
    Agrega el nombre y contraseña del usuario al archivo
    Creada Por: Yennyfer Garcia
    """
    archivo.write(linea + "\n")

def validar_registracion(archivo,nombre,contraseña):
    """
    Valida si el usuario se encuentra en el archivo
    Creada Por: Yennyfer Garcia
    """
    end="99999"
    linea_1=leerArchivo(archivo,end)
    se_encuentra=False
    while linea_1[0]!=end and se_encuentra==False:
        if linea_1[0]==nombre and linea_1[1]==contraseña:
            se_encuentra=True
        linea_1=leerArchivo(archivo,end)
    return se_encuentra

def validar_nombre_usuario(nombre_usuario):
    """
    Valida que el nombre del usuario cumpla con las caracteristicas requeridas
    Creada por: Yennyfer Garcia
    """
    valida=False
    guion_bajo=nombre_usuario.find("_")
    if (4<=len(nombre_usuario)<=15) and (nombre_usuario.isalpha()== False) and (nombre_usuario.isnumeric()==False) and (guion_bajo!=-1):
        valida=True
    return valida

def validar_contraseña_usuario(contraseña):
    valida=False
    alfanumerico= (contraseña.isalpha()==False) and (contraseña.isnumeric()==False)
    i=j=k=l=0
    if (8<=len(contraseña)<=12) and alfanumerico  :
        invalido=False
        mayuscula=False
        minuscula=False
        guiones=False
        caracteres_invalidos='áéíóúÁÉÍÓÚ'
        #----------OPTIMIZAR-----------------
        while (guiones==False) and i<len(contraseña):
            if contraseña[i] == "-" or contraseña[i] == "_" : guiones=True
            i+=1

        while (invalido==False) and j<len(contraseña):
            if contraseña[j] in caracteres_invalidos: invalido=True
            j+=1
    
        while (mayuscula==False) and k<len(contraseña):
            if contraseña[k].isupper():mayuscula=True
            k+=1
        
        while (minuscula==False) and l<len(contraseña):
            if contraseña[l].islower(): minuscula=True
            l+=1
        #--------------------------------------
        if guiones and (invalido==False) and mayuscula and minuscula:
            valida=True
    
    return valida

def validar_maximo_jugadores(archivo, jugadores): #necesita el archivo de configuracion y la longitud de la lista de jugadores para comparar
    """
    verifica que no se sobrepase el limite de jugadores
    Creada Por: Julieta Margenats
    """
    linea = leerArchivo(archivo,',')
    while linea[0] != 'MAXIMO_JUGADORES' and linea:
        linea = leerArchivo(archivo, ',')
    if int(linea[1]) > jugadores:
        devolver = True
    else:#si es igual a maximo de jugadores (2)
        devolver = False
    return devolver

def registro():
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
        if (contraseña_repetida==contraseña) and nombre_valido :
            
            archivo_usuarios=open("registro_usuarios.txt","r+")
            se_encuentra=validar_registracion(archivo_usuarios,nombre, contraseña)
            contraseña_valida=validar_contraseña_usuario(contraseña)
            
            if se_encuentra:
                mensaje.set("Usted ya se encuentra registrado")
            elif contraseña_valida==False:
                mensaje.set("La contraseña debe contener: Entre 8 y 12 caracteres,\n una letra mayuscula, una letra minuscula (sin acentos)\ny tener un guion (bajo o medio)")
            else:
                linea=(f"{nombre},{contraseña}")
                agregar_linea(archivo_usuarios,linea)
                mensaje.set("Se ha registrado exitosamente")
                #time.sleep(1.5)
                #raiz.destroy()
            archivo_usuarios.close()
        else:
            mensaje.set("alguno de los datos ingresados \n es invalido")
        
    def inicio():
        raiz.destroy()
        main()
        

                
    #----------Boton---------------------------

    boton_crear_ususario=Button(mi_frame,text="Crear Usuario",command= lambda: guardar_usuarios(cuadro_nombre.get(), cuadro_contraseña.get(), contraseña_repetida.get()) ,bg="#24CA1C", fg="white",width="15", border=3)
    boton_crear_ususario.grid(row=5,column=0,padx = 10, pady =10)
    
    boton_volver_inicio=Button(mi_frame,text="Volver inicio",command= lambda: inicio(),bg="#24CA1C", fg="white",width="15", border=3)
    boton_volver_inicio.grid(row=5,column=1,padx = 10, pady =10)


    raiz.mainloop() 

def nombres_jugadores():
    """
    CREA LA INTERFAZ para solicitar el nombre de los jugadores 
    Creada por: Milton Fernandez, Yennyfer Garcia.
    """
    raiz = Tk()
    lista = []
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

    #---------------- Entradas de texto -----------------#

    cuadro_nombre=Entry(mi_frame, border="3")
    cuadro_nombre.grid(row=1,column=1,padx = 10, pady =10)

    cuadro_contraseña=Entry(mi_frame ,border="3")
    cuadro_contraseña.grid(row=2,column=1,padx = 10, pady =10)
    cuadro_contraseña.config(show="*")

    """
    Nota: 

    1. Verificar que ambos usuarios esten en el archivo de lo contrario insertar aviso de registro
    2. Verificar que las contraseñas ingresadas sean las Correctas si no lo son avisar cual es la incorrecta
    3. Ejecutar el juego

    """

    def obtener_nombres():
        '''
        Guarda el nombre del jugador en una lista, luego de conocer que ya esta registrado. En caso contrario, avisa al participante que
        se registre primero.
        Creada por: Julieta Margenats, Juan Pedro Demarco.
        '''
        archivo = open('registro_usuarios.txt',"r")
        se_encuentra_jugador = validar_registracion(archivo,cuadro_nombre.get(), cuadro_contraseña.get())
        archivo.close()

        if se_encuentra_jugador:
            lista.append(cuadro_nombre.get()) #Los usuarios que se encuentran registrados se van sumando a la lista de jugadores.
            #verificacion el maximo de jugadores
            ar_config = open('configuracion.csv', 'r')
            maximo_jugadores = validar_maximo_jugadores(ar_config, len(lista))
            ar_config.close()

            if maximo_jugadores:
                raiz.contador +=1
                jugadores=Label(mi_frame, text= 'Puede seguir \n ingresando usuarios', fg="red")
                jugadores.grid(row=5, column=2, padx = 10, pady =10)
                jugadores.after(3000, lambda: jugadores.destroy())
            
            else: #Se destruye despues de 3 segundos si llega al maximo
                maximos=Label(mi_frame, text="Maximo de jugadores alcanzado. \n El juago comenzara",fg="red")
                maximos.grid(row=5, column=0, padx = 10, pady =10)
                maximos.after(4000, lambda: raiz.destroy())
        
        else:
            advertencia=Label(mi_frame, text="Por favor, registrese primero.",fg="red")
            advertencia.grid(row=5, column=0, padx = 10, pady =10)
            advertencia.after(4000, lambda: advertencia.destroy())
        

    def agregar_jugador():
        '''
        Funcion que se llama cada vez que queremos agregar un jugador. Actualiza la interfaz en el proceso. Se verifica que el jugador 
        este registrado anteriormente.
        Creada por: Juan Pedro Demarco.
        '''
        obtener_nombres()
        users_label.set(f'Nombre usuario {raiz.contador}:')
        contra_label.set(f'Contraseña usuario {raiz.contador}:')
        cuadro_nombre.delete(0, END)
        cuadro_contraseña.delete(0, END)


    def interfaz_registro():
        raiz.destroy()
        registro()

    #------------------- Botón enviar ------------------#
    boton_agregar_jugador=Button(mi_frame,text="Agregar jugador",command = lambda: agregar_jugador(),bg="#2DBCF1", fg="white",width="15", border=3)
    boton_agregar_jugador.grid(row=6,column=1,padx = 10, pady =10)

    boton_registro=Button(mi_frame,text="Registrarse",command = lambda: interfaz_registro(),bg="#2DBCF1", fg="white",width="15", border=3)
    boton_registro.grid(row=6,column=2,padx = 10, pady =10)

    boton_enviar=Button(mi_frame,text="Jugar", command = lambda: raiz.destroy(),bg="#24CA1C", fg="white",width="15", border=3)
    boton_enviar.grid(row=6,column=0,padx = 10, pady =10)


    raiz.mainloop() 
    return lista

def datos_jugadores(lista_nombres_ingresados):
    ''' 
    Crea el diccionario donde se registraran los datos de cada jugador.
    Creada por: Juan Pedro Demarco
    '''
    diccionario = {}
    lista_nombres_ingresados = mezclar(lista_nombres_ingresados)
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

def ganador(resultados):
    '''
    En calcula quien fue el ganador en base a los puntos obtenidos o ,en caso de empate, por la menor cantidad de intentos realizados.
    Creada por: Juan Pedro, Facundo Polech
    Interfaz y archivo partidas: Milton Fernández
    '''
    raiz = Tk()
    raiz.title("Registro Usuarios")
    raiz.config(bg="#D5D8DC")
    raiz.geometry('500x250')
    mi_frame=Frame(raiz)
    mi_frame.pack()
    mi_frame.config(bg="#D5D8DC")

    NOMBRE=PUNTOS=0
    TUPLA_DATOS=INTENTOS=1

    resultados = [(participante,puntos) for participante , puntos in resultados.items()] #lista de tuplas a partir de diccionario.

    resultados.sort(key = lambda tupla: tupla[TUPLA_DATOS][INTENTOS])

    for j in range (len(resultados)):
        archivo = open("partidas.csv", "a")
        archivo.write("Jugador:")
        archivo.write(str(resultados[j][NOMBRE]))
        archivo.write("; ")
        archivo.write("Puntos:")
        archivo.write(str(resultados[j][TUPLA_DATOS][PUNTOS]))
        archivo.write("; ")
        archivo.write("Intentos:")
        archivo.write(str(resultados[j][TUPLA_DATOS][INTENTOS]))
        archivo.write("\n")

    resultados.sort(key = lambda elemento: elemento[TUPLA_DATOS][PUNTOS] ,reverse = True)
    numero_max = resultados[0][TUPLA_DATOS][PUNTOS]
    contador = 0

    for player in resultados:
        if numero_max == player[TUPLA_DATOS][PUNTOS]:
            contador +=1

    if contador>1:
        resultados.sort(key = lambda tupla: tupla[TUPLA_DATOS][INTENTOS])
        for j in range (len(resultados)):
            if j == 0:
                fondo = "#EABE3F"
            else: fondo = "#D5D8DC"

            nombre_usuario=Label(mi_frame, text=f"Nombre de Jugador: {resultados[j][NOMBRE]}",bg=fondo)
            nombre_usuario.grid(row=j, column=0, padx = 10, pady =10)
                
            puntos=Label(mi_frame, text=f"Cantidad de aciertos: {resultados[j][TUPLA_DATOS][PUNTOS]}",bg=fondo)
            puntos.grid(row=j, column=1, padx = 10, pady =10)

            intentos=Label(mi_frame, text=f"Cantidad de intentos: {resultados[j][TUPLA_DATOS][INTENTOS]}",bg=fondo)
            intentos.grid(row=j, column=2, padx = 10, pady =10)
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

    def reiniciar():
        raiz.destroy()
        main()

    boton_continuar=Button(mi_frame,text="Volver a jugar",command= lambda: reiniciar() ,bg="#24CA1C", fg="white",width="15", border=3)
    boton_continuar.grid(row=len(resultados) + 1,column=0,padx = 10, pady =10)
    
    boton_abandonar=Button(mi_frame,text="Terminar",command= lambda: raiz.destroy(), bg="#24CA1C", fg="white",width="15", border=3)
    boton_abandonar.grid(row=len(resultados) + 1,column=2,padx = 10, pady =10)

def main():
    '''
    Creada por: Julieta Margenats
    '''
    fecha = datetime.datetime.now()
    seguir = "s"
    while seguir == "s":
        fecha_de_partida = fecha.strftime('%d/%m/%Y')
        lista_nombres_usuarios = nombres_jugadores()
        diccionario = datos_jugadores(lista_nombres_usuarios)
        #lista_juego = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16]]
        #lista_cartas = ["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H"]
        lista_juego = [[1],[2]]
        lista_cartas = ["A","A"]
        tiempo_inicial = time.time()
        resultados = voltear_cartas(lista_juego, lista_cartas, LISTA_VACIA, (diccionario,lista_nombres_usuarios))
        tiempo_partida = time.time() - tiempo_inicial
        ganador(resultados)
        hora_de_finalizacion = fecha.strftime('%H:%M:%S')
        print(f"El tiempo de la partida fue de {round(tiempo_partida)} segundos.")

        archivo = open("partidas.csv", "a")
        archivo.write("fecha_de_partida:")
        archivo.write(fecha_de_partida)
        archivo.write("; ")
        archivo.write("Hora de finalizacion:")
        archivo.write(hora_de_finalizacion)
        archivo.write("\n")
        archivo.write("----------------------")
        archivo.write("\n")
        seguir = input("¿Seguir jugando?(s/n): ")
#------------------------------------- Comienzo del juego -------------------------------------------#

cartas = ['A']
LISTA_VACIA = [[1],[2]]


main()
