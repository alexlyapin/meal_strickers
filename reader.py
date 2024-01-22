import pandas as pd
from tools import MealCard
from datetime import datetime
from numpy import isnan


def parse_excel_sheet(file_path, sheet_name):
    meal_cards = []

    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
        skiprows=range(1, 3),
        usecols=range(3),
        header=1,
    )
    # drop rows with nan values
    df.dropna(how="all", inplace=True)

    for _, row in df.iterrows():
        person = row["Employee Name"]
        sandwich = row["Sandwich"]
        bread = row["Bread Option"]

        meal_cards.append(
            MealCard(
                name=person,
                sandwich=sandwich,
                bread=bread if isinstance(bread, str) else "",
            )
        )
    return meal_cards


if __name__ == "__main__":
    # Example usage
    file_path = "tmp/NEW - SiTime Lunch Order Sheet and Office Registration.xlsx"
    sheet_name = "16-1"
    meal_cards = parse_excel_sheet(file_path, sheet_name)

    for m in meal_cards:
        print(m)
