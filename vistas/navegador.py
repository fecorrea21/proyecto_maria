from tkinter import *
from tkinter import ttk
from vistas.frame_carrera import *


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

        """Panel de Carrera"""
        self.resg_carrera = VisraCarrera(self.navegador)
        self.navegador.add(self.resg_carrera, text="Carrera")

        self.navegador.pack()
        self.pack()
