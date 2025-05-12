import os
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Define target columns for prediction
target_columns = [
    'player1_left', 'player1_right', 'player1_up', 'player1_down',
    'player1_A', 'player1_B', 'player1_X', 'player1_Y', 'player1_L', 'player1_R',
    'player2_left', 'player2_right', 'player2_up', 'player2_down',
    'player2_A', 'player2_B', 'player2_X', 'player2_Y', 'player2_L', 'player2_R'
]

# Define file paths to model and scaler located in the root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))  # Go up to the root directory
model_path = os.path.join(root_dir, 'mlp_model.pkl')
scaler_path = os.path.join(root_dir, 'scaler.pkl')

# Load the model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "API is running"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read the JSON data from the request
        data = request.get_json()
        input_df = pd.DataFrame([data])

        # Standardize the input features using the loaded scaler
        input_scaled = scaler.transform(input_df)

        # Make prediction using the loaded model
        prediction = model.predict(input_scaled)

        # Convert prediction to a list and return as JSON
        return jsonify({"Predicted Buttons": prediction.tolist()})

    except Exception as e:
        # If any error occurs, return error details with a 400 status
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)