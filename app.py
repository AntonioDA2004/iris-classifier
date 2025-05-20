# API to serve the model
from flask import Flask, request, jsonify
import mlflow.sklearn
import os

app = Flask(__name__)

# Check if model exists and load it
model = None
try:
    if os.path.exists("iris_model"):
        model = mlflow.sklearn.load_model("iris_model")
    else:
        print("Error: Model 'iris_model' does not exist in current directory")
except Exception as e:
    print(f"Error loading model: {str(e)}")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return jsonify({"error": "Model is not loaded"}), 503

        json_data = request.get_json()
        if not json_data or "features" not in json_data:
            return jsonify({"error": "Field 'features' is required in JSON"}), 400

        features = json_data["features"]
        pred = model.predict([features]).tolist()
        return jsonify({"prediction": pred})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
