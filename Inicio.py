import streamlit as st

st.set_page_config(page_title="Clases de Humanidades", page_icon="🏫")

# Diseño UX: Fondo de Cuaderno Rayado Sobrio
estilo_cuaderno = """
<style>
/* Crea las líneas horizontales suaves del cuaderno */
[data-testid="stAppViewContainer"] {
    background-color: #fcfcfc;
    background-image: repeating-linear-gradient(transparent, transparent 29px, #d2e4f0 29px, #d2e4f0 30px);
    background-attachment: local;
}
/* Mantiene el fondo blanco limpio en las cajas de texto para no cansar la vista */
.stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
    background-color: white !important;
    border: 1px solid #ccc !important;
}
</style>
"""
st.markdown(estilo_cuaderno, unsafe_allow_html=True)

st.title("Bienvenido al Portal de Clases 🏫")
st.subheader("Profesor: Eduardo Florez Montero")

st.markdown("---")
st.write("Hola a todos. En este aplicativo encontrarán las fichas de trabajo interactivas para nuestras sesiones.")
st.info("👈 Por favor, abre el menú lateral izquierdo (haz clic en la flechita arriba a la izquierda si estás en celular) y selecciona la ficha que corresponde al día de hoy.")

st.write("Recuerda leer bien las indicaciones antes de descargar tu evidencia.")
st.success("¡Mucho éxito en tus actividades!")
