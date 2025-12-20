from capaDatos.dCliente import DCliente

class LClientes:
    def __init__(self):
        self.__dCliente = DCliente()

    def mostrarClientes(self):
        """
        Devuelve la lista de clientes/pasajeros
        que usan los servicios de READY ONE
        """
        return self.__dCliente.mostrarClientes()

    def nuevoCliente(self, nombre, dni, telefono):
        """
        Registra un nuevo cliente/pasajero
        """
        if not dni.isdigit():
            raise ValueError("DNI inválido: solo números")

        if not telefono.isdigit():
            raise ValueError("Teléfono inválido: solo números")

        return self.__dCliente.nuevoCliente(nombre, dni, telefono)


    def actualizarCliente(self, idcliente, nombre, dni, telefono):
        """
        Actualiza datos del cliente
        """
        return self.__dCliente.actualizarCliente(
            idcliente, nombre, dni, telefono
        )

    def eliminarCliente(self, idcliente):
        """
        Elimina un cliente del sistema
        """
        return self.__dCliente.eliminarCliente(idcliente)
