from capaDatos.dViajes import DViaje

class LViajes:
    def __init__(self):
        self.datos = DViaje()

    def listar(self):
        return self.datos.listar()

    def nuevo(self, *args):
        return self.datos.insertar(*args)
