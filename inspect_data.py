import pandas as pd

df = pd.read_excel("2024_WEY2WAT.xlsx")

print("\n--- COLUMNS ---")
print(df.columns)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())