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


def run_chatbot():
    print("Train Delay Chatbot")
    print()

    train = input("Which train are you on? ")

    current_station = ask_station("Where is the train now? ")
    destination = ask_station("Where are you travelling to? ")

    current_delay = ask_number("How many minutes delayed is the train? ")
    station_index = ask_number("What station number is this in the journey? ")
    remaining_stops = ask_number("How many stops are left? ")


if __name__ == "__main__":
    run_chatbot()