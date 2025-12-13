from conexion import ConexionDB

class DReserva:
    def __init__(self):
        self.db = ConexionDB().conexionSupabase()
        self.tabla = "reservas"

    def listar(self):
        return self.db.table(self.tabla).select("*").execute().data

    def insertar(self, idcliente, idviaje, estado):
        return self.db.table(self.tabla).insert({
            "idcliente": idcliente,
            "idviaje": idviaje,
            "estado": estado
        }).execute()
