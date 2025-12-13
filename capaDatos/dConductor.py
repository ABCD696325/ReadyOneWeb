from conexion import ConexionDB

class DConductor:
    def __init__(self):
        self.db = ConexionDB().conexionSupabase()
        self.tabla = "conductores"

    def listar(self):
        return self.db.table(self.tabla).select("*").execute().data

    def insertar(self, nombre, licencia, telefono):
        return self.db.table(self.tabla).insert({
            "nombre": nombre,
            "licencia": licencia,
            "telefono": telefono
        }).execute()
