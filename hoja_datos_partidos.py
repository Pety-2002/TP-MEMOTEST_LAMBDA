import os
import datetime
from hoja_validaciones import *

def escritura_fecha_hora():
    '''
    Creada por: Milton Fernández
    '''
    fecha = datetime.datetime.now()
    fecha_de_partida = fecha.strftime('%d/%m/%Y')
    hora_de_finalizacion = fecha.strftime('%H:%M:%S')
    archivo = open("partidas.csv", "a")
    archivo.write(f"fecha_de_partida:{fecha_de_partida},Hora de finalizacion:{hora_de_finalizacion}\n----------------------\n")

def escritura_nombre_puntos_intentos(resultados):
    NOMBRE=PUNTOS=0
    TUPLA_DATOS=INTENTOS=1
    resumen = open("resumen_total.csv", 'a')
    partidas = open("partidas.csv", "a")
    for j in range (len(resultados)):
        fecha = datetime.datetime.now()
        fecha_de_partida = fecha.strftime('%d/%m/%Y')
        hora_de_finalizacion = fecha.strftime('%H:%M:%S')
        nombre=str(resultados[j][NOMBRE])
        puntos=str(resultados[j][TUPLA_DATOS][PUNTOS])
        intentos=str(resultados[j][TUPLA_DATOS][INTENTOS])
        
        partidas.write(f"{fecha_de_partida},{hora_de_finalizacion},{nombre},{puntos},{intentos}\n")
        resumen.write(f'{nombre},{puntos},{intentos}\n')
    resumen.close()
    partidas.close

def reiniciar_archivo_partidas(REINICIAR_ARCHIV0_PARTIDAS):
    '''
    Creada por: Milton Fernández
    '''
    if  REINICIAR_ARCHIV0_PARTIDAS == 'True':
        os.remove('partidas.csv')

def resumen_total():
    '''
    Imprime el resumen_total
    Creada por: Julieta Margenats
    ''' 
    ar_partidas = open('resumen_total.csv', 'r')
    nombre, puntos, intentos = leerArchivo(ar_partidas, ',,')
    dic = {}
    while nombre:
        if nombre not in dic:
            dic[nombre] = [int(puntos), int(intentos)]
        else: 
            dic[nombre][0] += int(puntos)
            dic[nombre][1] += int(intentos)
        nombre, puntos, intentos = leerArchivo(ar_partidas, ',,')
    
    print(f'\nresumen total: \n')
    for clave in dic:
        print(f'Nombre: {clave} \nAciertos: {dic[clave][0]} \nIntentos: {dic[clave][1]}\n-------------')
    ar_partidas.close()
    