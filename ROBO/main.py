import streamlit as st
import os
from previsor import prever_resultado

# Histórico de previsões em sessão
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

st.set_page_config(page_title="Robô AUGUSTO MB", page_icon="⚽", layout="centered")

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

st.markdown("## ⚽ ROBÔ PREDITOR AUGUSTO MB")
st.markdown("### 🙏 VOCÊ É ABENÇOADO E PONTO FINAL")

time_casa = st.text_input("🏠 Time da Casa").strip()
time_fora = st.text_input("🚩 Time Visitante").strip()

if st.button("🔍 Prever Resultado"):
    if time_casa and time_fora:
        resultado = prever_resultado(time_casa, time_fora)

        # Mensagens personalizadas
        if "casa" in resultado.lower():
            msg = f"🏠 Vitória provável do {time_casa.title()}! 💥 Aposta segura no 1"
            st.success(msg)
        elif "fora" in resultado.lower():
            msg = f"🚩 Vitória provável do {time_fora.title()}! ⚠️ Boa opção no 2"
            st.success(msg)
        else:
            msg = "🤝 Empate provável! ⚖️ Pode apostar no X"
            st.info(msg)

        # Salvar no histórico
        st.session_state['historico'].append({
            "casa": time_casa.title(),
            "fora": time_fora.title(),
            "resultado": msg
            # Mostrar histórico de previsões
if st.session_state['historico']:
    st.markdown("---")
    st.markdown("## 📜 Histórico de Previsões")

    for item in st.session_state['historico'][-5:][::-1]:  # últimos 5
        st.markdown(f"**{item['casa']} vs {item['fora']}** → {item['resultado']}")

        })
    else:
        st.warning("⚠️ Preencha os dois times para prever!")
