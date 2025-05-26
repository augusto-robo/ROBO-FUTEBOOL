import joblib

# Carregar os 3 modelos
modelo_resultado = joblib.load("ROBO/dados/modelo_resultado.pkl")
modelo_gols = joblib.load("ROBO/dados/modelo_gols.pkl")
modelo_cantos = joblib.load("ROBO/dados/modelo_cantos.pkl")

def prever_resultado(time_casa, time_fora):
    mapa_times = {
        "flamengo": 1, "river plate": 2, "chelsea": 3, "psg": 4,
        "real madrid": 5, "barcelona": 6, "petro": 7, "primeiro de agosto": 8
    }

    time_casa = time_casa.lower().strip()
    time_fora = time_fora.lower().strip()

    casa = mapa_times.get(time_casa, 0)
    fora = mapa_times.get(time_fora, 0)

    # Simular estatísticas do confronto (⚠️ depois vamos usar dados reais)
    dados = [[2, 1, 5, 4]] if casa and fora else [[0, 0, 0, 0]]

    # Previsões
    resultado = modelo_resultado.predict(dados)[0]
    gols = modelo_gols.predict(dados)[0]
    cantos = modelo_cantos.predict(dados)[0]

    # Montar resposta com frases personalizadas
    texto_resultado = f"🏁 Resultado provável: **{resultado.upper()}**"
    texto_gols = "🔥 Mais de 2.5 gols" if gols == 1 else "⚠️ Menos de 2.5 gols"
    texto_cantos = "🚩 Mais de 8.5 escanteios" if cantos == 1 else "🔍 Menos de 8.5 escanteios"

   return f"{texto_resultado}\n\n{texto_gols}\n{texto_cantos}"

