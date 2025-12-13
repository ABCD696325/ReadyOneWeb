import streamlit as st
from capaLogica.nVehiculo import LVehiculos

class PVehiculos:
    def __init__(self):
        self.logica = LVehiculos()
        self.ui()

    def ui(self):
        st.header("🚐 Gestión de Vehículos")

        with st.form("formVehiculo"):
            placa = st.text_input("Placa")
            modelo = st.text_input("Modelo")
            capacidad = st.number_input("Capacidad", min_value=1)

            if st.form_submit_button("Registrar"):
                self.logica.nuevo(placa, modelo, capacidad)
                st.success("Vehículo registrado")

        st.dataframe(self.logica.listar(), use_container_width=True)
