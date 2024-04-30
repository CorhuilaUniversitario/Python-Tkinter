import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class VentanaEliminar:
    
    # Ventana Modificar
    def eliminar():
        # Conexion Base de Datos
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="soporte",
        )
        mycursor = mydb.cursor()
        
        eliminar = tk.Tk()
        eliminar.title("")
        eliminar.geometry("1105x670")
        Label(eliminar, text="ELIMINAR ORDEN", font=(
            "arial20", 20,"bold"), fg="brown4").place(x=430, y=30)
        
        # Ventana Registro
        cambiar = LabelFrame(eliminar)
        cambiar.grid(row=0, column=0, padx=50, pady=90)

        # Ingreso ID
        Label(cambiar, text="Seleccione ID:", font=("arial", 13)).grid(
            row=0, column=0, padx=20, pady=10)
        entID = Entry(cambiar, width=20)
        entID.grid(row=0, column=1, padx=20)
        
        # Mostrar Tabla
        tabla = LabelFrame(eliminar, padx=20, pady=20)
        tabla.grid(row=1, column=0, padx=30)
        arbol = ttk.Treeview(tabla, columns=("ID", "DISPOSITIVO", "TIPO DE SERVICIO", "FALLA",
                                             "CLIENTE", "TELEFONO", "DIAGNOSTICO", "PRECIO", "FECHA"), show="headings", height=15,)
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
            
        def seleccion(event):
            punto = arbol.focus()

            if punto:

                values = arbol.item(punto)['values']
                entID.delete(0, END)
                entID.insert(0, values[0])
            
        arbol.bind("<<TreeviewSelect>>", seleccion)
        
        #Eliminar Parametro
        def Insertar():
            if (entID.get()==""):
                messagebox.showinfo("","Seleccione un ID",parent=eliminar)
            else:    
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="soporte",
                )
                mycursor = mydb.cursor()
                sql = "DELETE FROM ordenes WHERE id = %s"
                val = (entID.get(),)
                mycursor.execute(sql,val,)
                mydb.commit()
                # Ventana de registro exitoso
                messagebox.showinfo("", "ELIMINADO CORRECTAMENTE", parent=eliminar)

                # limpiar los datos
                entID.delete(0, END)
                
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
        Button(eliminar, text="Eliminar", font=(
            "arial", 13, "bold"), fg="red", command=Insertar).place(x=410, y=170)

        # Cerrar Eliminar
        Button(eliminar, text="Cerrar Ventana", font=(
            "arial", 13, "bold"), fg="red", command=eliminar.destroy).place(x=570, y=170)        
        
        eliminar.mainloop() 