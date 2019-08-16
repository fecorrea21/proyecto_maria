from tkinter import *
from tkinter import ttk
from vistas.frame_bodega import *
from vistas.frame_materia import *
from vistas.frame_cliente import *
from vistas.frame_proveedor import *

class Aplicacion(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.mi_ventana = ventana
        self.mi_ventana.title("Sistema Universitario")

        """Contenedor de paneles"""
        self.navegador = ttk.Notebook(self)

        """Panel de Inicio"""
        self.inicio = Label(self.navegador, text="Pagina de Inicio")
        self.navegador.add(self.inicio, text="Inicio")

        """Panel de bodega"""
        self.resg_bodega = Vista_bodega(self.navegador)
        self.navegador.add(self.resg_bodega, text="Bodega")

        """Panel de materia"""
        self.materia = Vista_materia(self.navegador)
        self.navegador.add(self.materia, text="Material")

        """Panel de Cliente"""
        self.cliente = Vista_cliente(self.navegador)
        self.navegador.add(self.cliente, text="Cliente")

        """Panel de Proveedor"""
        self.proveedor = Vista_proveedor(self.navegador)
        self.navegador.add(self.proveedor, text="Proveedor")

        self.navegador.pack()
        self.pack()
