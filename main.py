from reader import parse_excel_sheet
from tools import MealCard, generate_meal_stickers
from datetime import datetime

if __name__ == "__main__":
    file_path = "tmp/NEW - SiTime Lunch Order Sheet and Office Registration.xlsx"
    sheet_name = "16-1"

    meal_cards = parse_excel_sheet(file_path, sheet_name)
    date = datetime.strptime(sheet_name, "%d-%m")
    filename = f"Meal_Stickers_{date.strftime('%b_%d')}.pdf"
    canvas = generate_meal_stickers(meal_cards, f"tmp/{filename}", date)
