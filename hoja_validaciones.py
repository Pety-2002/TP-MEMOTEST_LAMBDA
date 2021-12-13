from tkinter import *

#sacar esta funcion de aqui
def leerArchivo(archivo, default):
    """
    Devuelve las lineas del archivo
    Creada Por: Yennyfer Garcia
    """
    linea = archivo.readline()
    return linea.rstrip().split(',') if linea else default.split(',')

def validar_ingreso(numero,lista_cartas,lista_juego):
    '''
    Validar que el ingreso no sea una valor fuera de rango/no se encuentre disponible/no sea un numero/no sea una ficha ya tomada.
    Creada por: Facundo Polech
    '''
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas) or lista_juego[int(numero)-1] == '[*]' or lista_juego[int(numero)-1] in lista_cartas:
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada EXISTENTE en el tablero: ")
    return int(numero)

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

def validar_maximo_partidas(partidas, mi_frame, raiz):
    
    archivo = open('configuracion.csv', 'r')

    linea = leerArchivo(archivo,',')

    while linea[0] != 'MAXIMO_PARTIDAS' and linea:
        linea = leerArchivo(archivo, ',')

    if int(linea[1]) > partidas:
        partidas= Label(mi_frame, text= 'Puede seguir \n jugando', fg="red")
        partidas.grid(row=5, column=2, padx = 10, pady =10)
        partidas.after(3000, lambda: partidas.destroy())

    else:#si es igual a maximo de partidas (5)
        maximos= Label(mi_frame, text="Maximo de partidas alcanzado. \n El juego se cerrará",fg="red")
        maximos.grid(row=5, column=0, padx = 10, pady =10)
        maximos.after(4000, lambda: raiz.destroy())
        
    archivo.close() 
