from capaLogica.nCliente import LClientes
import streamlit as st

class PClientes:
    def __init__(self):
        self.__nCliente = LClientes()

        # Estados de sesión
        if 'formKeyClientes' not in st.session_state:
            st.session_state.formKeyClientes = 0
        if 'clienteSeleccionado' not in st.session_state:
            st.session_state.clienteSeleccionado = None
        if 'idcliente' not in st.session_state:
            st.session_state.idcliente = 0
        if 'nombreCliente' not in st.session_state:
            st.session_state.nombreCliente = ''
        if 'dniCliente' not in st.session_state:
            st.session_state.dniCliente = ''
        if 'telefonoCliente' not in st.session_state:
            st.session_state.telefonoCliente = ''

        self.__construirInterfaz()

    def __construirInterfaz(self):
        st.title('READY ONE 🚐 | Registro de Clientes')

        # Si hay cliente seleccionado (editar)
        if st.session_state.clienteSeleccionado:
            st.session_state.idcliente = st.session_state.clienteSeleccionado['idcliente']
            st.session_state.nombreCliente = st.session_state.clienteSeleccionado['nombre']
            st.session_state.dniCliente = st.session_state.clienteSeleccionado['dni']
            st.session_state.telefonoCliente = st.session_state.clienteSeleccionado['telefono']

        with st.form(f'formClientes{st.session_state.formKeyClientes}'):
            txtNombre = st.text_input(
                'Nombre del cliente',
                value=st.session_state.nombreCliente
            )
            txtDni = st.text_input(
                'DNI',
                max_chars=8,
                value=st.session_state.dniCliente
            )
            txtTelefono = st.text_input(
                'Teléfono',
                max_chars=9,
                value=st.session_state.telefonoCliente
            )

            if st.session_state.clienteSeleccionado:
                btnActualizar = st.form_submit_button('Actualizar', type='primary')
                if btnActualizar:
                    self.actualizarCliente(
                        st.session_state.idcliente,
                        txtNombre,
                        txtDni,
                        txtTelefono
                    )
            else:
                btnGuardar = st.form_submit_button('Registrar', type='primary')
                if btnGuardar:
                    self.nuevoCliente(txtNombre, txtDni, txtTelefono)

        self.mostrarClientes()

    def mostrarClientes(self):
        st.subheader('Clientes registrados')
        lista = self.__nCliente.mostrarClientes()

        seleccion = st.dataframe(
            lista,
            selection_mode='single-row',
            on_select='rerun'
        )

        if seleccion.selection.rows:
            idx = seleccion.selection.rows[0]
            cliente = lista[idx]

            col1, col2 = st.columns(2)
            with col1:
                if st.button('Editar'):
                    st.session_state.clienteSeleccionado = cliente
                    st.rerun()
            with col2:
                if st.button('Eliminar'):
                    self.eliminarCliente(cliente['idcliente'])

    def nuevoCliente(self, nombre, dni, telefono):
        try:
            if not self._solo_numeros(dni):
                st.error("El DNI solo debe contener números")
                return

            if not self._solo_numeros(telefono):
                st.error("El teléfono solo debe contener números")
                return

            if len(dni) != 8:
                st.error("El DNI debe tener 8 dígitos")
                return

            if len(telefono) != 9:
                st.error("El teléfono debe tener 9 dígitos")
                return

            self.__nCliente.nuevoCliente(nombre, dni, telefono)
            st.success('Cliente registrado correctamente')
            self.limpiar()

        except Exception as e:
            st.error(str(e))

    def _solo_numeros(self, texto):
        return texto.isdigit()

    def actualizarCliente(self, idcliente, nombre, dni, telefono):
        try:
            if not dni.isdigit():
                st.error("El DNI solo debe contener números")
                return

            if not telefono.isdigit():
                st.error("El teléfono solo debe contener números")
                return

            self.__nCliente.actualizarCliente(idcliente, nombre, dni, telefono)
            st.success('Cliente actualizado correctamente')
            self.limpiar()

        except Exception as e:
            st.error(str(e))

    def eliminarCliente(self, idcliente):
        try:
            self.__nCliente.eliminarCliente(idcliente)
            st.success('Cliente eliminado')
            self.limpiar()
        except Exception as e:
            st.error(str(e))

    def limpiar(self):
        st.session_state.formKeyClientes += 1
        st.session_state.clienteSeleccionado = None
        st.session_state.idcliente = 0
        st.session_state.nombreCliente = ''
        st.session_state.dniCliente = ''
        st.session_state.telefonoCliente = ''
        st.rerun()
