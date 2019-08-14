from tkinter import *
from tkinter import ttk

class VisraCarrera(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_duracion. config(state = "normal")


        self.label_titulo = Label(self, text= "Registrar Nueva Carrera").grid(row = 0, column= 0, columnspan = 2)

        """Campo de Nombre de la Carrera"""
        Label(self, text = "Nombre de la carrera: ").grid(row = 1, column = 0)
        self.entry_nombre = Entry(self, state = 'readonly')
        self.entry_nombre.grid(row = 1, column = 1)

        """Campo de Duracion de la carrera"""
        Label(self, text = "Duracion de Carrera: ").grid(row = 2, column = 0)
        self.entry_duracion = Entry(self, state = 'readonly')
        self.entry_duracion.grid(row = 2, column = 1)

        """Boton Nuevo"""
        Button(self, text = "NUEVO", command = nuevo).grid(row = 3, column = 0)

        """Boton Guardar"""
        Button(self, text = "GUARDAR").grid(row = 3, column = 1)