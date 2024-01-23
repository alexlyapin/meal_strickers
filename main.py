from reader import parse_excel_sheet, parse_pricelist
from tools import generate_meal_stickers, generate_estimates
from datetime import datetime

if __name__ == "__main__":
    file_path = "tmp/NEW - SiTime Lunch Order Sheet and Office Registration.xlsx"
    pricelist_path = "pricelist.xlsx"
    sheet_name = "16-1"

    # generate stickers
    meal_cards = parse_excel_sheet(file_path, sheet_name)
    date = datetime.strptime(sheet_name, "%d-%m")
    filename = f"SiTime_Meal_Stickers_{date.strftime('%b_%d')}.pdf"
    generate_meal_stickers(meal_cards, f"tmp/{filename}", date)

    # generate estimates
    pricelist = parse_pricelist(pricelist_path)
    filename = f"SiTime_Meal_Estimates_{date.strftime('%b_%d')}.xlsx"
    generate_estimates(meal_cards, pricelist, f"tmp/{filename}")
