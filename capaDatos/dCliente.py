from conexion import ConexionDB

class DCliente:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__tabla = 'clientes'

    def mostrarClientes(self):
        """
        Obtiene todos los clientes/pasajeros
        de READY ONE
        """
        response = self.__db.table(self.__tabla).select('*').execute()
        return response.data

    def nuevoCliente(self, nombre, dni, telefono):
        """
        Inserta un nuevo cliente
        """
        cliente = {
            'nombre': nombre,
            'dni': dni,
            'telefono': telefono
        }
        return self.__db.table(self.__tabla).insert(cliente).execute()

    def actualizarCliente(self, idcliente, nombre, dni, telefono):
        """
        Actualiza un cliente existente
        """
        cliente = {
            'nombre': nombre,
            'dni': dni,
            'telefono': telefono
        }
        return (
            self.__db
            .table(self.__tabla)
            .update(cliente)
            .eq('idcliente', idcliente)
            .execute()
        )

    def eliminarCliente(self, idcliente):
        """
        Elimina un cliente del sistema
        """
        return (
            self.__db
            .table(self.__tabla)
            .delete()
            .eq('idcliente', idcliente)
            .execute()
        )
