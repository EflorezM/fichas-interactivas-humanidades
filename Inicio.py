import streamlit as st

st.set_page_config(page_title="Clases de Humanidades", page_icon="🏫")

# Diseño de fondo sobrio y educativo (Efecto cuaderno cuadriculado sutil)
estilo_fondo = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f7f9fc;
    background-image: radial-gradient(#d1d8e0 1px, transparent 1px);
    background-size: 25px 25px;
}
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e0e6ed;
}
</style>
"""
st.markdown(estilo_fondo, unsafe_allow_html=True)

st.title("Bienvenido al Portal de Clases 🏫")
st.subheader("Profesor: Eduardo Florez Montero")

st.markdown("---")
st.write("Hola a todos. En este aplicativo encontrarán las fichas de trabajo interactivas para nuestras sesiones.")
st.info("👈 Por favor, abre el menú lateral izquierdo (haz clic en la flechita arriba a la izquierda si estás en celular) y selecciona la ficha que corresponde al día de hoy.")

st.write("Recuerda leer bien las indicaciones antes de descargar tu evidencia.")
st.success("¡Mucho éxito en tus actividades!")
