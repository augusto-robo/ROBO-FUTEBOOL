import streamlit as st
import os
from previsor import prever_resultado

st.set_page_config(page_title="Robô Preditor de Futebol", page_icon="⚽", layout="centered")

# Estilo personalizado
st.markdown(
    """
    <style>
    body {
        background-color: #e9f5ec;
    }
    .stApp {
        background-image: url("https://i.ibb.co/4Kxprcy/campo-futebol.jpg");
        background-size: cover;
        background-position: center;
        color: white;
    }
    h1 {
        color: white;
        text-shadow: 2px 2px 4px #000000;
    }
    .stButton > button {
        background-color: #28a745;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⚽🔮 Robô Preditor de Futebol")

# Entradas
time_casa = st.text_input("🏠 Time da Casa").strip()
time_fora = st.text_input("🚩 Time Visitante").strip()

# Emblemas (básicos)
url_emblemas = {
    "flamengo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Flamengo_braz_logo.svg/1200px-Flamengo_braz_logo.svg.png",
    "river plate": "https://upload.wikimedia.org/wikipedia/pt/6/63/Club_Atl%C3%A9tico_River_Plate_logo.svg",
    "chelsea": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
    "psg": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"
}

# Mostrar emblemas
col1, col2 = st.columns(2)
if time_casa.lower() in url_emblemas:
    col1.image(url_emblemas[time_casa.lower()], width=100)
if time_fora.lower() in url_emblemas:
    col2.image(url_emblemas[time_fora.lower()], width=100)

# Botão
if st.button("🔍 Prever Resultado"):
    if time_casa and time_fora:
        resultado = prever_resultado(time_casa, time_fora)

        if "casa" in resultado.lower():
            st.success(f"🏠 Vitória provável do {time_casa.title()}!")
        elif "fora" in resultado.lower():
            st.success(f"🚩 Vitória provável do {time_fora.title()}!")
        else:
            st.info("🤝 Empate provável!")
    else:
        st.warning("⚠️ Preencha os dois times para prever!")
