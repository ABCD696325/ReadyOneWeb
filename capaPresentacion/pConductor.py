import streamlit as st
from capaLogica.nConductor import LConductores

class PConductores:
    def __init__(self):
        self.logica = LConductores()
        self.ui()

    def ui(self):
        st.header("👨‍✈️ Conductores")

        with st.form("formConductor"):
            nombre = st.text_input("Nombre")
            licencia = st.text_input("Licencia")
            telefono = st.text_input("Teléfono")

            if st.form_submit_button("Registrar"):
                self.logica.nuevo(nombre, licencia, telefono)
                st.success("Conductor registrado")

        st.dataframe(self.logica.listar(), use_container_width=True)
