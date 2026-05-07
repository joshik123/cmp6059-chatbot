import joblib
import numpy as np

MODEL_FILE = "models/delay_model.pkl"

def predict_delay(current_delay, station_index, remaining_stops, hour, day):
    #loads trained ai models
    model = joblib.load("models/delay_model.pkl")

    #prepares the data
    data = np.array([[current_delay, station_index, remaining_stops, hour, day]])
    prediction = model.predict(data)

    return round(float(prediction[0]), 2)