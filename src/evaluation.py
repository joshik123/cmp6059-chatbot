import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Loading data...")

# Load dataset
data = pd.read_csv("data/cleaned_train_data.csv")

# Features and target
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

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load trained model
model = joblib.load("models/delay_model.pkl")

# Make predictions
predictions = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("\nEvaluation Results")
print("------------------")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 2))

print("\nExplanation:")
print("MAE = average error in minutes")
print("RMSE = gives more penalty to large errors")
print("R2 = how well the model explains delay patterns")