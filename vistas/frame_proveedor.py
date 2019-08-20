from tkinter import *
from tkinter import ttk


class Vista_proveedor(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """Editar campos de texto"""

        def nuevo():
            self.entry_nombre.config(state="normal")
            self.entry_telefono.config(state="normal")
            self.entry_direccion.config(state="normal")

        """Label titulo registrar"""
        self.label_titulo_resgistrar = Label(self, text="Registrar Nuevo Proveedor")
        self.label_titulo_resgistrar.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        """Label y Campo de Nombre"""
        self.label_nombre = Label(self, text="Nombre del Proveedor: ")
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
        self.boton_nuevo = Button(self, text="REGISTRAR NUEVO PROVEEDOR", command=nuevo)
        self.boton_nuevo.grid(row=4, column=0, pady=10, padx=10)

        """Boton Guardar"""
        self.boton_guardar = Button(self, text="GUARDAR")
        self.boton_guardar.grid(row=4, column=1, pady=10, padx=10)

        """Label Listar Carrera"""
        self.label_listar = Label(self, text="Lista de Proveedor")
        self.label_listar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        """Crear Tabla"""
        self.tabla = ttk.Treeview(self, columns=('', '', ''))
        self.tabla.grid(row=6, column=0, columnspan=3, pady=10, padx=10)
        self.tabla.heading('#0', text="CODIGO DE PROVEEDOR")
        self.tabla.heading('#1', text="NOMBRE PROVEEDOR")
        self.tabla.heading('#2', text="TELEFONO")
        self.tabla.heading('#3', text="DIRECCION")

        """Boton Eliminar"""
        self.boton_eliminar = Button(self, text="ELIMINAR PROVEEDOR")
        self.boton_eliminar.grid(row=7, column=0, pady=10, padx=10)

        """Editar datos"""

        def editar_datos():
            """Arranque de ventana Editar"""
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR PROVEEDOR")

            """Label y Campo de Codigo"""
            self.label_codigo = Label(self.ventana_editar, text="Codigo Proveedor: ")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            """Label y Campo de Antiguo Nombre"""
            self.label_antiguo_nombre = Label(self.ventana_editar, text="Antiguo Nombre Proveedor: ")
            self.label_antiguo_nombre.grid(row=1, column=0, pady=10, padx=10)
            self.entry_antigua_nombre = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_nombre.grid(row=1, column=1, pady=10, padx=10)

            """Label y Campo de Nuevo Nombre"""
            self.label_nuevo_nombre = Label(self.ventana_editar, text="Nuevo Nombre Proveedor: ")
            self.label_nuevo_nombre.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nuevo_nombre = Entry(self.ventana_editar)
            self.entry_nuevo_nombre.grid(row=2, column=1, pady=10, padx=10)

            """Label y Campo de Antiguo Telefono"""
            self.label_antiguo_telefono = Label(self.ventana_editar, text="Antiguo Nombre Telefono: ")
            self.label_antiguo_telefono.grid(row=3, column=0, pady=10, padx=10)
            self.entry_antigua_telefono = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_telefono.grid(row=3, column=1, pady=10, padx=10)

            """Label y Campo de Nuevo Telefono"""
            self.label_nuevo_telefono = Label(self.ventana_editar, text="Nuevo Nombre Telefono: ")
            self.label_nuevo_telefono.grid(row=4, column=0, pady=10, padx=10)
            self.entry_nuevo_telefono = Entry(self.ventana_editar)
            self.entry_nuevo_telefono.grid(row=4, column=1, pady=10, padx=10)

            """Label y Campo de Antigua Direccion"""
            self.label_antigua_direccion = Label(self.ventana_editar, text="Antigua Direccion Proveedor: ")
            self.label_antigua_direccion.grid(row=5, column=0, pady=10, padx=10)
            self.entry_antigua_duracion = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_duracion.grid(row=5, column=1, pady=10, padx=10)

            """Label y Campo de Nueva Direccion"""
            self.label_nueva_direccion = Label(self.ventana_editar, text="Nueva Direccion Proveedor: ")
            self.label_nueva_direccion.grid(row=6, column=0, pady=10, padx=10)
            self.entry_nueva_duracion = Entry(self.ventana_editar)
            self.entry_nueva_duracion.grid(row=6, column=1, pady=10, padx=10)

            """Boton Actualizar"""
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR")
            self.boton_actualizar.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

        """Boton Editar"""
        self.boton_editar = Button(self, text="EDITAR PROVEEDOR", command= editar_datos)
        self.boton_editar.grid(row=7, column=1, pady=10, padx=10)
