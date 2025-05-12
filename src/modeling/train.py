import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import mlflow
import mlflow.sklearn


def train():
    # Load the dataset
    df = pd.read_csv('data/processed/processed_data.csv')

    # Define target columns (labels)
    target_columns = [
        'player1_left', 'player1_right', 'player1_up', 'player1_down',
        'player1_A', 'player1_B', 'player1_X', 'player1_Y', 'player1_L', 'player1_R',
        'player2_left', 'player2_right', 'player2_up', 'player2_down',
        'player2_A', 'player2_B', 'player2_X', 'player2_Y', 'player2_L', 'player2_R'
    ]

    # Features (X) and labels (y)
    X = df.drop(columns=target_columns + ['fight_result'])
    y = df[target_columns].astype(int)

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Model hyperparameters
    params = {
        "hidden_layer_sizes": (100, 50),
        "activation": "relu",
        "solver": "adam",
        "max_iter": 500,
        "random_state": 42
    }

    # Set tracking URI
    mlflow.set_tracking_uri("mlflow")

    # Create or set experiment
    experiment_name = "MLOps_Experiment"  # Define your experiment name
    mlflow.set_experiment(experiment_name)  # Set the experiment

    # Start an MLflow experiment
    with mlflow.start_run():
        # Log hyperparameters
        mlflow.log_params(params)
        
        # Initialize and train the model
        mlp = MLPClassifier(**params)
        multi_mlp = MultiOutputClassifier(mlp, n_jobs=-1)
        multi_mlp.fit(X_train_scaled, y_train)

        # Optionally evaluate on test set
        test_score = multi_mlp.score(X_test_scaled, y_test)
        print(f"[✔] Test accuracy: {test_score:.4f}")
        
        # Log metrics (test accuracy)
        mlflow.log_metric("test_accuracy", test_score)

        # Log model as an artifact
        mlflow.sklearn.log_model(multi_mlp, "model")
        mlflow.log_artifact("scaler.pkl")  # Save scaler artifact
        
        # Save model and scaler locally as well
        model_path = 'mlp_model.pkl'
        scaler_path = 'scaler.pkl'
        joblib.dump(multi_mlp, model_path)
        joblib.dump(scaler, scaler_path)

        print("[✔] Model and scaler saved locally")
        print("Training complete.")

if __name__ == "__main__":
    train()