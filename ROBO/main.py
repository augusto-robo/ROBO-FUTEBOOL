import streamlit as st
from previsor import prever_resultado

# ✅ Adicione estas linhas:
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


st.set_page_config(page_title="Robô do AUGUSTO MB", page_icon="⚽", layout="centered")

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
        previsao = prever_resultado(time_casa, time_fora)
        st.markdown("### 📊 Previsão do Robô:")
        st.markdown(previsao)
    else:
        st.warning("⚠️ Preencha os dois times para prever.")
        from sklearn.ensemble import RandomForestClassifier
import joblib
import os

if st.button("⚙️ Treinar Modelos no Servidor"):
    st.info("Treinando modelos no ambiente Streamlit...")

    X = [[2, 0, 5, 3], [1, 1, 4, 4], [0, 2, 3, 6], [3, 1, 7, 4]]
    y_resultado = ["casa", "empate", "fora", "casa"]
    y_gols = [1, 0, 1, 1]
    y_cantos = [1, 0, 1, 1]

    os.makedirs("ROBO/dados", exist_ok=True)

    joblib.dump(RandomForestClassifier().fit(X, y_resultado), "ROBO/dados/modelo_resultado.pkl")
    joblib.dump(RandomForestClassifier().fit(X, y_gols), "ROBO/dados/modelo_gols.pkl")
    joblib.dump(RandomForestClassifier().fit(X, y_cantos), "ROBO/dados/modelo_cantos.pkl")

    st.success("✅ Modelos criados com sucesso no servidor!")

