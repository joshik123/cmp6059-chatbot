import os
import joblib
import pandas as pd

# AI Prediction Methods
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def evaluate_model(model, X_test, y_test):
    # Makes predictions
    predictions = model.predict(X_test)
    # Accuracy score
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    # Understanding Pattern
    r2 = r2_score(y_test, predictions)
    return mae, rmse, r2


def main():
    df = pd.read_csv("data/cleaned_train_data.csv")

    print("Loaded cleaned dataset")
    print("Rows:", len(df))
    
    #input information
    features = [
        "current_delay",
        "station_index",
        "remaining_stops",
        "arrival_hour",
        "day_of_week"
    ]
    
    #input and answers
    X = df[features]
    y = df["final_delay"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        #similiar examples
        "kNN Regressor": KNeighborsRegressor(n_neighbors=5),
        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )
    }
    # Tracks best model
    best_model = None
    best_name = ""
    best_mae = 999999

    print("\nModel Evaluation Results")
    print("------------------------")

    # Loops through all 3 models
    for name, model in models.items():
        model.fit(X_train, y_train)
    # checks perfromance
        mae, rmse, r2 = evaluate_model(model, X_test, y_test)
        
        print(f"{name}")
        print(f"MAE: {mae:.2f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"R2: {r2:.2f}")
        print()
    # keeps best model
        if mae < best_mae:
            best_mae = mae
            best_model = model
            best_name = name

    os.makedirs("models", exist_ok=True)
    joblib.dump(best_model, "models/delay_model.pkl")

    print("Best model:", best_name)
    print("Model saved to models/delay_model.pkl")


if __name__ == "__main__":
    main()