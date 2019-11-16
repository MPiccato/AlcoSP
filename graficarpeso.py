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

    consulta = ("SELECT * FROM PESOALQUISTA WHERE NROALQUISTA = 123 ORDER BY FECHAPESO")
    
   
   
  

    
    
    miCursor.execute(consulta)
    #miCursor.execute("SELECT * FROM PESOALQUISTA")
  
  
    fechas = []
    pesos = []
    for filas in miCursor.fetchall():
        print("Hola {}, tus fechas y pesos son: {} -> {}".format(filas[0],filas[3],filas[4]))
        fechas.append(filas[3])
        pesos.append(filas[4])

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






    

    print("Has {} de peso".format(strFelicitacion))
    for filas in miCursor.fetchall():
        fechas.remove(filas[3])
        pesos.remove(filas[4])



graficar_datos()
miCursor.close()
MiConexion.close()

