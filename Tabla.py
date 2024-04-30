import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk

class VentanaTabla:
    
    def tabla():
        ventana = tk.Tk()
        ventana.geometry("1135x550")
        ventana.title("")
        Label(ventana, text="TABLA DE RESULTADOS", font=(
            "arial20", 20,"bold"), fg="purple4").place(x=400, y=30)
        
        # Mostrar Tabla
        tabla = LabelFrame(ventana, padx=40, pady=40)
        tabla.grid(row=0, column=0,pady=50)
        
        tabla = LabelFrame(ventana, padx=20, pady=20)
        tabla.grid(row=1, column=0, padx=20)
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
        arbol.column("#5", width=150, anchor=CENTER)
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
            mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="soporte",
            )
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM ordenes")

            myresult = mycursor.fetchall()
            mydb.commit()
            mydb.close()

            return myresult

        for row in mostrar():
            arbol.insert("", "end", values=row)
            
        # Cerrar registro
        Button(ventana, text="Cerrar Tabla", font=(
            "arial", 13, "bold"), fg="DarkOrchid4", command=ventana.destroy).place(x=500, y=490)    
        
        
        #ventana.mainloop()        