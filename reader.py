import pandas as pd
from tools import MealCard
from datetime import datetime


def parse_excel_sheet(file_path, sheet_name):
    meal_cards = []
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # drop rows with nan values
    df.dropna(how="all", inplace=True)

    for _, row in df.iterrows():
        person = row["Person"]
        sandwich = row["Sandwich"]
        bread = row["Bread"]

        meal_cards.append(
            MealCard(name=person, sandwich=sandwich, bread=bread, date=datetime.now())
        )
    return meal_cards


# Example usage
file_path = "Meals.xlsx"
sheet_name = "11-2"
meal_cards = parse_excel_sheet(file_path, sheet_name)

for m in meal_cards:
    print(m)
