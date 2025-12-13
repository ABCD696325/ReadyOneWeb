import streamlit as st
from capaLogica.nReserva import LReservas
from capaLogica.nCliente import LClientes
from capaLogica.nViajes import LViajes

class PReservas:
    def __init__(self):
        self.reservas = LReservas()
        self.clientes = LClientes()
        self.viajes = LViajes()
        self.ui()

    def ui(self):
        st.header("📑 Reservas")

        clientes = self.clientes.mostrarClientes()
        viajes = self.viajes.listar()

        map_c = {c["nombre"]: c["idcliente"] for c in clientes}
        map_v = {f'{v["origen"]} → {v["destino"]}': v["idviaje"] for v in viajes}

        with st.form("formReserva"):
            cliente = st.selectbox("Cliente", map_c.keys())
            viaje = st.selectbox("Viaje", map_v.keys())
            estado = st.selectbox("Estado", ["Reservado", "Confirmado", "Cancelado"])

            if st.form_submit_button("Registrar reserva"):
                self.reservas.nueva(
                    map_c[cliente],
                    map_v[viaje],
                    estado
                )
                st.success("Reserva registrada")

        st.dataframe(self.reservas.listar(), use_container_width=True)
