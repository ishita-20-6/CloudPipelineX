import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

print("🔄 Loading Iris Dataset...")
iris = load_iris()
X, y = iris.data, iris.target

print("🧠 Training Machine Learning Model (Random Forest)...")
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

print("💾 Saving trained model to disk...")
joblib.dump(model, "iris_model.pkl")

print("✅ Model trained and saved successfully as 'iris_model.pkl'!")
