from capaDatos.dConductor import DConductor

class LConductores:
    def __init__(self):
        self.datos = DConductor()

    def listar(self):
        return self.datos.listar()

    def nuevo(self, nombre, licencia, telefono):
        return self.datos.insertar(nombre, licencia, telefono)
