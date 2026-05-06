import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("data/cleaned_train_data.csv")

features = [
    "current_delay",
    "station_index",
    "remaining_stops",
    "arrival_hour",
    "day_of_week"
]

target = "final_delay"

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = joblib.load("models/delay_model.pkl")

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("Model Evaluation")
print("----------------")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

print()
print("Explanation:")
print("MAE shows the average error in minutes.")
print("RMSE gives more penalty to large errors.")
print("R2 shows how well the model explains the delay pattern.")