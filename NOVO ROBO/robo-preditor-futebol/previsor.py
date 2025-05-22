import joblib

def prever_resultado(time_casa, time_fora):
    modelo = joblib.load("dados/modelo_treinado.pkl")
    entrada = [[len(time_casa), len(time_fora)]]
    previsao = modelo.predict(entrada)
    return previsao[0]