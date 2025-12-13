from capaDatos.dReserva import DReserva

class LReservas:
    def __init__(self):
        self.datos = DReserva()

    def listar(self):
        return self.datos.listar()

    def nueva(self, idcliente, idviaje, estado):
        return self.datos.insertar(idcliente, idviaje, estado)
