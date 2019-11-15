import sqlite3
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


strNombre = ""


MiConexion = sqlite3.connect('ALQUISTA.DB')
miCursor = MiConexion.cursor()




def graficar_datos():
     #veo si la consulta está vacía, sino limpiarla primero
  

    miCursor.execute("SELECT * FROM PESOALQUISTA WHERE NROALQUISTA = 120 ORDER BY FECHAPESO")
    #miCursor.execute("SELECT * FROM PESOALQUISTA")
  
    fechas = []
    pesos = []
    for filas in miCursor.fetchall():
        print("Hola {}, tus fechas y pesos son: {} -> {}".format(filas[0],filas[3],filas[4]))
        fechas.append(filas[3])
        pesos.append(filas[4])

    
    #plt.title("Evolución del peso de {} {}".format(strNombre[0],strNombre[1]))
    plt.xlabel("Fechas del peso")
    plt.ylabel("Peso observado")
    plt.plot(fechas,pesos)
    plt.show()



graficar_datos()
miCursor.close()
MiConexion.close()

