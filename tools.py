from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from pydantic import BaseModel
from datetime import datetime
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit


# Define a Pydantic model for the meal card
class MealCard(BaseModel):
    name: str
    sandwich: str
    bread: str
    date: datetime


def generate_meal_stickers(meals, filename):
    # Create a new PDF canvas with A4 size
    c = canvas.Canvas(filename, pagesize=A4)

    def insertTextBlock(text, font, size, x, y, width):
        c.setFont(font, size)
        lines = simpleSplit(text, font, size, width)
        text_y = y
        for line in lines:
            c.drawString(x, text_y, line)
            text_y -= size

    number_of_cards_per_width = 3
    number_of_cards_per_height = 7

    # Define card dimensions
    card_width = A4[0] / number_of_cards_per_width
    card_height = A4[1] / number_of_cards_per_height

    # Define label positions within each card
    sandwich_x = 0.1 * card_width
    sandwich_y = 0.5 * card_height

    bread_x = 0.1 * card_width
    bread_y = 0.2 * card_height

    # Define date position within each card
    date_x = 0.7 * card_width
    date_y = 0.7 * card_height

    # Define name position within each card
    name_x = 0.1 * card_width
    name_y = 0.7 * card_height

    # Loop through each card
    for meal_index, current_meal in enumerate(meals):
        # Calculate the row and column of the current card
        row = meal_index // number_of_cards_per_width
        col = meal_index % number_of_cards_per_width

        # Calculate the position of the current card
        card_x = col * card_width
        card_y = (
            (meal_index // (number_of_cards_per_width * number_of_cards_per_height))
            * number_of_cards_per_height
            + (number_of_cards_per_height - row - 1)
        ) * card_height

        # Draw the card rectangle
        c.rect(card_x, card_y, card_width, card_height, stroke=1)

        # Register the font
        pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
        pdfmetrics.registerFont(TTFont("ArialBd", "arialbd.ttf"))

        insertTextBlock(
            current_meal.name,
            "ArialBd",
            12,
            card_x + name_x,
            card_y + name_y,
            card_width - 2 * name_x,
        )

        insertTextBlock(
            current_meal.sandwich,
            "Arial",
            12,
            card_x + sandwich_x,
            card_y + sandwich_y,
            card_width - 2 * sandwich_x,
        )

        insertTextBlock(
            current_meal.bread,
            "Arial",
            12,
            card_x + bread_x,
            card_y + bread_y,
            card_width - 2 * bread_x,
        )

        c.setFont("ArialBd", 10)
        c.drawString(
            card_x + date_x, card_y + date_y, current_meal.date.strftime("%b-%d")
        )

        # Check if the current page is full
        if (
            meal_index % (number_of_cards_per_width * number_of_cards_per_height)
            == (number_of_cards_per_width * number_of_cards_per_height) - 1
        ):
            # Add a new page
            c.showPage()

    # Save the PDF file
    c.save()
