import os
import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)

MODEL_PATH = "iris_model.pkl"

model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ ML Model loaded successfully!")
else:
    print("❌ Model file not found! Please run train_model.py first.")


@app.route("/")
def home():
    return jsonify(
        {
            "status": "success",
            "message": "Welcome to Iris Flower Prediction MLOps API!",
            "version": "3.0.0",
        }
    )


@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return jsonify({"error": "Model not loaded properly"}), 500

    try:
        data = request.get_json()

        features = [
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"],
            ]
        ]
        prediction = model.predict(features)[0]

        flower_types = ["Setosa", "Versicolor", "Virginica"]
        predicted_flower = flower_types[prediction]

        return jsonify(
            {"status": "success", "predicted_flower_type": predicted_flower}
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
