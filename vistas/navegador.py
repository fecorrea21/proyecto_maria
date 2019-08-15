from tkinter import *
from tkinter import ttk
from vistas.frame_carrera import *
from vistas.frame_materia import *
from vistas.frame_alumno import *
from vistas.frame_profesor import *

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
        self.resg_carrera = Vista_carrera(self.navegador)
        self.navegador.add(self.resg_carrera, text="Carrera")

        """Panel de materia"""
        self.materia = Vista_materia(self.navegador)
        self.navegador.add(self.materia, text="Materia")

        """Panel de Alumno"""
        self.alumno = Vista_alumno(self.navegador)
        self.navegador.add(self.alumno, text="Alumno")

        """Panel de Profesor"""
        self.profesor = Vista_profesor(self.navegador)
        self.navegador.add(self.profesor, text="Profesor")

        self.navegador.pack()
        self.pack()
