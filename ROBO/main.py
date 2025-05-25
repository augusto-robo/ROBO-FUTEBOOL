import os
import streamlit as st

st.write("Diretório de trabalho atual:", os.getcwd())
st.write("Arquivos no diretório atual:", os.listdir())
import os
import streamlit as st

st.write("Diretório de trabalho atual:", os.getcwd())

import streamlit as st
from previsor import prever_resultado

st.title("🔮 Robô Preditor de Futebol")

time_casa = st.text_input("Time da Casa")
time_fora = st.text_input("Time Visitante")

if st.button("Prever"):
    resultado = prever_resultado(time_casa, time_fora)
    st.success(f"Previsão: {resultado}")
