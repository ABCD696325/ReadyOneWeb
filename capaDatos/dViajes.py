from conexion import ConexionDB

class DViaje:
    def __init__(self):
        self.db = ConexionDB().conexionSupabase()
        self.tabla = "viajes"

    def listar(self):
        return self.db.table(self.tabla).select("*").execute().data

    def insertar(self, origen, destino, fecha, tipo, idvehiculo, idconductor):
        if hasattr(fecha, "strftime"):
            fecha = fecha.strftime("%Y-%m-%d")
            
        return self.db.table(self.tabla).insert({
            "origen": origen,
            "destino": destino,
            "fecha": fecha,
            "tipo": tipo,
            "idvehiculo": idvehiculo,
            "idconductor": idconductor
        }).execute()
