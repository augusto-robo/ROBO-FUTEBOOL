import streamlit as st
from previsor import prever_resultado

st.set_page_config(page_title="Robô do AUGUSTO MB", page_icon="⚽", layout="centered")

# CSS personalizado com imagem de fundo e estilo profissional
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://images.unsplash.com/photo-1599058917211-91f1c781f416?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        font-family: sans-serif;
    }
    h1, h3 {
        color: white;
        text-align: center;
        text-shadow: 2px 2px 5px black;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #000;
        font-weight: bold;
    }
    .stButton > button {
        background-color: #28a745;
        color: white;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho com nome e frase
st.markdown("## ⚽ ROBÔ PREDITOR AUGUSTO MB")
st.markdown("### 🙏 VOCÊ É ABENÇOADO E PONTO FINAL")

# Entrada de times
time_casa = st.text_input("🏠 Time da Casa").strip()
time_fora = st.text_input("🚩 Time Visitante").strip()

# Emblemas básicos
url_emblemas = {
    "flamengo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Flamengo_braz_logo.svg/1200px-Flamengo_braz_logo.svg.png",
    "river plate": "https://upload.wikimedia.org/wikipedia/pt/6/63/Club_Atl%C3%A9tico_River_Plate_logo.svg",
    "chelsea": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
    "psg": "https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"
}

# Mostrar escudos
col1, col2 = st.columns(2)
if time_casa.lower() in url_emblemas:
    col1.image(url_emblemas[time_casa.lower()], width=100)
if time_fora.lower() in url_emblemas:
    col2.image(url_emblemas[time_fora.lower()], width=100)

# Botão de previsão
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
