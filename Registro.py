import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import datetime

# Conexion Base de Datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soporte",
)
mycursor = mydb.cursor()


class VentanaRegistro:
    
    # Creacion de la ventana registro
    def Registro():
        registro = tk.Tk()
        registro.title("")
        registro.geometry("440x520")
        Label(registro, text="REGISTRAR ORDEN", font=(
            "arial20", 20,"bold"), fg="navy").place(x=80, y=40)
        
       
        # Ventana Registro
        ventana = LabelFrame(registro)
        ventana.grid(row=0, column=0, padx=50, pady=100)
        
        # Ingreso Dispositivo
        Label(ventana, text="Dispositivo:", font=("arial", 13)).grid(
            row=0, column=0, padx=20, pady=20)
        entDispositivo = Entry(ventana, width=20)
        entDispositivo.grid(row=0, column=1, padx=20, pady=20)

        # Ingreso Servicio
        Label(ventana, text="Tipo de Servicio:", font=("arial", 13)).grid(
            row=1, column=0, padx=20)
        entServicio = Entry(ventana, width=20)
        entServicio.grid(row=1, column=1, padx=20)

        # Ingreso Falla
        Label(ventana, text="Falla Reportada:", font=("arial", 13)).grid(
            row=2, column=0, padx=20, pady=20)
        entFalla = Entry(ventana, width=20)
        entFalla.grid(row=2, column=1, padx=20, pady=20)

        # Ingreso Cliente
        Label(ventana, text="Cliente:", font=("arial", 13)).grid(
            row=3, column=0, padx=20)
        entCliente = Entry(ventana, width=20)
        entCliente.grid(row=3, column=1, padx=20)

        # Ingreso Telefono
        Label(ventana, text="Telefono:", font=("arial", 13)).grid(
            row=4, column=0, padx=20, pady=20)
        entTelefono = Entry(ventana, width=20)
        entTelefono.grid(row=4, column=1, padx=20, pady=20)

        # Ingreso Diagnostico
        Label(ventana, text="Diagnostico:", font=("arial", 13)).grid(
            row=5, column=0, padx=20)
        entDiagnostico = Entry(ventana, width=20)
        entDiagnostico.grid(row=5, column=1, padx=20)

        # Ingeso Precio
        Label(ventana, text="Precio:", font=("arial", 13)).grid(
            row=6, column=0, padx=20, pady=20)
        entPrecio = Entry(ventana, width=20)
        entPrecio.grid(row=6, column=1, padx=20, pady=20)

        # Fecha
        fecha = datetime.datetime.now()
        fechaMysql = fecha.strftime("%Y-%m-%d %H:%M:%S")
            
        # Base de datos Registro
        def Insertar():
            if (entDispositivo.get()=="" or entServicio.get()=="" or entCliente.get()=="" or entTelefono.get()==""):
                messagebox.showinfo("","No dejar Casillas Vacias",parent=registro)
            else: 
                sql = "INSERT INTO ordenes VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (entDispositivo.get(), entServicio.get(), entFalla.get(), entCliente.get(),
                    entTelefono.get(), entDiagnostico.get(), entPrecio.get(), fechaMysql)

                mycursor.execute(sql, val,)

                mydb.commit()
                mycursor.rowcount

                # Ventana de registro exitoso
                messagebox.showinfo("", "REGISTRO EXITOSO",parent=registro)

                # limpiar los datos
                entDispositivo.delete(0, END)
                entServicio.delete(0, END)
                entFalla.delete(0, END)
                entCliente.delete(0, END)
                entTelefono.delete(0, END)
                entDiagnostico.delete(0, END)
                entPrecio.delete(0, END)
            

        # Boton de Ingresar parametros
        Button(registro, text="Ingreso", font=(
            "arial", 13, "bold"), fg="green", command=Insertar).place(x=90, y=460)

        # Cerrar registro
        Button(registro, text="Cerrar Ventana", font=(
            "arial", 13, "bold"), fg="green", command=registro.destroy).place(x=230, y=460)

        ventana.mainloop()
