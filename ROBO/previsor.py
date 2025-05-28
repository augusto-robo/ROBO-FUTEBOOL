import joblib

def prever_resultado(time_casa, time_fora):
    try:
        modelo_resultado = joblib.load("ROBO/dados/modelo_resultado.pkl")
        modelo_gols = joblib.load("ROBO/dados/modelo_gols.pkl")
        modelo_cantos = joblib.load("ROBO/dados/modelo_cantos.pkl")
    except FileNotFoundError:
        return "⚠️ Modelos ainda não treinados. Clique em 'Treinar Modelos'."

    mapa_times = {
        "flamengo": 1, "river plate": 2, "man city": 3, "real madrid": 4, "barcelona": 5,
        "psg": 6, "bayern munique": 7, "chelsea": 8, "al ahly": 9, "zamalek": 10,
        "tp mazembe": 11, "kaizer chiefs": 12, "esperance": 13, "gamba osaka": 14,
        "guangzhou evergrande": 15, "boca juniors": 16, "palmeiras": 17, "petro": 18,
        "1º de agosto": 19, "camaroes": 20, "brasil": 21, "angola": 22, "japao": 23,
        "portugal": 24, "franca": 25, "algeria": 26, "senegal": 27
    }

    time_casa = time_casa.lower().strip()
    time_fora = time_fora.lower().strip()

    casa = mapa_times.get(time_casa, 0)
    fora = mapa_times.get(time_fora, 0)

    if casa == 0 or fora == 0:
        return "⚠️ Um dos times não está no banco de dados do robô."

    # Gerar dados variáveis simulando estatísticas reais
    dados = [[casa, fora, abs(casa - fora) + 1, (casa + fora) % 5 + 3]]

    resultado = modelo_resultado.predict(dados)[0]
    gols = modelo_gols.predict(dados)[0]
    cantos = modelo_cantos.predict(dados)[0]

    texto_resultado = f"🏁 Vitória provável do {'Time da Casa' if resultado == 'casa' else 'Time Visitante' if resultado == 'fora' else 'Empate'}"
    texto_gols = "💥 Aposta segura: Mais de 2.5 gols!" if gols == 1 else "🚨 Menos de 2.5 gols esperados."
    texto_cantos = "🚩 Alta chance de +8.5 escanteios!" if cantos == 1 else "📉 Baixa chance de escanteios."

    return f"{texto_resultado}\n\n{texto_gols}\n{texto_cantos}"
