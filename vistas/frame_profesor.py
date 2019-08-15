from tkinter import *
from tkinter import ttk


class Vista_profesor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo():
            self.entry_nombre.config(state="normal")
            self.entry_duracion.config(state="normal")

        """Label titulo registrar"""
        self.label_titulo = Label(self, text="Registrar Nueva Carrera")
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        """Label y Campo de Nombre"""
        self.label_nombre = Label(self, text="Nombre de la carrera: ")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        """Label y Campo de Duracion"""
        self.laber_duracion = Label(self, text="Duracion de Carrera: ")
        self.label_nombre.grid(row=2, column=0, pady=10, padx=10)
        self.entry_duracion = Entry(self, state='readonly')
        self.entry_duracion.grid(row=2, column=1, pady=10, padx=10)

        """Boton Nuevo"""
        self.boton_nuevo = Button(self, text="NUEVA CARRERA", command=nuevo)
        self.boton_nuevo.grid(row=3, column=0, pady=10, padx=10)

        """Boton Guardar"""
        self.boton_guardar = Button(self, text="GUARDAR CARRERA")
        self.boton_guardar.grid(row=3, column=1, pady=10, padx=10)

        """Label Listar Carrera"""
        self.label_listar = Label(self, text="Lista de Carreras")
        self.label_listar.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        """Tabla"""
        self.tabla = ttk.Treeview(self, columns=('', ''))
        self.tabla.grid(row=5, column=0, columnspan=3, pady=10, padx=10)
        self.tabla.heading('#0', text="CODIGO DE CARRERA")
        self.tabla.heading('#1', text="NOMBRE CARRERA")
        self.tabla.heading('#2', text="DURACION DE CARRERA")

        """Boton Editar"""
        self.boton_editar = Button(self, text="EDITAR MATERIA")
        self.boton_editar.grid(row=6, column=0, pady=10, padx=10)

        """Boton Eliminar"""
        self.boton_eliminar = Button(self, text="ELIMINAR MATERIA")
        self.boton_eliminar.grid(row=6, column=1, pady=10, padx=10)
