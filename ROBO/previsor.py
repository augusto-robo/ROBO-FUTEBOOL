
import joblib
import pandas as pd

modelo = joblib.load("ROBO/dados/modelo_treinado.pkl")



def def prever_resultado(time_casa, time_fora):
    mapa_times = {
        "real madrid": 1, "barcelona": 2, "bayern munique": 3, "manchester city": 4,
        "manchester united": 5, "liverpool": 6, "chelsea": 7, "psg": 8, "juventus": 9,
        "inter de milão": 10, "milan": 11, "arsenal": 12, "napoli": 13,

        "al hilal": 14, "al nassr": 15, "al ahli": 16, "al ittihad": 17, "persepolis": 18,
        "kashima antlers": 19, "gamba osaka": 20, "guangzhou evergrande": 21,
        "urawa red diamonds": 22, "al sadd": 23,

        "petro": 24, "primeiro de agosto": 25, "esperance": 26, "zamalek": 27, "al ahly": 28,
        "tp mazembe": 29, "kaizer chiefs": 30, "orlando pirates": 31,
        "vita club": 32, "cotonsport": 33,

        "flamengo": 34, "palmeiras": 35, "corinthians": 36, "são paulo": 37,
        "river plate": 38, "boca juniors": 39, "atlético nacional": 40,
        "club américa": 41, "la galaxy": 42, "seattle sounders": 43
    }

    # Normaliza os nomes digitados pelo usuário
    time_casa = time_casa.lower().strip()
    time_fora = time_fora.lower().strip()

    # Obtém os valores numéricos dos times ou usa 0 se não existir
    casa = mapa_times.get(time_casa, 0)
    fora = mapa_times.get(time_fora, 0)

    dados = [[casa, fora]]
    pred = modelo.predict(dados)[0]
    return pred

    }])
    pred = modelo.predict(dados)[0]
    if pred == 0:
        return "Vitória da Casa"
    elif pred == 1:
        return "Empate"
    else:
        return "Vitória do Visitante"
