from tkinter import *
from tkinter import ttk


class Vista_profesor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """Editar campos de texto"""

        def nuevo():
            self.entry_nombre.config(state="normal")
            self.entry_telefono.config(state="normal")
            self.entry_direccion.config(state="normal")

        """Label titulo registrar"""
        self.label_titulo_resgistrar = Label(self, text="Registrar Nuevo Profesor")
        self.label_titulo_resgistrar.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        """Label y Campo de Nombre"""
        self.label_nombre = Label(self, text="Nombre del Profesor: ")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        """"Label y campo de telefono"""
        self.label_telefono = Label(self, text="Telefono")
        self.label_telefono.grid(row=2, column=0, pady=10, padx=10)
        self.entry_telefono = Entry(self, state='readonly')
        self.entry_telefono.grid(row=2, column=1, pady=10, padx=10)

        """Label y campo de direccion"""
        self.label_direccion = Label(self, text="Direccion")
        self.label_direccion.grid(row=3, column=0, pady=10, padx=10)
        self.entry_direccion = Entry(self, state='readonly')
        self.entry_direccion.grid(row=3, column=1, pady=10, padx=10)

        """Boton Nuevo"""
        self.boton_nuevo = Button(self, text="REGISTRAR NUEVO PROFESOR", command=nuevo)
        self.boton_nuevo.grid(row=4, column=0, pady=10, padx=10)

        """Boton Guardar"""
        self.boton_guardar = Button(self, text="GUARDAR")
        self.boton_guardar.grid(row=4, column=1, pady=10, padx=10)

        """Label Listar Carrera"""
        self.label_listar = Label(self, text="Lista de profesores")
        self.label_listar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        """Crear Tabla"""
        self.tabla = ttk.Treeview(self, columns=('', '', ''))
        self.tabla.grid(row=6, column=0, columnspan=3, pady=10, padx=10)
        self.tabla.heading('#0', text="CODIGO DE PROFESOR")
        self.tabla.heading('#1', text="NOMBRE PROFESOR")
        self.tabla.heading('#2', text="TELEFONO")
        self.tabla.heading('#3', text="DIRECCION")

        """Boton Editar"""
        self.boton_editar = Button(self, text="EDITAR ALUMNO")
        self.boton_editar.grid(row=7, column=0, pady=10, padx=10)

        """Boton Eliminar"""
        self.boton_eliminar = Button(self, text="ELIMINAR ALUMNO")
        self.boton_eliminar.grid(row=7, column=1, pady=10, padx=10)
