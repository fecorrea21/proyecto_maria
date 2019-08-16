from tkinter import *
from tkinter import ttk


class Vista_cliente(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """Editar campos de texto"""

        def nuevo():
            self.entry_nombre.config(state="normal")
            self.entry_edad.config(state="normal")
            self.entry_telefono.config(state="normal")

        """Label titulo registrar"""
        self.label_titulo_resgistrar = Label(self, text="Registrar Nuevo Cliente")
        self.label_titulo_resgistrar.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        """Label y Campo de Nombre"""
        self.label_nombre = Label(self, text="Nombre del Cliente: ")
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)
        self.entry_nombre = Entry(self, state='readonly')
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        """Label y Campo de Edad """
        self.label_edad = Label(self, text="Edad: ")
        self.label_edad.grid(row=2, column=0, pady=10, padx=10)
        self.entry_edad = Entry(self, state='readonly')
        self.entry_edad.grid(row=2, column=1, pady=10, padx=10)

        """"Label y campo de telefono"""
        self.label_telefono = Label(self, text="Telefono")
        self.label_telefono.grid(row=3, column=0, pady=10, padx=10)
        self.entry_telefono = Entry(self, state='readonly')
        self.entry_telefono.grid(row=3, column=1, pady=10, padx=10)

        """Boton Nuevo"""
        self.boton_nuevo = Button(self, text="REGISTRAR NUEVO CLIENTE", command=nuevo)
        self.boton_nuevo.grid(row=4, column=0, pady=10, padx=10)

        """Boton Guardar"""
        self.boton_guardar = Button(self, text="GUARDAR CLIENTE")
        self.boton_guardar.grid(row=4, column=1, pady=10, padx=10)

        """Label Listar Carrera"""
        self.label_listar = Label(self, text="Lista de Cliente")
        self.label_listar.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

        """Crear Tabla"""
        self.tabla = ttk.Treeview(self, columns=('', '', ''))
        self.tabla.grid(row=6, column=0, columnspan=3, pady=10, padx=10)
        self.tabla.heading('#0', text="CODIGO DE CLIENTE")
        self.tabla.heading('#1', text="NOMBRE CLIENTE")
        self.tabla.heading('#2', text="EDAD CLIENTE")
        self.tabla.heading('#3', text="TELEFONO DEL CLIENTE")

        """Boton Eliminar"""
        self.boton_eliminar = Button(self, text="ELIMINAR CLIENTE")
        self.boton_eliminar.grid(row=7, column=0, pady=10, padx=10)

        def editar_datos():
            """Arranque de ventana Editar"""
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR CLIENTE")

            """Label y Campo de Codigo"""
            self.label_codigo = Label(self.ventana_editar, text="Codigo Cliente: ")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            """Label y Campo de Antiguo Nombre"""
            self.label_antiguo_nombre = Label(self.ventana_editar, text="Antiguo Nombre Cliente: ")
            self.label_antiguo_nombre.grid(row=1, column=0, pady=10, padx=10)
            self.entry_antigua_nombre = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_nombre.grid(row=1, column=1, pady=10, padx=10)

            """Label y Campo de Nuevo Nombre"""
            self.label_nuevo_nombre = Label(self.ventana_editar, text="Nuevo Nombre Cliente: ")
            self.label_nuevo_nombre.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nuevo_nombre = Entry(self.ventana_editar)
            self.entry_nuevo_nombre.grid(row=2, column=1, pady=10, padx=10)

            """Label y Campo de Antigua Edad"""
            self.label_antigua_edad = Label(self.ventana_editar, text="Antigua Edad: ")
            self.label_antigua_edad.grid(row=3, column=0, pady=10, padx=10)
            self.entry_antigua_edad = Entry(self.ventana_editar, state='readonly')
            self.entry_antigua_edad.grid(row=3, column=1, pady=10, padx=10)

            """Label y Campo de Nueva Edad"""
            self.label_nueva_edad = Label(self.ventana_editar, text="Nueva Edad: ")
            self.label_nueva_edad.grid(row=4, column=0, pady=10, padx=10)
            self.entry_nueva_edad = Entry(self.ventana_editar)
            self.entry_nueva_edad.grid(row=4, column=1, pady=10, padx=10)

            """Label y Campo de Antigua Telefono"""
            self.label_antiguo_telefono = Label(self.ventana_editar, text="Antiguo Telefono: ")
            self.label_antiguo_telefono.grid(row=5, column=0, pady=10, padx=10)
            self.entry_antiguo_telefono = Entry(self.ventana_editar, state='readonly')
            self.entry_antiguo_telefono.grid(row=5, column=1, pady=10, padx=10)

            """Label y Campo de Nueva Telefono"""
            self.label_nuevo_telefono = Label(self.ventana_editar, text="Nuevo Telefono: ")
            self.label_nuevo_telefono.grid(row=6, column=0, pady=10, padx=10)
            self.entry_nuevo_telefono = Entry(self.ventana_editar)
            self.entry_nuevo_telefono.grid(row=6, column=1, pady=10, padx=10)

            """Boton Actualizar"""
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR")
            self.boton_actualizar.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

        """Boton Editar"""
        self.boton_editar = Button(self, text="EDITAR CLIENTE", command=editar_datos)
        self.boton_editar.grid(row=7, column=1, pady=10, padx=10)


