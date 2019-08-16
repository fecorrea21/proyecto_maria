from tkinter import *
from tkinter import ttk


class Vista_bodega(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo():
            self.entry_nombre.config(state="normal")
            self.entry_duracion.config(state="normal")

        """Label titulo registrar"""
        self.label_titulo = Label(self, text="Registrar Nueva Bodega")
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        """Label y Campo de Nombre"""
        self.label_nombre = Label(self, text="Nombre Bodega: ")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        """Label y Campo de Direccion"""
        self.label_direccion = Label(self, text="Direccion Bodega: ")
        self.label_direccion.grid(row=2, column=0, pady=10, padx=10)
        self.entry_duracion = Entry(self, state='readonly')
        self.entry_duracion.grid(row=2, column=1, pady=10, padx=10)

        """Boton Nuevo"""
        self.boton_nuevo = Button(self, text="NUEVA BODEGA", command=nuevo)
        self.boton_nuevo.grid(row=3, column=0, pady=10, padx=10)

        """Boton Guardar"""
        self.boton_guardar = Button(self, text="GUARDAR BODEGA")
        self.boton_guardar.grid(row=3, column=1, pady=10, padx=10)

        """Label Listar Carrera"""
        self.label_listar = Label(self, text="Lista de Bodegas")
        self.label_listar.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

        """Tabla"""
        self.tabla = ttk.Treeview(self, columns=('', ''))
        self.tabla.grid(row=5, column=0, columnspan=3, pady=10, padx=10)
        self.tabla.heading('#0', text="CODIGO DE BODEGA")
        self.tabla.heading('#1', text="NOMBRE BODEGA")
        self.tabla.heading('#2', text="DIRECCION DE BODEGA")

        """Boton Eliminar"""
        self.boton_eliminar = Button(self, text="ELIMINAR CARRERA")
        self.boton_eliminar.grid(row=6, column=0, pady=10, padx=10)

        """Editar datos"""

        def editar_datos():
            """Arranque de ventana Editar"""
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR BODEGA")

            """Label y Campo de Codigo"""
            self.label_codigo = Label(self.ventana_editar, text="Codigo Bodega: ")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            """Label y Campo de Antiguo Nombre"""
            self.label_antiguo_nombre = Label(self.ventana_editar, text="Antiguo Nombre Bodega: ")
            self.label_antiguo_nombre.grid(row=1, column=0, pady=10, padx=10)
            self.entry_antigua_nombre = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_nombre.grid(row=1, column=1, pady=10, padx=10)

            """Label y Campo de Nuevo Nombre"""
            self.label_nuevo_nombre = Label(self.ventana_editar, text="Nuevo Nombre Bodega: ")
            self.label_nuevo_nombre.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nuevo_nombre = Entry(self.ventana_editar)
            self.entry_nuevo_nombre.grid(row=2, column=1, pady=10, padx=10)

            """Label y Campo de Antigua Direccion"""
            self.label_antigua_direccion = Label(self.ventana_editar, text="Antigua Direccion Bodega: ")
            self.label_antigua_direccion.grid(row=3, column=0, pady=10, padx=10)
            self.entry_antigua_duracion = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_duracion.grid(row=3, column=1, pady=10, padx=10)

            """Label y Campo de Nueva Direccion"""
            self.label_nueva_direccion = Label(self.ventana_editar, text="Nueva Direccion Bodega: ")
            self.label_nueva_direccion.grid(row=4, column=0, pady=10, padx=10)
            self.entry_nueva_duracion = Entry(self.ventana_editar)
            self.entry_nueva_duracion.grid(row=4, column=1, pady=10, padx=10)

            """Boton Actualizar"""
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR BODEGA")
            self.boton_actualizar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        """Boton Editar"""
        self.boton_editar = Button(self, text="EDITAR BODEGA", command=editar_datos)
        self.boton_editar.grid(row=6, column=1, pady=10, padx=10)
