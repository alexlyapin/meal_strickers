from tools import MealCard, generate_meal_stickers
from datetime import datetime

meals = [
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
    MealCard(
        name="John Doe",
        sandwich="Ham Ham Ham Ham Ham Ham Ham Ham Ham",
        bread="White",
        date=datetime.now(),
    ),
    MealCard(name="Jane Doe", sandwich="Cheese", bread="Brown", date=datetime.now()),
    MealCard(name="John Smith", sandwich="Tuna", bread="Corn", date=datetime.now()),
    MealCard(
        name="Jane Smith", sandwich="Egg", bread="Gluten free", date=datetime.now()
    ),
]


if __name__ == "__main__":
    canvas = generate_meal_stickers(meals, "Meal_Stickers.pdf")
