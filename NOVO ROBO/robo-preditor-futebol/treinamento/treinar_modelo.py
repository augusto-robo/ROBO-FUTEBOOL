from sklearn.ensemble import RandomForestClassifier
import joblib

# Exemplo simples de treino
X = [[5, 4], [6, 5], [7, 6], [3, 2]]
y = ["Casa", "Casa", "Casa", "Fora"]

modelo = RandomForestClassifier()
modelo.fit(X, y)

joblib.dump(modelo, "dados/modelo_treinado.pkl")