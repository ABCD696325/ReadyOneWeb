import streamlit as st
from capaLogica.nViajes import LViajes
from capaLogica.nVehiculo import LVehiculos
from capaLogica.nConductor import LConductores

class PViajes:
    def __init__(self):
        self.viajes = LViajes()
        self.vehiculos = LVehiculos()
        self.conductores = LConductores()
        self.ui()

    def ui(self):
        st.header("🗺️ Viajes")

        vehiculos = self.vehiculos.listar()
        conductores = self.conductores.listar()

        map_v = {v["placa"]: v["idvehiculo"] for v in vehiculos}
        map_c = {c["nombre"]: c["idconductor"] for c in conductores}

        with st.form("formViaje"):
            origen = st.text_input("Origen")
            destino = st.text_input("Destino")
            fecha = st.date_input("Fecha")
            tipo = st.selectbox("Tipo", ["Aeropuerto", "Tour"])
            vehiculo = st.selectbox("Vehículo", map_v.keys())
            conductor = st.selectbox("Conductor", map_c.keys())

            if st.form_submit_button("Registrar viaje"):
                self.viajes.nuevo(
                    origen, destino, fecha, tipo,
                    map_v[vehiculo], map_c[conductor]
                )
                st.success("Viaje registrado")

        st.dataframe(self.viajes.listar(), use_container_width=True)
