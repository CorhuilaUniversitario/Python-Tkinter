import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class VentanaModifcar:

    # Ventana Modificar
    def modificar():
        
        # Conexion Base de Datos
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="soporte",
        )
        mycursor = mydb.cursor()
        
        modificar = tk.Tk()
        modificar.title("")
        modificar.geometry("1105x670")
        Label(modificar, text="MODIFICAR ORDEN", font=(
            "arial20", 20,"bold"), fg="orange").place(x=420, y=5)

        # Ventana Registro
        cambiar = LabelFrame(modificar)
        cambiar.grid(row=0, column=0, padx=50, pady=60)

        # Ingreso ID
        Label(cambiar, text="ID:", font=("arial", 13)).grid(
            row=0, column=0, padx=20)
        entID = Entry(cambiar, width=20)
        entID.grid(row=0, column=1, padx=20)

        # Ingreso Dispositivo
        Label(cambiar, text="Dispositivo:", font=("arial", 13)).grid(
            row=1, column=0, padx=20, pady=10)
        entDispositivo = Entry(cambiar, width=20)
        entDispositivo.grid(row=1, column=1, padx=20, pady=10)

        # Ingreso Servicio
        Label(cambiar, text="Tipo de Servicio:", font=("arial", 13)).grid(
            row=2, column=0, padx=20)
        entServicio = Entry(cambiar, width=20)
        entServicio.grid(row=2, column=1, padx=20)

        # Ingreso Falla
        Label(cambiar, text="Falla Reportada:", font=("arial", 13)).grid(
            row=3, column=0, padx=20, pady=10)
        entFalla = Entry(cambiar, width=20)
        entFalla.grid(row=3, column=1, padx=20, pady=10)

        # Ingreso Cliente
        Label(cambiar, text="Cliente:", font=("arial", 13)).grid(
            row=4, column=0, padx=20)
        entCliente = Entry(cambiar, width=20)
        entCliente.grid(row=4, column=1, padx=20)

        # Ingreso Telefono
        Label(cambiar, text="Telefono:", font=("arial", 13)).grid(
            row=5, column=0, padx=20, pady=10)
        entTelefono = Entry(cambiar, width=20)
        entTelefono.grid(row=5, column=1, padx=20, pady=10)

        # Ingreso Diagnostico
        Label(cambiar, text="Diagnostico:", font=("arial", 13)).grid(
            row=6, column=0, padx=20)
        entDiagnostico = Entry(cambiar, width=20)
        entDiagnostico.grid(row=6, column=1, padx=20)

        # Ingeso Precio
        Label(cambiar, text="Precio:", font=("arial", 13)).grid(
            row=7, column=0, padx=20, pady=10)
        entPrecio = Entry(cambiar, width=20)
        entPrecio.grid(row=7, column=1, padx=20, pady=10)

        # Mostrar Tabla
        tabla = LabelFrame(modificar, padx=20, pady=20)
        tabla.grid(row=1, column=0, padx=30)
        arbol = ttk.Treeview(tabla, columns=("ID", "DISPOSITIVO", "TIPO DE SERVICIO", "FALLA",
                                             "CLIENTE", "TELEFONO", "DIAGNOSTICO", "PRECIO", "FECHA"), show="headings", height=7,)
        arbol.column("#1", width=40, anchor=CENTER)
        arbol.heading("#1", text="ID")
        arbol.column("#2", width=100, anchor=CENTER)
        arbol.heading("#2", text="DISPOSITIVO")
        arbol.column("#3", width=150, anchor=CENTER)
        arbol.heading("#3", text="TIPO DE SERVICIO")
        arbol.column("#4", width=100, anchor=CENTER)
        arbol.heading("#4", text="FALLA")
        arbol.column("#5", width=100, anchor=CENTER)
        arbol.heading("#5", text="CLIENTE")
        arbol.column("#6", width=90, anchor=CENTER)
        arbol.heading("#6", text="TELEFONO")
        arbol.column("#7", width=190, anchor=CENTER)
        arbol.heading("#7", text="DIAGNOSTICO")
        arbol.column("#8", width=90, anchor=CENTER)
        arbol.heading("#8", text="PRECIO")
        arbol.column("#9", width=140, anchor=CENTER)
        arbol.heading("#9", text="FECHA")
        arbol.pack()

        # Mostrar los parametros en la tabla
        def mostrar():

            mycursor.execute("SELECT * FROM ordenes")

            myresult = mycursor.fetchall()
            mydb.commit()
            mydb.close()

            return myresult

        for row in mostrar():
            arbol.insert("", "end", values=row)


        # Selecionar El parametro
        def seleccion(event):
            punto = arbol.focus()

            if punto:

                values = arbol.item(punto)['values']
                entID.delete(0, END)
                entID.insert(0, values[0])
                entDispositivo.delete(0, END)
                entDispositivo.insert(0, values[1])
                entServicio.delete(0, END)
                entServicio.insert(0, values[2])
                entFalla.delete(0, END)
                entFalla.insert(0, values[3])
                entCliente.delete(0, END)
                entCliente.insert(0, values[4])
                entTelefono.delete(0, END)
                entTelefono.insert(0, values[5])
                entDiagnostico.delete(0, END)
                entDiagnostico.insert(0, values[6])
                entPrecio.delete(0, END)
                entPrecio.insert(0, values[7])

        arbol.bind("<<TreeviewSelect>>", seleccion)
        

        # Insertar Nuevos parametros
        def Insertar():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="soporte",
            )
            mycursor = mydb.cursor()

            sql = "UPDATE ordenes SET dispositivo = %s, servicio = %s, falla = %s, cliente = %s, telefono = %s, diagnostico = %s, precio = %s  WHERE id = %s"
            val = (entDispositivo.get(),entServicio.get(),entFalla.get(),entCliente.get(),entTelefono.get(),entDiagnostico.get(),entPrecio.get(),entID.get())

            mycursor.execute(sql, val,)

            mydb.commit()
            mycursor.rowcount

            # Ventana de registro exitoso
            messagebox.showinfo("", "MODIFICACION EXITOSA", parent=modificar)

            # limpiar los datos
            entID.delete(0, END)
            entDispositivo.delete(0, END)
            entServicio.delete(0, END)
            entFalla.delete(0, END)
            entCliente.delete(0, END)
            entTelefono.delete(0, END)
            entDiagnostico.delete(0, END)
            entPrecio.delete(0, END)

            # Recargar los datos cambiados
            arbol.delete(*arbol.get_children())

            def mostrar():
                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM ordenes")

                myresult = mycursor.fetchall()
                mydb.commit()
                mydb.close()

                return myresult

            for row in mostrar():
                arbol.insert("", "end", values=row)

        # Boton de Ingresar parametros
        Button(modificar, text="Modificar", font=(
            "arial", 13, "bold"), fg="green", command=Insertar).place(x=410, y=355)

        # Cerrar Modificar
        Button(modificar, text="Cerrar Ventana", font=(
            "arial", 13, "bold"), fg="green", command=modificar.destroy).place(x=570, y=355)

        modificar.mainloop() 
