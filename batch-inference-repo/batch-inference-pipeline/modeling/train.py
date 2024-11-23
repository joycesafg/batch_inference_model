import pickle
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

def train_new_model():
    # Dados fictícios para exemplo
    X, y = make_classification(n_samples=1000, n_features=20)
    model = RandomForestClassifier()
    model.fit(X, y)
    # Salva o novo modelo
    with open("models/new_model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_new_model()