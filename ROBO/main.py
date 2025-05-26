import streamlit as st
from previsor import prever_resultado

st.set_page_config(page_title="Robô do AUGUSTO MB", page_icon="⚽", layout="centered")

# Interface e estilo
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://images.unsplash.com/photo-1599058917211-91f1c781f416?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
    }
    h1, h3 {
        color: white;
        text-align: center;
        text-shadow: 2px 2px 4px black;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #000;
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

# Cabeçalho
st.markdown("## ⚽ ROBÔ PREDITOR AUGUSTO MB")
st.markdown("### 🙏 VOCÊ É ABENÇOADO E PONTO FINAL")

# Entrada
time_casa = st.text_input("🏠 Time da Casa").strip()
time_fora = st.text_input("🚩 Time Visitante").strip()

# Previsão com IA real
if st.button("🔍 Prever Resultado"):
    if time_casa and time_fora:
        resultado = prever_resultado(time_casa, time_fora)

        # Mostrar previsão completa
        st.markdown("### 📊 Previsão:")
        st.markdown(resultado)

    else:
        st.warning("⚠️ Preencha os dois times para prever.")
