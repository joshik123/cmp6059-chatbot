import pandas as pd


# convert HH:MM:SS → minutes
def time_to_minutes(t):
    if pd.isna(t):
        return None
    try:
        h, m, s = str(t).split(":")
        return int(h) * 60 + int(m)
    except:
        return None


# load dataset
df = pd.read_excel("data/2024_WEY2WAT.xlsx")

print("\nLoaded data successfully.\n")

# convert times
df["planned_arrival_mins"] = df["planned_arrival_time"].apply(time_to_minutes)
df["actual_arrival_mins"] = df["actual_arrival_time"].apply(time_to_minutes)

# calculate delay
df["arrival_delay"] = df["actual_arrival_mins"] - df["planned_arrival_mins"]

print("\n--- Sample delays ---")
print(df[["location", "arrival_delay"]].head())


# show all station codes (IMPORTANT)
print("\n--- Station codes ---")
print(df["location"].unique())


# ===== FIND WATERLOO CODE =====
# After running, replace "WAT" with the correct code if needed

WATERLOO_CODE = "WAT"   # <-- update if needed


# get final delay at destination
wat_df = df[df["location"] == WATERLOO_CODE]

target = wat_df.groupby("rid")["arrival_delay"].last().reset_index()
target.columns = ["rid", "final_delay"]

print("\n--- Target (final delay) ---")
print(target.head())


# get starting point (simple feature for now)
features = df.groupby("rid").first().reset_index()

features = features[["rid", "location", "arrival_delay", "date_of_service"]]

features.rename(columns={
    "location": "current_station",
    "arrival_delay": "current_delay"
}, inplace=True)


# merge features and target
dataset = pd.merge(features, target, on="rid")

print("\n--- Final dataset ---")
print(dataset.head())


# save cleaned dataset
dataset.to_csv("data/cleaned_train_data.csv", index=False)

print("\nCleaned dataset saved to data/cleaned_train_data.csv")