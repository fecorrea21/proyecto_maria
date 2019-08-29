from tkinter import *
from tkinter import ttk
from conexion_db.consultas_db import *


class Vista_cliente(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """Editar campos de texto"""

        def nuevo():
            self.entry_nombre.config(state="normal")
            self.entry_edad.config(state="normal")
            self.entry_telefono.config(state="normal")

        # Agregar datos a base de datos

        def agregar_datos():
            query = 'INSERT INTO cliente VALUES (NULL,?,?,?)'
            parametros = (self.entry_nombre.get(), self.entry_edad.get(), self.entry_telefono.get())

            conn = Conectar_bd()
            conn.run_db(query, parametros)

            # Limpiar Campos
            self.entry_nombre.delete(0, END)
            self.entry_edad.delete(0, END)
            self.entry_telefono.delete(0, END)

            # Mostar Datos
            listar_datos()

        # Eliminar Datos
        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = 'DELETE FROM cliente where codigo_a = ?'

            conn = Conectar_bd()
            conn.run_db(query, (codigo,))

            # Actualizar Tabla
            listar_datos()

        # Actualizar Datos
        def actualizar_datos(codigo_n, codigo_a, nombre_n, nombre_a, edad_n, edad_a, telefono_n, telefono_a):
            query = 'UPDATE cliente SET codigo_a = ?, nombre_a = ?, edad_a = ?, telefono_a = ? WHERE codigo_a=? AND nombre_a=? AND edad_a=? AND telefono_a=?'
            parametros = (codigo_n, nombre_n, edad_n, telefono_n, codigo_a, nombre_a, edad_a, telefono_a)

            conn = Conectar_bd()
            conn.run_db(query, parametros)
            self.ventana_editar.destroy()

            # Actualizar Tabla
            listar_datos()

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
        self.boton_guardar = Button(self, text="GUARDAR CLIENTE", command=agregar_datos)
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
        self.boton_eliminar = Button(self, text="ELIMINAR CLIENTE", command=eliminar_datos)
        self.boton_eliminar.grid(row=7, column=0, pady=10, padx=10)

        def editar_datos():

            codigo = self.tabla.item(self.tabla.selection())['text']
            nombre_anti = self.tabla.item(self.tabla.selection())['values'][0]
            edad_anti = self.tabla.item(self.tabla.selection())['values'][1]
            telefono_anti = self.tabla.item(self.tabla.selection())['values'][2]
            codigo_c1 = self.tabla.item(self.tabla.selection())['text']

            """Arranque de ventana Editar"""
            self.ventana_editar = Toplevel()
            self.ventana_editar.title("EDITAR CLIENTE")

            """Label y Campo de Codigo"""
            self.label_codigo = Label(self.ventana_editar, text="Codigo Cliente: ")
            self.label_codigo.grid(row=0, column=0, pady=10, padx=10)
            self.entry_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo),
                                      state='readonly')
            self.entry_codigo.grid(row=0, column=1, pady=10, padx=10)

            """Label y Campo de Antiguo Nombre"""
            self.label_antiguo_nombre = Label(self.ventana_editar, text="Antiguo Nombre Cliente: ")
            self.label_antiguo_nombre.grid(row=1, column=0, pady=10, padx=10)
            self.entry_antigua_nombre = Entry(self.ventana_editar,
                                              textvariable=StringVar(self.ventana_editar, value=nombre_anti),
                                              state='readonly')
            self.entry_antigua_nombre.grid(row=1, column=1, pady=10, padx=10)

            """Label y Campo de Nuevo Nombre"""
            self.label_nuevo_nombre = Label(self.ventana_editar, text="Nuevo Nombre Cliente: ")
            self.label_nuevo_nombre.grid(row=2, column=0, pady=10, padx=10)
            self.entry_nuevo_nombre = Entry(self.ventana_editar)
            self.entry_nuevo_nombre.grid(row=2, column=1, pady=10, padx=10)

            """Label y Campo de Antigua Edad"""
            self.label_antigua_edad = Label(self.ventana_editar, text="Antigua Edad: ")
            self.label_antigua_edad.grid(row=3, column=0, pady=10, padx=10)
            self.entry_antigua_edad = Entry(self.ventana_editar,
                                            textvariable=StringVar(self.ventana_editar, value=edad_anti),
                                            state='readonly')
            self.entry_antigua_edad.grid(row=3, column=1, pady=10, padx=10)

            """Label y Campo de Nueva Edad"""
            self.label_nueva_edad = Label(self.ventana_editar, text="Nueva Edad: ")
            self.label_nueva_edad.grid(row=4, column=0, pady=10, padx=10)
            self.entry_nueva_edad = Entry(self.ventana_editar)
            self.entry_nueva_edad.grid(row=4, column=1, pady=10, padx=10)

            """Label y Campo de Antigua Telefono"""
            self.label_antiguo_telefono = Label(self.ventana_editar, text="Antiguo Telefono: ")
            self.label_antiguo_telefono.grid(row=5, column=0, pady=10, padx=10)
            self.entry_antiguo_telefono = Entry(self.ventana_editar,
                                                textvariable=StringVar(self.ventana_editar, value=telefono_anti),
                                                state='readonly')
            self.entry_antiguo_telefono.grid(row=5, column=1, pady=10, padx=10)

            """Label y Campo de Nueva Telefono"""
            self.label_nuevo_telefono = Label(self.ventana_editar, text="Nuevo Telefono: ")
            self.label_nuevo_telefono.grid(row=6, column=0, pady=10, padx=10)
            self.entry_nuevo_telefono = Entry(self.ventana_editar)
            self.entry_nuevo_telefono.grid(row=6, column=1, pady=10, padx=10)

            """Boton Actualizar"""
            self.boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR",
                                           command=lambda: actualizar_datos(codigo, codigo,
                                                                            self.entry_nuevo_nombre.get(), nombre_anti,
                                                                            self.entry_nueva_edad.get(), edad_anti,
                                                                            self.entry_nuevo_telefono.get(),
                                                                            telefono_anti
                                                                            ))
            self.boton_actualizar.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

        """Boton Editar"""
        self.boton_editar = Button(self, text="EDITAR CLIENTE", command=editar_datos)
        self.boton_editar.grid(row=7, column=1, pady=10, padx=10)

        """Listar"""

        def listar_datos():
            # Eliminar datos de la tabla
            recorrer_table = self.tabla.get_children()
            for elementos in recorrer_table:
                self.tabla.delete(elementos)

            # Ejecutar la consulta y cargar datos
            query = 'select * from cliente'
            conn = Conectar_bd()
            datos = conn.run_db(query)

            for cliente in datos:
                self.tabla.insert('', 0, text=cliente[0], value=(cliente[1], cliente[2], cliente[3]))

        listar_datos()
