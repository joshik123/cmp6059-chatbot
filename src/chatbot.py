from datetime import datetime, timedelta
from src.predictor import predict_delay
from src.stations import check_station


def ask_number(question):
    while True:
        answer = input(question)

        try:
            return float(answer)
        except ValueError:
            print("Please enter a number.")


def ask_station(question):
    while True:
        answer = input(question)
        station = check_station(answer)

        if station is not None:
            return station

        print("Sorry, I do not recognise that station. Please try again.")


def ask_time(question):
    while True:
        answer = input(question)

        try:
            return datetime.strptime(answer, "%H:%M")
        except ValueError:
            print("Please enter the time in HH:MM format, for example 14:30.")


def run_chatbot():
    print("Train Delay Chatbot")
    print("I can help predict your train arrival delay.")
    print()

    train = input("Which train are you on? ")

    current_station = ask_station("Where is the train now? ")
    destination = ask_station("Where are you travelling to? ")

    current_delay = ask_number("How many minutes delayed is the train? ")
    station_index = ask_number("What station number is this in the journey? ")
    remaining_stops = ask_number("How many stops are left? ")
    hour = ask_number("What hour is it now? Use 24 hour time: ")
    day = ask_number("What day is it? Monday=0, Tuesday=1, Sunday=6: ")

    scheduled_arrival = ask_time(
        "What is the scheduled arrival time? Example 14:30: "
    )

    predicted_delay = predict_delay(
        current_delay,
        station_index,
        remaining_stops,
        hour,
        day
    )

    new_arrival_time = scheduled_arrival + timedelta(minutes=predicted_delay)

    print()
    print("Journey Summary")
    print("---------------")
    print(f"Train: {train}")
    print(f"Current station: {current_station}")
    print(f"Destination: {destination}")
    print(f"Current delay: {current_delay} minutes")
    print(f"Predicted final delay: {predicted_delay} minutes")
    print(f"Estimated arrival time: {new_arrival_time.strftime('%H:%M')}")

    if predicted_delay <= 5:
        print("This is a minor delay.")
    elif predicted_delay <= 15:
        print("This is a moderate delay.")
    else:
        print("This is a significant delay.")


if __name__ == "__main__":
    run_chatbot()
    
