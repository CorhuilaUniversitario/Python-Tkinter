import tkinter as tk
from tkinter import *
from Registro import *
from Buscar import *
from Modificar import *
from Eliminar import *
from Tabla import *

class Principal:
    def Ventana():
        ventana = tk.Tk()
        ventana.geometry("1000x300")
        ventana.title("BIENVENIDO")
        ventana.configure(background="cornflower blue")

        # Boton de guardar
        guardar = LabelFrame(ventana)
        guardar.grid(row=0, column=0, padx=20, pady=20)
        imagenRegistro = tk.PhotoImage(
            file='Imagenes/registro.png').subsample(3)
        Label(guardar, image=imagenRegistro).grid(row=0, column=0, pady=20)
        Button(guardar, text="REGISTRO", width=16, font=12,
                   command=VentanaRegistro.Registro).grid(row=1, column=0)

        # Boton de Buscar
        buscar = LabelFrame(ventana)
        buscar.grid(row=0, column=1, padx=0, pady=20)
        imagenBuscar = PhotoImage(file="Imagenes/buscar.png").subsample(6)
        Label(buscar, image=imagenBuscar).grid(row=0, column=0, pady=20)
        Button(buscar, text="BUSQUEDA", width=16, height=0, font=10,
                command=VentanaBuscar.Buscar).grid(row=1, column=0)

        # Boton Modificar
        modificar = LabelFrame(ventana)
        modificar.grid(row=0, column=2, padx=20, pady=20)
        imagenModificar = PhotoImage(
            file="Imagenes/modificar.png").subsample(3)
        Label(modificar, image=imagenModificar).grid(
            row=0, column=0, pady=20)
        Button(modificar, text="MODIFICAR", width=16,
                height=0, font=10, command=VentanaModifcar.modificar).grid(row=1, column=0)

        # boton Eliminar
        eliminar = LabelFrame(ventana)
        eliminar.grid(row=0, column=3, padx=0, pady=20)
        imagenEliminar = PhotoImage(
            file="Imagenes/eliminar.png").subsample(3)
        Label(eliminar, image=imagenEliminar).grid(
            row=0, column=0, pady=20)
        Button(eliminar, text="ELIMINAR", width=16,
            height=0, font=10, command=VentanaEliminar.eliminar).grid(row=1, column=0)
        
        
        # Boton Tabla
        Button(ventana, text="TABLA", font=(
            "arial", 18, "bold"), fg="blue", command= VentanaTabla.tabla).place(x=880, y=90)
    
            
        # Cerrar registro
        Button(ventana, text="EXIT", font=(
            "arial", 18, "bold"), fg="red", command=ventana.destroy).place(x=893, y=170)

        ventana.mainloop()

    #Ventana()
