import pickle
import numpy as np

MODEL_FILE = "models/delay_model.pkl"


def predict_delay(current_delay, station_index, remaining_stops, hour, day):
    with open(MODEL_FILE, "rb") as file:
        model = pickle.load(file)

    values = np.array([[current_delay, station_index, remaining_stops, hour, day]])
    result = model.predict(values)

    return round(result[0], 2)