
from tkinter import *
from hoja_manipulacion_archivos import leer_linea_archivo

def validar_ingreso(numero,lista_cartas,lista_juego):
    '''
    Validar que el ingreso no sea una valor fuera de rango/no se encuentre disponible/no sea un numero/no sea una ficha ya tomada.
    CREADA POR: FACUNDO POLECH
    '''
    while not numero.isdigit() or int(numero)<=0 or int(numero)>len(lista_cartas) or lista_juego[int(numero)-1] == '[*]' or lista_juego[int(numero)-1] in lista_cartas:
        numero = input("ERROR 401 :) /Escribir un NUMERO correspondiente a la posicion de la ficha deseada EXISTENTE en el tablero: ")
    return int(numero)

def validar_registracion(nombre,contraseña):
    """
    Valida si el usuario se encuentra en el archivo
    CREADA POR: EVANGELINA ZURITA
    COLABORADOR: YENNYFER GARCIA
    """
    archivo = open('registro_usuarios.csv',"r")

    end="99999"
    linea_1=leer_linea_archivo(archivo,end)
    se_encuentra=False
    not_contraseña_correcta = False
    while linea_1[0]!=end and se_encuentra==False:
        if linea_1[0]==nombre and linea_1[1]==contraseña:
            se_encuentra=True
        elif linea_1[0] == nombre and linea_1[1] !=contraseña:
            not_contraseña_correcta = True
        linea_1 =leer_linea_archivo(archivo,end)

    archivo.close()
    return se_encuentra,not_contraseña_correcta

def validar_nombre_usuario(nombre_usuario):
    """
    Valida que el nombre del usuario cumpla con las caracteristicas requeridas
    CREADA POR: EVANGELINA ZURITA
    """
    valida=False
    guion_bajo=nombre_usuario.find("_")
    if (4<=len(nombre_usuario)<=15) and (nombre_usuario.isalpha()== False) and (nombre_usuario.isnumeric()==False) and (guion_bajo!=-1):
        valida=True
    return valida

def validar_contraseña_usuario(contraseña):
    """
    Valida si el usuario ingresó una contraseña que cumple con las condiciones dadas
    CREADA POR: EVANGELINA ZURITA
    """
    valida=False
    alfanumerico= contraseña.isalpha()==False and contraseña.isnumeric()==False
    i=j=k=l=0
    if 8<=len(contraseña)<=12 and alfanumerico:
        invalido=False
        mayuscula=False
        minuscula=False
        guiones=False
        caracteres_invalidos='áéíóúÁÉÍÓÚ'
       
        while guiones==False and i<len(contraseña):
            if contraseña[i] == "-" or contraseña[i] == "_": guiones=True
            i+=1

        while invalido==False and j<len(contraseña):
            if contraseña[j] in caracteres_invalidos: invalido=True
            j+=1
    
        while mayuscula==False and k<len(contraseña):
            if contraseña[k].isupper():mayuscula=True
            k+=1
        
        while minuscula==False and l<len(contraseña):
            if contraseña[l].islower(): minuscula=True
            l+=1
        
        if guiones and invalido==False and mayuscula and minuscula:
            valida=True
    
    return valida

def validar_maximo_jugadores(max_jugadores, jugadores):
    """
    verifica que no se sobrepase el limite de jugadores
    CREADA POR: JULIETA MARGENATS
    """
    if max_jugadores> jugadores:
        devolver = True 
    else:
        devolver = False 
    return devolver

def validar_maximo_partidas(maximo_partidas ,partidas, mi_frame, raiz,filas,boton_continuar):
    '''
    Verifica que no se sobrepase el limite de partidas
    CREADA POR: EVANGELINA ZURITA
    COLABORADOR: MILTON FERNANDEZ
    '''
    if maximo_partidas > partidas:
        partidas= Label(mi_frame, text= 'Puede seguir \n jugando', fg="red")
        partidas.grid(row=filas+3, column=0, columnspan=4, padx = 10, pady =10)

    else:#si es igual a maximo de partidas 
        maximos= Label(mi_frame, text="MAXIMO DE PARTIDAS ALCANZADO. \n El juego se cerrará automaticamente en 15 segundos",fg="red")
        maximos.grid(row=filas+3, column=0,columnspan=4, padx = 10, pady =10)
        boton_continuar["state"] = DISABLED
        maximos.after(15000, lambda: raiz.destroy())