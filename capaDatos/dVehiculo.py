from conexion import ConexionDB

class DVehiculo:
    def __init__(self):
        self.db = ConexionDB().conexionSupabase()
        self.tabla = "vehiculos"

    def listar(self):
        return self.db.table(self.tabla).select("*").execute().data

    def insertar(self, placa, modelo, capacidad):
        return self.db.table(self.tabla).insert({
            "placa": placa,
            "modelo": modelo,
            "capacidad": capacidad
        }).execute()
