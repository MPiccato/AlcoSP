from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import modulo_licencia
import calendar
import time
import datetime
import sqlite3
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
from  matplotlib import style
style.use('fivethirtyeight')



class Inicio():


    db_tabla = 'ALQUISTA.db'
    
    def __init__(self, ventana):

      
      self.txtDatosVar = StringVar()
      self.alquista = IntVar()
      self.DNI = IntVar()
      self.CorregirPesoVar = StringVar()
      self.imagenlogin=PhotoImage(file="login.png")

      #variables validación entrada
      self.strloginNroAlquista = StringVar()
      self.strloginPassAlquista = StringVar()





      #self.txtAlquistaVar= StringVar()
      self.VentPrincipal = Toplevel(ventana)
      self.VentPrincipal.state(newstate='withdraw')
      self.VentPrincipal.title("Alco - Presidencia Roque Sáenz Peña")
      self.VentPrincipal.configure(bg = "white")
      self.VentPrincipal.geometry('480x200+500+300')
      self.VentPrincipal.resizable(width = False, height = False)

#Login al sistema

      self.VentLogin = ventana
      self.VentLogin.geometry('480x180+500+300')
      self.VentLogin.title("Ingreso y Autenticación")
      self.frmimagenlogin=Frame(self.VentLogin)
      self.frmimagenlogin.grid(row = 0, column = 0, sticky = N+W)
      self.imagen = Label(self.frmimagenlogin,image=self.imagenlogin)
      self.imagen.grid(row = 0,column =0, padx = 5, pady = 5)
      self.frmlogin = Frame(self.VentLogin)
      self.frmlogin.grid(row=0, column =1, padx = 5, pady = 5)
      self.lblLoginUsuario = Label(self.frmlogin, text = "Nro Alquista:")
      self.lblLoginUsuario.grid(row = 0, column = 0,padx=5,pady =5, sticky = W)
      self.txtLoginUsuario = Entry(self.frmlogin, textvariable = self.strloginNroAlquista)
      self.txtLoginUsuario.grid(row = 0, column = 1,padx = 5, pady = 5)
      self.lblLoginPass = Label(self.frmlogin, text ="Password:")
      self.lblLoginPass.grid(row=1,column = 0,padx =5, pady = 5, sticky = W)
      self.txtLoginPass=Entry(self.frmlogin,show="*", textvariable = self.strloginPassAlquista)
      self.txtLoginPass.grid(row =1,column =1, padx = 5, pady = 5)
      self.btnLogin = Button(self.frmlogin, text="Entrar",  width = 20, height = 2, command=self.login)
      self.btnLogin.grid(row = 2, column =1, padx = 5, pady=5, columnspan =3, sticky = W+E)


#Menú Principal


      self.barraMenu = Menu(self.VentPrincipal)
      self.VentPrincipal.config(menu = self.barraMenu,width = 300,height = 300)
      self.MenuPrincipal=Menu(self.barraMenu,tearoff = 0)
      self.barraMenu.add_cascade(label = "Alquista", menu = self.MenuPrincipal)
      self.MenuInformes = Menu(self.barraMenu,tearoff = 0)

      self.MenuConfiguracion = Menu(self.barraMenu,tearoff = 0)
      self.MenuLicencia = Menu(self.barraMenu,tearoff = 0)
      self.MenuLicencia.add_command(label = "Información sobre los autores", command = self.Licencia)

  

      self.barraMenu.add_cascade(label = "Informes y estadísticas", menu = self.MenuInformes)
      self.barraMenu.add_cascade(label = "Configuración", menu = self.MenuConfiguracion)
      self.barraMenu.add_cascade(label = "Licencia", menu = self.MenuLicencia)
      self.MenuPrincipal.add_command(label = "Control del peso",state = DISABLED)
      self.MenuPrincipal.add_command(label = "Dar de Alta...", command = self.DardeAlta_alquista)
      self.MenuPrincipal.add_command(label = "Actualizar Alquista...", command = self.Actualizaralquista)
      self.MenuPrincipal.add_separator()
      self.MenuPrincipal.add_command(label="Dar de Baja...", command = self.DardeBaja_Alquista)
      self.MenuPrincipal.add_separator()

      self.MenuPrincipal.add_command(label="Salir",command =self.SalirAplicacion)
      self.MenuConfiguracion.add_command(label = "Agregar o modificar Usuarios/Adms", command = self.ConfigUsuarios)
      
      self.lblfrmDatos =LabelFrame(self.VentPrincipal, text ="Ingrese los datos a consultar o completar:")
      self.lblfrmDatos.config(bg = "white", fg = "orange",font = "Arial 16")
      self.lblfrmDatos.grid(row = 0, column = 0,padx = 5, pady = 5,sticky = W+E)
      self.lblNroAlquista = Label(self.lblfrmDatos, text = "Seleccione número de Alquista/DNI:", bg = "orange", fg = "white")
      self.lblNroAlquista.grid(row= 1, column = 0,padx = 5, pady = 5, sticky = W)
      

  


      #Checkbuttons
      self.chkAlquista = Checkbutton(self.lblfrmDatos, text="Nro. Alquista",command = self.nopuedenlosdos,variable = self.alquista, onvalue = 1, offvalue = 0)
      self.chkDNI = Checkbutton(self.lblfrmDatos, text="Nro. DNI", command = self.nopuedenlosdos,variable = self.DNI, onvalue = 1, offvalue = 0)
      self.chkAlquista.grid(row =1, column =1)
      self.chkDNI.grid(row = 1, column = 2)

      self.lblIngresoDatos = Label(self.lblfrmDatos, text = "Ingrese el número correspondiente: ", bg = "orange", fg = "white")
      self.lblIngresoDatos.grid(row= 2, column = 0,padx = 5, pady = 5,sticky = W)
      
      self.txtDatos = Entry(self.lblfrmDatos, textvariable = self.txtDatosVar)
      self.txtDatos.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)
      self.btnAceptar = Button(self.lblfrmDatos, text="Aceptar", width = 10, height = 2, command = self.validar)
      self.btnAceptar.grid(row=3,column =1,padx = 5,columnspan = 2, sticky = E)
      self.btnCancelar = Button(self.lblfrmDatos, text="Cancelar", width = 10, height = 2, command = lambda: ventana.destroy())
      self.btnCancelar.grid(row=3,column =1,padx = 5,columnspan = 2, sticky = W)

    def nopuedenlosdos(self):
        if self.alquista.get() == 1:
          self.DNI.set(0)
        if self.DNI.get()==1:
          self.alquista.set(0)
    
    
    def validar(self):

      if self.alquista.get() == 1:
        self.parametros = int(self.txtDatosVar.get())
        self.queryNroAlquista = ("SELECT * FROM ALQUISTAS WHERE NROALQUISTA = %s" % self.parametros)
        self.miConexion = sqlite3.connect(self.db_tabla)
        self.miCursor = self.miConexion.cursor()
        self.miCursor.execute(self.queryNroAlquista)
        self.consulta = self.miCursor.fetchone()
        self.VentPrincipal.iconify()
        self.ventanapeso()
        
      
     
      if self.DNI.get() == 1:
        self.parametros = int(self.txtDatosVar.get())
        self.queryNroAlquista = ("SELECT * FROM ALQUISTAS WHERE DNI = %s" % self.parametros)
        self.miConexion = sqlite3.connect(self.db_tabla)
        self.miCursor = self.miConexion.cursor()
        self.miCursor.execute(self.queryNroAlquista)
        self.consulta = self.miCursor.fetchone()
        self.VentPrincipal.iconify()
        self.ventanapeso()
      self.miConexion.commit()
      self.miConexion.close()









    def ConfigUsuarios(self):
      self.strIdUsuarios = StringVar()
      self.strConfigNroAlquista = StringVar()
      self.strNombreUsuario = StringVar()
      self.strPassUsuario = StringVar()
      self.VentConfigUsuarios = Toplevel()

      self.VentConfigUsuarios.resizable(width = False, height = False)
      self.frmConfigUsuarios = LabelFrame(self.VentConfigUsuarios, text = "Dar de Alta un usuario: ")
      self.frmConfigUsuarios.grid(row = 0, column = 0, padx = 2, pady = 2)
      self.lblConfigNroAlquista = Label(self.frmConfigUsuarios, text = "Ingrese el número de Alquista:")
      self.lblConfigNroAlquista.grid(row = 0, column = 0, padx = 2, pady =2, sticky = E)

      self.lblConfigUsuarios = Label(self.frmConfigUsuarios, text = "Ingrese DNI usuario: ")
      self.lblConfigUsuarios.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = E)
      
      
      self.txtConfigNroAlquista = Entry(self.frmConfigUsuarios, textvariable = self.strConfigNroAlquista)
      self.txtConfigNroAlquista.grid(row = 0, column = 1, padx = 2, pady = 2)
      self.txtConfigUsuarios = Entry(self.frmConfigUsuarios, textvariable = self.strNombreUsuario)
      self.txtConfigUsuarios.grid (row = 1, column = 1, padx = 2, pady = 2)
      self.lblConfigUsuariosPass = Label(self.frmConfigUsuarios, text = "Ingrese contraseña:")
      self.lblConfigUsuariosPass.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = E)
      self.txtConfigUsuariosPass = Entry(self.frmConfigUsuarios, textvariable = self.strPassUsuario)
      self.txtConfigUsuariosPass.grid(row = 2, column = 1, padx = 2, pady = 2)
      self.btnAgregarConfigUsuarios = Button(self.frmConfigUsuarios, text ="Agregar...", width = 10, height = 3, command = self.AgregarUsuario)
      self.btnAgregarConfigUsuarios.grid(row = 3, column = 1, padx = 2, pady = 2,  sticky = S + E)
      self.btnAgregarConfigUsuarios = Button(self.frmConfigUsuarios, text ="Cancelar...", width = 10, height = 3,command = lambda: self.VentConfigUsuarios.withdraw())
      self.btnAgregarConfigUsuarios.grid(row = 3, column = 0, padx = 2, pady = 2, sticky = S + E)
      self.txtConfigUsuariosPass.config(justify = "right")
      self.txtConfigUsuarios.config(justify = "right")


    def login(self):
      loginnroalquista = bool()
      loginpass = bool()
      loginnroalquista = False
      loginpass = False
      
      self.miConexion = sqlite3.connect(self.db_tabla)
      self.Cursor = self.miConexion.cursor()
      self.query = ("SELECT * FROM USUARIOS")
      if (self.Cursor.execute(self.query)):
        filas = self.Cursor.fetchall()
        for fila in filas:
          if str(fila[0]) == self.strloginNroAlquista.get():
         
            loginnroalquista = 1 
          if str(fila[2]) == self.strloginPassAlquista.get():
        
            loginpass = 1
      if loginnroalquista == 1 and loginpass == 1:
        self.VentPrincipal.state(newstate = 'normal')
        self.VentLogin.withdraw()
      else:
        messagebox.showinfo("Autenticación","Alguno de los datos ingresados es incorrecto")
      

      self.miConexion.commit()
      self.miConexion.close()

      

      
      
      
      #self.VentPrincipal.state(newstate='normal')
      
      
    

    def Actualizaralquista(self):

      #Armando la ventana
      self.VentLogin.withdraw()
      self.VentPrincipal.iconify()
      self.VentActualizar = Toplevel()
      self.VentPrincipal.resizable(width = False, height = False)
      #self.VentActualizar.geometry('1050x700+100+100')


      self.VentActualizar.title("Actualizar registro Alquista")
      
      
      self.lblActualizarRegistro = LabelFrame(self.VentActualizar, text ="Seleccione el registro a actualizar...")
      self.lblActualizarRegistro.grid(row = 0, column = 0, sticky = N+W)

      
      self.tablaActualizar =ttk.Treeview(self.lblActualizarRegistro, height = 30, columns = ('Nombre', 'Apellido', 'DNI','Fecha de Nacimiento','Fecha de Inicio'))
      self.tablaActualizar.grid(row =1, column = 0, padx = 10, pady = 10, sticky = W+E)
      self.tablaActualizar.heading('#0', text = 'Nombre', anchor = CENTER)
      self.tablaActualizar.heading('#1', text = 'Apellido', anchor = CENTER)
      self.tablaActualizar.heading('#2', text = 'DNI', anchor = CENTER)
      self.tablaActualizar.heading('#3', text = 'Fecha de Nacimiento', anchor = CENTER)
      self.tablaActualizar.heading('#4', text = 'Fecha Inicio')
      self.tablaActualizar.heading('#5', text = "Nro Alquista")

      self.frmBotonesActualizarRegistros = Frame(self.VentActualizar)
      self.frmBotonesActualizarRegistros.grid(row = 2, column = 0, sticky = E)
      self.btnActualizarRegistro = Button(self.frmBotonesActualizarRegistros, text = "Actualizar Registro", width = 20, height = 5)
      self.btnActualizarRegistro.grid(row = 0, column = 0)
      self.btnCancelarActualizarRegistro = Button(self.frmBotonesActualizarRegistros, text = "Cancelar Actualización", width = 20, height = 5, command=lambda : self.VentActualizar.withdraw())
      self.btnCancelarActualizarRegistro.grid(row = 0, column = 1, sticky = E)
      
      #self.btnActualizarRegistro = Button(self.VentActualizar, "Actualizar Registro", width = 10, height =2)
      #self.btnActualizarRegistro.grid(row=2,column =6, columnspan = 2, sticky = S+E)
      
      self.get_productos()



    def AgregarUsuario(self):

      self.miConexion = sqlite3.connect("ALQUISTA.DB")
      self.miCursor = self.miConexion.cursor()
      self.query = ("INSERT INTO USUARIOS VALUES (?,?,?)")

      self.parametros = self.strConfigNroAlquista.get(),self.strNombreUsuario.get(),self.strPassUsuario.get()
      self.miCursor.execute(self.query,self.parametros)  
      self.miConexion.commit()
      self.miConexion.close()  
      messagebox.showinfo("Ingresar Usuario Nuevo", "El usuario fue ingresado correctamente")
      self.VentConfigUsuarios.withdraw()
    
    
    
    def ejecutar_tabla(self,query,parameters = ()):
        with sqlite3.connect(self.db_tabla) as conn:
            cursor = conn.cursor()
            resultado = cursor.execute(query, parameters)
            conn.commit()
        return resultado 


    def get_productos(self):
       
       #veo si la consulta está vacía, sino limpiarla primero
       records = self.tablaActualizar.get_children()
       for element in records:
           self.tablaActualizar.delete(element)


       query =  'SELECT * FROM ALQUISTAS ORDER BY NOMBRE DESC'
       db_filas = self.ejecutar_tabla(query)
       
       #Reflejando los datos en la tabla
       for fila in db_filas:
           self.tablaActualizar.insert('',0, text = fila[0], values = (fila[1],fila[2],fila[3],fila[4]))
    
    
    
    def actualizar_elementos(self, strNombre,strApellido,strDNI,strNroAlquista):
        query = 'UPDATE ALQUISTAS SET NOMBRE = ?, APELLIDO = ?, DNI = ?, NROALQUISTA = ? WHERE NOMBRE = ?, APELLIDO = ?, DNI = ?, NROALQUISTA=?'
        parameters = (strNombre,strApellido,strDNI,strNroAlquista)
        self.ejecutar_tabla(query,parameters)
        self.get_productos()
    
    
    
    def CorregirPeso(self):
      if len(self.CorregirPesoVar.get())!= 0:
        return self.CorregirPesoVar.set("")
      else:
        messagebox.showinfo("Corregir Peso", "No hay nada que corregir")
        

      
    
    def ventanapeso(self):

    
      
      self.dia = StringVar()
      self.dia = StringVar()
      self.VentPrincipal.state(newstate = 'withdraw')
      self.cargadepeso = Toplevel()
      self.cargadepeso.resizable(width = False, height = False)
      self.CorregirPesoVar = StringVar()


      #self.VentPrincipal.iconify()
      self.cargadepeso.title("Vamos a registrar el peso: ")
      self.cargadepeso.geometry('630x260+300+300')
      self.lblimagenbalanza = Label(self.cargadepeso, text = "Qué bueno que estés acá haciendo esto {} {}".format(self.consulta[0],self.consulta[1]), font ="Arial 16", fg= "blue")
      self.lblimagenbalanza.grid(row = 0, column = 0, padx = 10, pady = 10)

      self.frmCargaPeso = LabelFrame(self.cargadepeso, text ="Ahora vamos a anotar tu peso actual")
      self.frmCargaPeso.grid(row =1, column = 0, columnspan = 2,padx = 15,pady = 10)
      self.lblPeso = Label(self.frmCargaPeso,text ="Fecha en la que estás registrando el peso (AAAA-MM-DD):")
      self.lblPeso.grid(row = 1, column = 0, padx = 5, pady = 5)
      self.txtFechaPeso = Entry(self.frmCargaPeso, textvariable = self.dia)
      #self.txtFechaPeso = Entry(self.frmCargaPeso, textvariable = StringVar(value = self.dia.strftime("%d/%b/%Y")))
      self.txtFechaPeso.grid(row = 1, column = 1, padx = 5, pady = 5)
      self.txtFechaPeso.config(justify="right")
      self.lblUltimoPeso = Label(self.frmCargaPeso, text = "Ingresa por favor el peso actual: ")
      self.lblUltimoPeso.grid(row=2,column =0, padx = 5, pady =5,sticky = W)
      self.txtUltimoPeso=Entry(self.frmCargaPeso, textvariable = self.CorregirPesoVar) #La variable CorregirPesoVar es para la carga del peso
      self.txtUltimoPeso.grid(row=2, column =1, padx = 5, pady =5)
      self.txtUltimoPeso.config(justify = "right")
      self.btnAceptarPeso = Button(self.frmCargaPeso, text= "Guardar Peso", command = self.PantallaFelicitacion, width = 10, height = 2)
      self.btnAceptarPeso.grid(row = 3, column = 1, padx = 5, pady = 5,sticky = W+E)
      self.btnCorregirPeso = Button(self.frmCargaPeso, text= "Corregir Peso", width = 10, height = 2,command = self.CorregirPeso)
      self.btnCorregirPeso.grid(row = 3, column = 0, padx = 5, pady = 5,sticky = W+E)
    



    def grafico(self):

      self.cargadepeso.withdraw()

      self.VentFelicitacion.withdraw()

      self.VentGrafico = Toplevel(self.VentFelicitacion)
      self.VentGrafico.title("Evolución gráfica del peso")

      x = np.array(self.fechas)
      y = np.array(self.pesos)

      fig = Figure(figsize=(10,10))
      a=fig.add_subplot(111)
      a.plot(x,y,color='blue')
      #a.plot(p,range(2+max(x)),color='blue')
      #a.invert_yaxis()
      a.set_title("Evolución del peso", fontsize=16)
      a.set_ylabel("Peso", fontsize = 14)
      a.set_xlabel("Fechas", fontsize = 14)

      canvas = FigureCanvasTkAgg(fig, master = self.VentGrafico)
      canvas.get_tk_widget().pack()
      canvas.draw()




    def PantallaFelicitacion(self, *args, **kwargs):


      self.IMC = float
      self.EstIMC = ""


      self.VentFelicitacion = Toplevel()
      self.VentFelicitacion.title("Así van tus avances")
      self.VentFelicitacion.resizable(width = False, height = False)
      self.lblSaludo = Label(self.VentFelicitacion, text="Estadísticas básicas de tu progreso {} {}".format(self.consulta[0],self.consulta[1]), font = 'Arial 16', fg = 'white', bg = 'black')
      self.lblSaludo.grid(row = 0, column = 1, padx = 5, pady = 5)
      self.lblSaludo.config (justify = 'center')

      self.VentFelicitacion.geometry('900x290+300+400')
      self.VentFelicitacion.title("Alco SP")
      self.VentFelicitacion.configure(background = 'black')
      self.imagenAlcoSP=PhotoImage(file="imagenrecortada.png")

      self.imgimagenAlcoSP = Label(self.VentFelicitacion, image = self.imagenAlcoSP, bd = 0)
      self.imgimagenAlcoSP.grid(row = 0, column = 0,rowspan = 6)
      

      self.miConexion=sqlite3.connect(self.db_tabla)
      self.miCursor = self.miConexion.cursor()
      self.query = ("INSERT INTO PESOALQUISTA VALUES (?,?,?,?,?)")
      self.parametros = str(self.consulta[0]), str(self.consulta[1]),str(self.consulta[5]),str(self.dia.get()),int(self.CorregirPesoVar.get())
      self.miCursor.execute(self.query,self.parametros)

      #Cálculo Indice Masa Corporal
      self.IMC = float(self.CorregirPesoVar.get())/float((self.consulta[6])**2)



      self.lblIMC = Label(self.VentFelicitacion, text = "Tu IMC actualizado hasta hoy es {0:.2f}".format(self.IMC))
      self.lblIMC.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)
      self.lblIMC.config(bg = 'black', fg='white', justify = 'center')

      if float(self.IMC) < 18.5:
        self.EstIMC = "más bajo del recomendado"
      if float(self.IMC) >= 18.5 and float(self.IMC) <= 24.9:
        self.EstIMC = "normal"
      if float(self.IMC) >=25 and float(self.IMC) <= 29.9:
        self.EstIMC = "Obesidad I \n(muy pocas complicaciones físicas y mínimo impacto de ánimo)"
      if float(self.IMC) >=30 and float(self.IMC)<=34.9:
        self.EstIMC ="Obesidad II \n(riesgo de diabetes, colesterol, várices, hipertensión, gota)"
      if float(self.IMC)>= 35 and float(self.IMC)<=39.9:
        self.EstIMC = "Obesidad III \n(apnea del sueño, artrosis, hígado graso)"
      if float(self.IMC)>=40 and float(self.IMC)<=49.9:
        self.EstIMC = "Obesidad IV \n(falta de aire, tromboflebitis, eripela)"
      if float(self.IMC)>=50 and float(self.IMC)<=64.9:
        self.EstIMC = "Obesidad V \n(Problemas de hemorroides, complicaciones cardíacas)"
      if float(self.IMC)>= 65 and float(self.IMC)<= 79.9:
        self.EstIMC = "Obesidad VI \n(Discapacidad severa)"
      if float(self.IMC)>=80 and float(self.IMC)<=99.9:
        self.EstIMC = "Obesidad VII \n(úlceras en piernas, escaras)"
      if float(self.IMC) >= 100:
        self.EstIMC = "Postración. Deterioro de funciones vitales"
    



      
      


      self.lblExplicacionIMC = Label(self.VentFelicitacion, text = "Ese IMC implica que tu peso es {}".format(self.EstIMC))
      self.lblExplicacionIMC.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)
      self.lblExplicacionIMC.config(fg = 'white',bg = 'black',justify = 'center')
      #self.lblFelicitacion = Label(self.VentFelicitacion, text=("Has {} {} kilos".format(self.strFelicitacion,abs(self.resultado))))
      #self.lblFelicitacion.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = W)

      self.miConexion.commit()
      self.miConexion.close()

      self.miConexion=sqlite3.connect(self.db_tabla)
      self.miCursor = self.miConexion.cursor()
      self.query = ("SELECT * FROM PESOALQUISTA WHERE NROALQUISTA =" + self.txtDatosVar.get())
      self.miCursor.execute(self.query)
      
      
      
      self.fechas = []
      self.pesos =[]
      self.datos = self.miCursor.fetchall()
      for self.filas in self.datos:
        self.fechas.append(self.filas[3])
        self.pesos.append(self.filas[4])

      #Ordenando por fechas para después hacer el gráfico y comparar pesos

      self.pesoordenado = zip(self.fechas,self.pesos)
      self.ordenado = sorted(self.pesoordenado)
      print("Lista ordenada", self.ordenado)
      self.fechas,self.pesos = zip(*self.ordenado)

      #calculando evolución de los pesos
      self.UltPeso = self.pesos[len(self.pesos)-1]
      self.AnteultPeso = self.pesos[len(self.pesos)-2]
      self.resultado = self.UltPeso - self.AnteultPeso
      self.strFelicitacion = ''
      if self.resultado <0:
        self.strFelicitacion = "¡Felicidades! Has bajado de peso"
      if self.resultado > 0:
        self.strFelicitacion = "No bajaste de peso, pero no te aflijas"
      if self.resultado == 0:
        self.strFelicitacion = "Mantuviste el peso, sigue así"

      self.lblPeso = Label(self.VentFelicitacion, text = "{}".format(self.strFelicitacion))
      self.lblPeso.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = W+E)
      self.lblPeso.config(fg = 'blue',bg = 'white',justify = 'center',font = "Helvetic 20")

      self.btnMostrarGrafico = Button(self.VentFelicitacion, text ="Quiero ver el gráfico", command = self.grafico)
      self.btnMostrarGrafico.config(width = 10, height = 6)
      self.btnMostrarGrafico.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = W+E)




      self.fechas = list(self.fechas)
      self.pesos = list(self.pesos)

  
      for self.filas in self.miCursor.fetchall():
        self.fechas.remove(self.filas[3])
        self.pesos.remove(self.filas[4])




      
      
      self.miCursor.close()
      self.miConexion.close()
     


  
      




   

      





      












    def DarAltaAlquistaDB(self):

      self.miConexion = sqlite3.connect("ALQUISTA.db")
      self.miCursor = self.miConexion.cursor()
      self.datos = self.strNombre.get(),self.strApellido.get(),self.strDNI.get(),self.strFechaNacimiento.get(),self.strFechaInicio.get(),self.strNroAlquista.get(),self.strAltura.get()
      self.miCursor.execute("INSERT INTO ALQUISTAS VALUES (?,?,?,?,?,?,?)",self.datos)
      self.miConexion.commit()
      self.miConexion.close()
      messagebox.showinfo("Base de Datos", "Registro insertado con éxito")
    
    
    def ActualizarAlquistaDB(self):
      pass





  
    
    def DardeAlta_alquista(self):
      """Aquí van las ventanas y datos necesarios para realizar el alta de los 
      clientes"""
      self.strId = StringVar()
      self.strNombre = StringVar()
      self.strApellido = StringVar()
      self.strDNI = StringVar()
      self.strFechaNacimiento = StringVar()
      self.strFechaInicio = StringVar()
      self.strNroAlquista = StringVar()
      self.strAltura=StringVar()
      

      self.alta_alquista = Toplevel()
      self.VentPrincipal.iconify()
      self.alta_alquista.geometry('500x550+500+200')
      self.frmalta_alquista = LabelFrame(self.alta_alquista, text = "Alta de Alquista")
      self.alta_alquista.title('Alta de Alquista en Sáenz Peña')
      self.frmalta_alquista.grid(row = 0, column = 0, padx = 5, pady = 5)
      #carga de datos
      ##Nombre
      self.lblNombre = Label(self.frmalta_alquista,text="Ingrese su Nombre: ")
      self.lblNombre.grid(row = 0, column = 0,sticky = W)
      self.txtNombre = Entry(self.frmalta_alquista, textvariable = self.strNombre)
      self.txtNombre.grid(row = 0, column = 1)

      ##Apellido
      self.lblApellido = Label(self.frmalta_alquista,text="Ingrese su Apellido: ")
      self.lblApellido.grid(row = 1, column = 0,sticky = W)
      self.txtApellido = Entry(self.frmalta_alquista,textvariable = self.strApellido)
      self.txtApellido.grid(row = 1, column = 1)

      ##DNI

      self.lblDNI = Label(self.frmalta_alquista,text="Ingrese su DNI: ")
      self.lblDNI.grid(row = 2, column = 0,sticky = W)
      self.txtDNI = Entry(self.frmalta_alquista,textvariable = self.strDNI)
      self.txtDNI.grid(row = 2, column = 1)

      ##Fecha de Nacimiento
      self.lblFechaNacimiento = Label(self.frmalta_alquista,text="Ingrese Fecha de Nacimiento (dd/mm/aaaa): ")
      self.lblFechaNacimiento.grid(row = 3, column = 0,sticky = W)
      self.txtFechaNacimiento = Entry(self.frmalta_alquista,textvariable = self.strFechaNacimiento)
      self.txtFechaNacimiento.grid(row = 3, column = 1)

      #Agregar etiqueta Altura variable = strAltura
      self.lblAltura = Label(self.frmalta_alquista,text="Ingrese la altura por favor: ")
      self.lblAltura.grid(row =4, column = 0, pady = 10, sticky = W)
      self.txtAltura = Entry(self.frmalta_alquista, textvariable=self.strAltura)
      self.txtAltura.grid(row = 4, column = 1)

      ##Etiqueta Administrador
      self.lblAdministrador = Label(self.frmalta_alquista, text = "Para que completen administradores: ")
      self.lblAdministrador.grid(row =5, column = 0, pady = 10, sticky = W)
      ##datos carga Administrador
      self.lblFechaInicio = Label(self.frmalta_alquista, text = "Ingrese fecha de Inicio: ")
      self.lblFechaInicio.grid(row = 6, column = 0, sticky = W)
      self.txtFechaInicio = Entry(self.frmalta_alquista,textvariable = self.strFechaInicio)
      self.txtFechaInicio.grid( row = 6, column = 1)
      self.lblNroAlquista = Label(self.frmalta_alquista, text="Ingrese número de Alquista: ")
      self.lblNroAlquista.grid(row = 7, column = 0, sticky = W)
      self.txtNroAlquista = Entry(self.frmalta_alquista,textvariable = self.strNroAlquista)
      self.txtNroAlquista.grid(row = 7, column = 1)

      self.frmBotones = Frame(self.alta_alquista)
      self.frmBotones.grid(row =2, column = 0)
      self.btnCrear = Button(self.frmBotones, text="Insertar Registro",command = self.DarAltaAlquistaDB)
      self.btnCrear.grid(row =0,column = 0, pady = 10,padx = 10)
      #self.btnLeer = Button(self.frmBotones,text="Leer")
      #self.btnLeer.grid(row = 0, column = 1, pady = 10,padx = 10)
      self.btnActualizar = Button(self.frmBotones,text="Actualizar", command = self.ActualizarAlquistaDB)
      self.btnActualizar.grid(row =0, column = 3, pady =10,padx = 10)
      #self.btnBorrar = Button(self.frmBotones,text="Borrar")
      #self.btnBorrar.grid(row = 0,column = 4,pady = 10,padx = 10)
    
    def DardeBaja_Alquista(self):
      """Dar de baja un Alquista después de haber faltado a 4 reuniones consecutivas"""
      
      self.baja_alquista = Toplevel()
      self.VentPrincipal.iconify()
      self.baja_alquista.geometry('460x380+500+200')
      self.baja_alquista.resizable(width = False, height = False)
      self.frmbaja_alquista = LabelFrame(self.baja_alquista, text = "Baja de Alquista")
      self.baja_alquista.title('Baja de Alquista en Sáenz Peña')
      self.frmbaja_alquista.grid(row = 0, column = 0, padx = 5, pady = 5)

      #Cuadro de consulta de la baja
      self.lblBaja = Label(self.baja_alquista,text="Ingrese el número de Alquista: ")
      self.lblBaja.grid(row = 0, column = 0, sticky = W, padx = 5, pady = 5)
      self.txtBaja = Entry(self.baja_alquista)
      self.txtBaja.grid(row = 0, column = 1, padx = 5, pady = 5)

      self.btnBaja = Button(self.baja_alquista, text = "Confirmar la baja")
      self.btnBaja.grid(row = 1, column = 1,padx = 5, pady = 5)
      self.btnBajaCancelar = Button(self.baja_alquista, text = "Cancelar la baja")
      self.btnBajaCancelar.grid(row = 1, column = 0,padx = 5, pady = 5)
      













    






    def Licencia(self):

        self.imageLicence = PhotoImage(file = "mpiccato_licencia.png")

        


        self.VentLicencia = Toplevel()
        self.VentLicencia.geometry('580x240+500+300')
        self.VentLicencia.resizable(width = False, height = False)
        self.VentLicencia.title("Licencia PicTrading")
        self.frmimagenlogin=Frame(self.VentLicencia)
        self.frmimagenlogin.grid(row = 0, column = 0, padx = 10,sticky = N+W)
        self.imagen = Label(self.frmimagenlogin,image=self.imageLicence)
        self.imagen.grid(row = 0,column =0, padx = 5, pady = 5)
        self.frmlogin = Frame(self.VentLicencia)
        self.frmlogin.grid(row=0, column =1, padx = 5, pady = 5)
        self.lblLoginUsuario = Label(self.frmlogin, text = "Producto realizado por Pictrading", font = "Helvetic 18")
        self.lblLoginUsuario.grid(row = 0, column = 0,padx=5,pady =5, sticky = W)
        self.lblLoginPass = Label(self.frmlogin, text ="Copyright, todos los derechos reservados")
        self.lblLoginPass.grid(row=1,column = 0,padx =5, pady = 5, sticky = W)
        self.btnLogin = Button(self.frmlogin, text="Entendido",  width = 20, height = 2, command=lambda : self.VentLicencia.destroy())
        self.btnLogin.grid(row = 2, column =0, padx = 5, pady=5, sticky = W+E)



    def SalirAplicacion(self):
      salir=messagebox.askokcancel("Alco","¿Está seguro que desea salir de la Aplicación?")
      if salir == True:
        sys.exit()

    
        











if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Inicio(ventana)
    ventana.mainloop()
