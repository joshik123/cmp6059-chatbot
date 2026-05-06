import joblib
import numpy as np

MODEL_FILE = "models/delay_model.pkl"

def predict_delay(current_delay, station_index, remaining_stops, hour, day):
    model = joblib.load("models/delay_model.pkl")

    data = np.array([[current_delay, station_index, remaining_stops, hour, day]])
    prediction = model.predict(data)

    return round(float(prediction[0]), 2)