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


class RegistroLogin:

    # Creacion ventana
    def inicio():
        inicio = tk.Tk()
        inicio.title("")
        inicio.geometry("350x400")
        Label(inicio, text="LOGIN REGISTRO", font=(
            "arial20", 17, "bold"), fg="green").place(x=70, y=20)

        # Frame Digitalizacion
        ventana = LabelFrame(inicio)
        ventana.grid(row=0, column=0, pady=80, padx=20)

        # Nombre Completo
        Label(ventana, text="Nombre Completo", font=("arial", 10, "bold")).grid(
            row=0, column=0, padx=10, pady=10)
        entNombre = Entry(ventana)
        entNombre.grid(row=0, column=1, padx=20, pady=10)

        # Identificacion
        Label(ventana, text="Identificacion", font=("arial", 10, "bold")).grid(
            row=1, column=0, padx=10, pady=10)
        entIdenti = Entry(ventana)
        entIdenti.grid(row=1, column=1, padx=20, pady=10)

        # Cargo
        Label(ventana, text="Cargo", font=("arial", 10, "bold")).grid(
            row=2, column=0, padx=10, pady=10)
        entCargo = Entry(ventana)
        entCargo.grid(row=2, column=1, padx=20, pady=10)

        # Usuario
        Label(ventana, text="Usuario", font=("arial", 10, "bold")).grid(
            row=3, column=0, padx=10, pady=10)
        entUsuario = Entry(ventana)
        entUsuario.grid(row=3, column=1, padx=20, pady=10)

        # Contraseña
        Label(ventana, text="Constraseña", font=("arial", 10, "bold")).grid(
            row=4, column=0, padx=10, pady=10)
        entClave = Entry(ventana)
        entClave.grid(row=4, column=1, padx=20, pady=10)

        # Fecha
        fecha = datetime.datetime.now()
        fechaMysql = fecha.strftime("%Y-%m-%d %H:%M:%S")

        def Insertar():
            if (entNombre.get() == "" or entIdenti.get() == "" or entCargo.get() == "" or entUsuario.get() == "" or entClave.get() == ""):
                messagebox.showinfo(
                    "", "No deje Espacios en Blanco", parent=inicio)
            else:
                sql = "INSERT INTO login VALUES (null,%s,%s,%s,%s,%s,%s)"
                val = (entIdenti.get(), entNombre.get(), entCargo.get(), entUsuario.get(),
                       entClave.get(), fechaMysql,)

                mycursor.execute(sql, val,)

                mydb.commit()
                mycursor.rowcount

                # Ventana de registro exitoso
                messagebox.showinfo("", "REGISTRO EXITOSO", parent=inicio)

                # limpiar los datos
                entIdenti.delete(0, END)
                entNombre.delete(0, END)
                entCargo.delete(0, END)
                entUsuario.delete(0, END)
                entClave.delete(0, END)

        # Boton Registro
        Button(inicio, text="REGISTRO", font=("arial", 12, "bold"),
               fg="green", command=Insertar).place(x=40, y=330)

        # Boton Salir
        Button(inicio, text="SALIR", font=("arial", 12, "bold"),
               fg="green", command= inicio.destroy).place(x=210, y=330)

        inicio.mainloop()
