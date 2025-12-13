
import streamlit as st

from capaPresentacion.pCliente import PClientes
from capaPresentacion.pViajes import PViajes
from capaPresentacion.pVehiculo import PVehiculos
from capaPresentacion.pConductor import PConductores
from capaPresentacion.pReserva import PReservas

PAGINAS = {
    "Clientes / Pasajeros": PClientes,
    "Viajes": PViajes,
    "Vehículos": PVehiculos,
    "Conductores": PConductores,
    "Reservas": PReservas
}

def main():
    st.set_page_config(
        page_title="READY ONE",
        page_icon="🚐",
        layout="wide"
    )

    st.sidebar.title("READY ONE 🚐✈️")
    st.sidebar.caption("Sistema de Gestión de Transporte")

    opcion = st.sidebar.selectbox(
        "Seleccione un módulo",
        list(PAGINAS.keys())
    )

    PAGINAS[opcion]()

if __name__ == "__main__":
    main()
