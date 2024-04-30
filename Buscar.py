import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Conexion Base de Datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soporte",
)
mycursor = mydb.cursor()


class VentanaBuscar:

    # Ventana de Registro
    def Buscar():
        buscar = tk.Tk()
        buscar.title("")
        buscar.geometry("400x280")
        Label(buscar, text="BUSCAR ORDEN", font=(
            "arial20", 20,"bold"), fg="green").place(x=90, y=40)

        # Ventana Registro
        ventana = LabelFrame(buscar)
        ventana.grid(row=0, column=0, padx=50, pady=100)

        # Ingreso Dispositivo
        Label(ventana, text="Buscar por:", font=("arial", 13)).grid(
            row=0, column=0, padx=20, pady=10)
        entSeleccion = ttk.Combobox(
            ventana, values=["ID", "CLIENTE"], width=17)
        entSeleccion.grid(row=0, column=1, padx=20, pady=10)

        # Ingreso Servicio
        Label(ventana, text="Busqueda:", font=("arial", 13)).grid(
            row=1, column=0, padx=20, pady=10)
        entBuscar = Entry(ventana, width=20)
        entBuscar.grid(row=1, column=1, padx=20, pady=10)

        # Base de datos Registro
        def Insertar():

            # Para digitar casillas
            if entBuscar.get() == "":
                messagebox.showinfo(
                    "", "No dejar Casilla Vacia", parent=buscar)

            else:
                # Seleccion de ID
                if entSeleccion.get() == "ID":
                    sql = "SELECT * FROM ordenes WHERE ID = %s"
                    val = (entBuscar.get(),)
                    mycursor.execute(sql, val)
                    myresult = mycursor.fetchone()

                    # Busqueda del parametro
                    if myresult is not None:
                        ventanaTabla = tk.Tk()
                        ventanaTabla.title("BUSQUEDA")
                        tabla = LabelFrame(ventanaTabla, padx=40, pady=40)
                        tabla.grid(row=0, column=0)
                        arbol = ttk.Treeview(tabla, columns=("ID", "DISPOSITIVO", "TIPO DE SERVICIO", "FALLA",
                                             "CLIENTE", "TELEFONO", "DIAGNOSTICO", "PRECIO", "FECHA"), show="headings", height=1,)
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

                        arbol.insert("", "end", values=myresult)
                        arbol.pack()
                        
                    else:
                        messagebox.showinfo(
                            "", "No se encontro Registro", parent=buscar)

                # Seleccion de Cliente
                elif entSeleccion.get() == "CLIENTE":

                    sql = "SELECT * FROM ordenes WHERE CLIENTE = %s"
                    val = (entBuscar.get(),)
                    mycursor.execute(sql, val)
                    myresult = mycursor.fetchone()

                    # Busqueda del parametro
                    if myresult is not None:
                        ventanaTabla = tk.Tk()
                        ventanaTabla.title("BUSQUEDA")
                        tabla = LabelFrame(ventanaTabla, padx=40, pady=40)
                        tabla.grid(row=0, column=0)
                        arbol = ttk.Treeview(tabla, columns=("ID", "DISPOSITIVO", "TIPO DE SERVICIO", "FALLA",
                                             "CLIENTE", "TELEFONO", "DIAGNOSTICO", "PRECIO", "FECHA"), show="headings", height=1,)
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

                        arbol.insert("", "end", values=myresult)
                        arbol.pack()
                        
                    else:
                        messagebox.showinfo(
                            "", "No se encontro Registro", parent=buscar)

                # Mensaje de error
                else:
                    messagebox.showinfo(
                        "", "Seleccione un Parametro", parent=buscar)   

            # limpiar los datos
            entSeleccion.delete(0, END)
            entBuscar.delete(0, END)

        # Boton de Ingresar parametros
        Button(buscar, text="Ingreso", font=(
            "arial", 13, "bold"), fg="purple4", command=Insertar).place(x=70, y=220)

        # Cerrar Busqueda
        Button(buscar, text="Cerrar Ventana", font=(
            "arial", 13, "bold"), fg="purple4", command=buscar.destroy).place(x=200, y=220)

        ventana.mainloop()