stations = {
    "weymouth": "Weymouth",
    "southampton": "Southampton Central",
    "southampton central": "Southampton Central",
    "bournemouth": "Bournemouth",
    "winchester": "Winchester",
    "basingstoke": "Basingstoke",
    "waterloo": "London Waterloo",
    "london waterloo": "London Waterloo"
}


def check_station(name):
    name = name.lower().strip()

    if name in stations:
        return stations[name]

    return None