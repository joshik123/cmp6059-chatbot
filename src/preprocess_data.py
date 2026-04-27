import pandas as pd


WATERLOO_CODE = "WAT"


def time_to_minutes(t):
    if pd.isna(t):
        return None

    try:
        h, m, s = str(t).split(":")
        return int(h) * 60 + int(m)
    except:
        return None


df = pd.read_excel("data/2024_WEY2WAT.xlsx")

df["planned_arrival_mins"] = df["planned_arrival_time"].apply(time_to_minutes)
df["actual_arrival_mins"] = df["actual_arrival_time"].apply(time_to_minutes)
df["arrival_delay"] = df["actual_arrival_mins"] - df["planned_arrival_mins"]

# remove rows where delay cannot be calculated
df = df.dropna(subset=["arrival_delay"])

# create station order from the data
station_order = list(df["location"].drop_duplicates())
station_to_index = {station: i for i, station in enumerate(station_order)}

df["station_index"] = df["location"].map(station_to_index)
waterloo_index = station_to_index[WATERLOO_CODE]

df["remaining_stops"] = waterloo_index - df["station_index"]
df["day_of_week"] = df["date_of_service"].dt.dayofweek
df["arrival_hour"] = df["planned_arrival_mins"] // 60

# get final delay at Waterloo for each train
waterloo_rows = df[df["location"] == WATERLOO_CODE]
targets = waterloo_rows.groupby("rid")["arrival_delay"].last().reset_index()
targets.columns = ["rid", "final_delay"]

# merge final delay onto every station row
dataset = pd.merge(df, targets, on="rid")

# keep only stations before Waterloo
dataset = dataset[dataset["remaining_stops"] > 0]

dataset = dataset[
    [
        "rid",
        "location",
        "arrival_delay",
        "station_index",
        "remaining_stops",
        "arrival_hour",
        "day_of_week",
        "final_delay",
    ]
]

dataset.rename(columns={
    "location": "current_station",
    "arrival_delay": "current_delay"
}, inplace=True)

dataset.to_csv("data/cleaned_train_data.csv", index=False)

print("Cleaned dataset saved.")
print(dataset.head())
print("Rows:", len(dataset))