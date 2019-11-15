import sqlite3
import time
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates



MiConexion = sqlite3.connect('ALQUISTA.DB')
miCursor = MiConexion.cursor()

def graficar_datos():
    miCursor.execute("SELECT * FROM PESOALQUISTA ORDER BY FECHAPESO ASC")
    #miCursor.execute("SELECT * FROM PESOALQUISTA")
    fechas = []
    pesos = []
    for filas in miCursor.fetchall():
        print("Hola {}, tus fechas y pesos son: {} -> {}".format(filas[0],filas[3],filas[4]))
        fechas.append(filas[3])
        pesos.append(filas[4])
    plt.plot(fechas,pesos)
    plt.show()



graficar_datos()
miCursor.close()
MiConexion.close()

