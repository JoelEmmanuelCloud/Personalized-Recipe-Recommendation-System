from pydantic import BaseModel

class InputData(BaseModel):
    ingredients: list
    cuisine: str

    @classmethod
    def validate(cls, ingredients: list, cuisine: str):
        # Check if all characters in each ingredient are alphanumeric (letters and numbers)
        if not all(ingredient.strip().replace(' ', '').isalnum() for ingredient in ingredients):
            raise ValueError("Ingredients should contain only alphanumeric characters.")
        # Check if cuisine input is appropriate
        if not cuisine.replace(' ', '').isalpha():
            raise ValueError("Cuisine should contain only alphabetic characters.")
        return cls(ingredients=ingredients, cuisine=cuisine)

def create_prompt(ingredients, cuisine):
    """Generate a prompt asking for recipes based on ingredients and cuisine."""
    ingredient_list = ', '.join(ingredients)
    return f"Considering these ingredients {ingredient_list}, what are some suitable recipes in the {cuisine} style?"

def create_safety_mechanisms():
    """Returns safety and guidance mechanisms."""
    return {
        "guidance": "Let's keep our focus on cooking! What type of cuisine or ingredients do you have today?",
        "content_filter": "We've implemented filters to prevent the processing of inappropriate or irrelevant content.",
        "input_validation": "All user inputs are checked to ensure they meet our expected format, focusing solely on food-related terms."
    }
