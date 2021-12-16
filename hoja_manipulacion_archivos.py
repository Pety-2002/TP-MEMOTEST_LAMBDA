import os
import datetime

def leer_linea_archivo(archivo, default):
    """
    Devuelve las lineas del archivo
    CREADA POR: JULIETA MARGENATS
    """
    linea = archivo.readline()
    return linea.rstrip().split(',') if linea else default.split(',')

def agregar_linea(linea):
    """
    Agrega el nombre y contraseña del usuario al archivo
    CREADA POR: MILTON FERNANDEZ
    """
    archivo = open ("registro_usuarios.csv","a")
    archivo.write(linea + "\n")
    archivo.close()

def reiniciar_archivo_partidas(REINICIAR_ARCHIV0_PARTIDAS):
    '''
    Reinica el archivo de partidas
    CREADA POR: MILTON FERNANDEZ
    '''
    if  REINICIAR_ARCHIV0_PARTIDAS == 'True':
        os.remove('partidas.csv')

def escritura_archivo_partidas(resultados):
    """
    Registra los resultados de cada partida
    CREADA POR: MILTON FERNANDEZ
    """
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
    partidas.close()


def leer_config():
    '''
    Lee el archivo de configuracion solo 1 vez al iniciar el programa
    CREADA POR : JULIETA MARGENATS 
    Si no tienen los valores prestablecidos, se tienen que configurar lo valores "por defecto" usqra ternario
    '''
    ar_config = open('configuracion.csv', 'r')
    linea = leer_linea_archivo(ar_config, ',')

    cantidad_fichas = [int(linea[1]), 'configuracion'] if linea[1] and (int(linea[1]) % 2 == 0) and (int(linea[1]) < 53) else [8, 'defecto']
    linea = leer_linea_archivo(ar_config, ',')

    max_jugadores = [int(linea[1]), 'configuracion'] if linea[1] else [3, 'defecto']
    linea = leer_linea_archivo(ar_config, ',')

    max_partidas = [int(linea[1]), 'configuracion'] if linea[1] else [2, 'defecto']
    linea = leer_linea_archivo(ar_config, ',')

    reiniciar_ar = [linea[1], 'configuracion'] if linea[1] else ['False', 'defecto']
    ar_config.close()

    return cantidad_fichas, max_jugadores, max_partidas, reiniciar_ar


def resumen_total():
    '''
    Imprime el resumen_total
    Creada por: JULIETA MARGENATS 
    ''' 
    ar_partidas = open('resumen_total.csv', 'r')
    nombre, puntos, intentos = leer_linea_archivo(ar_partidas, ',,')
    dic = {}
    while nombre:
        if nombre not in dic:
            dic[nombre] = [int(puntos), int(intentos)]
        else: 
            dic[nombre][0] += int(puntos)
            dic[nombre][1] += int(intentos)
        nombre, puntos, intentos = leer_linea_archivo(ar_partidas, ',,')
    
    print(f'\nresumen total: \n')
    for clave in dic:
        print(f'Nombre: {clave} \nAciertos: {dic[clave][0]} \nIntentos: {dic[clave][1]}\n-------------')
    ar_partidas.close()
    