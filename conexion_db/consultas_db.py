import sqlite3


class Conectar_bd():
    nombre_db = '/home/fabian/Documentos/proyecto_maria/db/base_datos'

    def run_db(self, query, parametros=()):
        with sqlite3.connect(self.nombre_db) as conn:
            cursor = conn.cursor()
            datos = cursor.execute(query, parametros)

            conn.commit()
        return datos
