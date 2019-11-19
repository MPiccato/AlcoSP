import sqlite3
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.dates as mdates


strNombre = ""


MiConexion = sqlite3.connect('ALQUISTA.DB')
miCursor = MiConexion.cursor()





def graficar_datos():
     #veo si la consulta está vacía, sino limpiarla primero


    consulta = ("SELECT * FROM PESOALQUISTA WHERE NROALQUISTA =123")
    
   
   
  

    
    
    miCursor.execute(consulta)
    #miCursor.execute("SELECT * FROM PESOALQUISTA")
  
  
    fechas = []
    pesos = []
    for filas in miCursor.fetchall():
        print("Hola {}, tus fechas y pesos son: {} -> {}".format(filas[0],filas[3],filas[4]))
        fechas.append(filas[3])
        pesos.append(filas[4])

    pesoordenado = zip(fechas,pesos)
    ordenado = sorted(pesoordenado)
    print("Lista ordenada", ordenado)
    fechas,pesos = zip(*ordenado)

    consultaNombre = (consulta)
    miCursor.execute(consultaNombre)
    strNombre = miCursor.fetchone()
    plt.title("Evolución del peso de {} {}".format(strNombre[0],strNombre[1]))
    plt.xlabel("Fechas del peso")
    plt.ylabel("Peso observado")
    plt.plot(fechas,pesos)
    plt.show()
    strNombre=""



    intUltimopeso = pesos[len(pesos)-1]
    intAnteUltimopeso = pesos[len(pesos)-2]
    resultado = intUltimopeso - intAnteUltimopeso
    strFelicitacion = ""
    if resultado <0:
        strFelicitacion = "bajado"
    else:
        strFelicitacion = "subido"

    #Acá va agregado el gráfico con la evolución del peso, quizás en otra función






    fechas = list(fechas)
    pesos = list(pesos)

    print("Has {} de peso".format(strFelicitacion))
    for filas in miCursor.fetchall():
        fechas.remove(filas[3])
        pesos.remove(filas[4])



graficar_datos()
miCursor.close()
MiConexion.close()

