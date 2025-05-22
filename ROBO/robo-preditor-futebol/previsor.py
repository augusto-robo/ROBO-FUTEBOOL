
import joblib
import pandas as pd

modelo = joblib.load("modelos/preditivo.pkl")

def prever_resultado(time_casa, time_fora):
    dados = pd.DataFrame([{
        "media_gols_casa": 1.5,
        "media_gols_fora": 1.2,
        "forma_casa": 3,
        "forma_fora": 2
    }])
    pred = modelo.predict(dados)[0]
    if pred == 0:
        return "Vitória da Casa"
    elif pred == 1:
        return "Empate"
    else:
        return "Vitória do Visitante"
