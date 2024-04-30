import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Inicio import *
from RegistrarLogin import *

# Conexion Base de Datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soporte",
)
mycursor = mydb.cursor()


class VentanaLogin:
    
    #Creacion ventana
    def login() :
        login = tk.Tk()
        login.title("LOGIN")
        login.geometry("300x400")
        login.configure(background="DarkOrange")
        
        #Logo
        logo = PhotoImage(file="Imagenes/logo.png").subsample(3)
        Label(login, image=logo,background="DarkOrange").pack(pady=20)
        
        #Frame Digitalizacion
        ventana = LabelFrame(login)
        ventana.pack(pady=10)
        
        #Usuario
        Label(ventana, text="USUARIO",font=("arial",10,"bold")).grid(row=0,column=0,padx=10,pady=10)
        entUsuario = Entry(ventana)
        entUsuario.grid(row=0,column=1,padx=20,pady=10)
        
        #Contraseña
        Label(ventana,text="PASSWORD",font=("arial",10,"bold")).grid(row=1,column=0,padx=10,pady=10)
        entClave = Entry(ventana)
        entClave.grid(row=1,column=1,padx=20,pady=10)
        
        #Iniciar Validacion
        def inicio():
            
            # If de no dejar espacios en blanco
            if (entUsuario.get()=="" or entClave.get()==""):
                messagebox.showinfo("","No deje Espacios en Blanco",parent=login)
            else:
                sql = "SELECT * FROM login WHERE usuario = %s"
                val = (entUsuario.get(),)
                mycursor.execute(sql, val,)
                user = mycursor.fetchone()
                
                sql = "SELECT * FROM login WHERE contraseña = %s"
                val = (entClave.get(),)
                mycursor.execute(sql, val,)
                clave = mycursor.fetchone() 
                
                #Destruir Login e Iniciar la ventana principal
                if user and clave is not None:
                    login.destroy()
                    Principal.Ventana()
                    
                else:
                    messagebox.showinfo("","Usuario o Contraseña Incorrecta",parent=login)    
        
        
        #Boton Entrar
        Button(login, text="INICIO",font=("arial",12,"bold"),fg="navy", command=inicio).place(x=50,y=340)
        
        #Boton Registro
        Button(login,text="REGISTRO",font=("arial",12,"bold"),fg="navy", command= RegistroLogin.inicio).place(x=160,y=340)
        
        login.mainloop()
        
    login()        