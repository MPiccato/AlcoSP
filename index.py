from tkinter import *
from tkinter import messagebox

inicio = Tk()
inicio.title("Alco - Sáenz Peña")

#mensaje de aviso que funciona
def funciona():
    funcionamiento = messagebox.askokcancel("Mensaje de aviso", "Esto está funcionando")
    if funcionamiento == True:
        inicio.destroy()



#configurar menus
barraMenu = Menu(inicio)
inicio.config(menu = barraMenu,width = 300,height = 300)
MenuPrincipal=Menu(barraMenu,tearoff = 0)
barraMenu.add_cascade(label = "Alquista", menu = MenuPrincipal)
MenuInformes = Menu(barraMenu,tearoff = 0)

MenuAyuda = Menu(barraMenu,tearoff = 0)
MenuLicencia = Menu(barraMenu,tearoff = 0)

barraMenu.add_cascade(label = "Informes y estadísticas", menu = MenuInformes)
barraMenu.add_cascade(label = "Ayuda", menu = MenuAyuda)
barraMenu.add_cascade(label = "Licencia", menu = MenuLicencia)
MenuPrincipal.add_command(label = "Control del peso",command = funciona)




inicio.mainloop()