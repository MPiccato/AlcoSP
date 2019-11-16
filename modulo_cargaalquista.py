from tkinter import *
import sqlite3

VentanaCarga = Tk()

def VentanaPrincipal():

    VentanaCarga.title("Módulo de carga de información del Alquista")
    VentanaCarga.geometry('700x500+100+100')

    #Contenedor para ficha Alquista
    frmDatosAlquista = Frame(VentanaCarga)
    frmDatosAlquista.grid(row = 0, column = 0, padx = 5, pady = 5)

    #Labels y textos de los Alquistas

    lblNombre = Label(frmDatosAlquista, text="Ingrese el nombre del Alquista:")
    lblNombre.grid(row = 0, column = 0, padx = 2, pady = 5, sticky = W)
    
    lblApellido = Label(frmDatosAlquista, text="Ingrese el apellido del Alquista:")
    lblApellido.grid(row = 1, column = 0, padx = 2, pady = 5, sticky = W)

    lblDNI = Label(frmDatosAlquista, text="Ingrese el DNI del Alquista:")
    lblDNI.grid(row = 2, column = 0, padx = 2, pady = 5, sticky = W)

    lblFechaNacimiento = Label(frmDatosAlquista, text="Ingrese la fecha de nacimiento del Alquista:")
    lblFechaNacimiento.grid(row = 3, column = 0, padx = 2, pady = 5, sticky = W)

    lblAltura = Label(frmDatosAlquista, text="Ingrese la altura del Alquista:")
    lblAltura.grid(row = 4, column = 0, padx = 2, pady = 5, sticky = W)

    lbltelefono = Label(frmDatosAlquista, text="Ingrese el número de teléfono celular  del Alquista:")
    lbltelefono.grid(row = 5, column = 0, padx = 2, pady = 5, sticky = W)

    frmInfAdm = LabelFrame(frmDatosAlquista, text="Información a ser cargada por el coordinador")
    frmInfAdm.grid(row = 6, column = 0, padx = 2, pady = 15, sticky = W)

    lblFechaInicio = Label(frmInfAdm, text="Ingrese la fecha de inicio del Alquista:")
    lblFechaInicio.grid(row = 7, column = 0, padx = 2, pady = 5, sticky = W)




VentanaPrincipal()







VentanaCarga.mainloop()
