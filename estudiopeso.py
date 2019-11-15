from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



"""Generar el cuadro que muestre los gráficos de evolución del peso.
estudiar los pesos de los alquistas
Generar el cuadro que muestre la evolución del IMC

Necesito la BBDD de historial de peso

Voy a generar una base de datos falsa para hacer las pruebas PRUEBAPESO.DB
Campos requeridos: NOMBRE, APELLIDO, DNI, NROALQUISTA, PESO """

class EstPeso():

    def __init__(self, VentPeso):


        self.VentPesoPpal = VentPeso
        self.VentPesoPpal.geometry('800x800+100+100')
        self.VentPesoPpal.title("Informe de evolución del peso")

        #Construyendo los cuadros de información
        self.frmInfPpal = Frame(self.VentPesoPpal)
        self.frmInfPpal.grid(row = 0, column = 0, padx = 10, pady = 10, ipadx = 5,ipady=5)
        self.lblInfAlquista = Label(self.frmInfPpal, text="Esta es tu información actualizada: {}".format("Martin Piccato"))
        self.lblInfAlquista.grid (row = 0, column = 0, padx = 5, pady = 5, sticky = W)

        #self.txtInfNombreAlquista = Entry(self.frmInfPpal)
        #self.txtInfNombreAlquista.config(state = 'readonly')
        #self.txtInfNombreAlquista.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.graficaAlquista()


    def graficaAlquista(self):
        x = np.linspace(0,2) #Acá van los datos
        plt.plot(x,x,label = "Gráfico lineal")
        plt.plot(x,x**2, label="línea al cuadrado")
        plt.plot(x,x**3, label = "Línea al cubo")

        plt.xlabel('Fecha de peso')
        plt.ylabel('Kg. Observados')

        plt.title('Gráfico simple')
        plt.legend()
        plt.show()

       


   


if __name__ == '__main__':
    VentPeso = Tk()
    AppPeso = EstPeso(VentPeso)
    VentPeso.mainloop()