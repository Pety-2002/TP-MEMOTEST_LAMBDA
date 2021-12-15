import os
import datetime

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
    for j in range (len(resultados)):
        archivo = open("partidas.csv", "a")
        fecha = datetime.datetime.now()
        fecha_de_partida = fecha.strftime('%d/%m/%Y')
        hora_de_finalizacion = fecha.strftime('%H:%M:%S')
        nombre=str(resultados[j][NOMBRE])
        puntos=str(resultados[j][TUPLA_DATOS][PUNTOS])
        intentos=str(resultados[j][TUPLA_DATOS][INTENTOS])
        promedio_intentos=str(resultados[j][TUPLA_DATOS][INTENTOS]//len(resultados))
        
        archivo.write(f"{fecha_de_partida},{hora_de_finalizacion},{nombre},{puntos},{intentos},{promedio_intentos}\n")

def reiniciar_archivo_partidas(REINICIAR_ARCHIV0_PARTIDAS):
    '''
    Creada por: Milton Fernández
    '''
    if REINICIAR_ARCHIV0_PARTIDAS == 'True':
        os.remove('partidas.csv')
        