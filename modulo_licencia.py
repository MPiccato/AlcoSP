from tkinter import *

class Licencia():


    def __init__(self, ventana):


        self.imageLicence = PhotoImage(file = "mpiccato_licencia.png")


        self.VentLogin = ventana
        self.VentLogin.geometry('580x220+500+300')
        self.VentLogin.title("Licencia PicTrading")
        self.frmimagenlogin=Frame(self.VentLogin)
        self.frmimagenlogin.grid(row = 0, column = 0, padx = 10,sticky = N+W)
        self.imagen = Label(self.frmimagenlogin,image=self.imageLicence)
        self.imagen.grid(row = 0,column =0, padx = 5, pady = 5)
        self.frmlogin = Frame(self.VentLogin)
        self.frmlogin.grid(row=0, column =1, padx = 5, pady = 5)
        self.lblLoginUsuario = Label(self.frmlogin, text = "Producto realizado por Pictrading", font = "Helvetic 18")
        self.lblLoginUsuario.grid(row = 0, column = 0,padx=5,pady =5, sticky = W)
        self.lblLoginPass = Label(self.frmlogin, text ="Copyright, todos los derechos reservados")
        self.lblLoginPass.grid(row=1,column = 0,padx =5, pady = 5, sticky = W)
        self.btnLogin = Button(self.frmlogin, text="Entendido",  width = 20, height = 2, command=self.AceptarLicencia)
        self.btnLogin.grid(row = 2, column =0, padx = 5, pady=5, sticky = W+E)

    def AceptarLicencia(self):

        self.VentLogin.destroy()



if __name__ == "__main__":

    ventana = Tk()
    aplicacion = Licencia(ventana)
    ventana.mainloop()