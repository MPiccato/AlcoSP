from tkinter import *



VentFelicitacion = Tk()
VentFelicitacion.geometry('700x290+500+300')
VentFelicitacion.resizable(width = False, height = False)
VentFelicitacion.title("Alco SP")
VentFelicitacion.configure(background = 'black')
imagenAlcoSP=PhotoImage(file="imagenrecortada.png")

imgimagenAlcoSP = Label(VentFelicitacion, image = imagenAlcoSP, bd = 0)
imgimagenAlcoSP.grid(row = 0, column = 0)

imgimagenAlcoSP.grid(row = 0, column = 0)
frmcajafelicitacion = Label(VentFelicitacion, text = "Acá va la info")


VentFelicitacion.mainloop()    