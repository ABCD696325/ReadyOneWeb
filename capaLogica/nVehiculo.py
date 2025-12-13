from capaDatos.dVehiculo import DVehiculo

class LVehiculos:
    def __init__(self):
        self.datos = DVehiculo()

    def listar(self):
        return self.datos.listar()

    def nuevo(self, placa, modelo, capacidad):
        return self.datos.insertar(placa, modelo, capacidad)
