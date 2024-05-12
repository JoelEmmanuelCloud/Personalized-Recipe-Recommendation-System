import boto3
import json
import os
from dotenv import load_dotenv
from prompts import create_prompt, create_safety_mechanisms, validate_input

# Load environment variables
load_dotenv()

class RecipeAssistant:
    def __init__(self, model_id='anthropic.claude-v2'):
        self.bedrock_client = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            aws_session_token=os.getenv("AWS_SESSION_TOKEN")
        )
        self.model_id = model_id
        self.context = "You are a culinary assistant designed to provide recipe suggestions."

    def invoke_model(self, ingredients, cuisine):
        if not validate_input(ingredients, cuisine):
            return "Please focus on ingredients and cuisines. What can I help you with today?"

        user_prompt = create_prompt(ingredients, cuisine)
        system_context = f"{self.context}. Safety guidance: {create_safety_mechanisms()['guidance']}"

        full_prompt = f"System: {system_context}\n\nHuman: {user_prompt}\n\nAssistant:"
        body = json.dumps({"prompt": full_prompt, "max_tokens_to_sample": 200})

        response = self.bedrock_client.invoke_model(
            modelId=self.model_id, body=body, contentType='application/json', accept='application/json'
        )
        response_body = json.loads(response['body'].read().decode('utf-8'))

        return response_body.get('completion', "No relevant suggestions found.")

def main():
    assistant = RecipeAssistant()
    while True:
        cuisine = input("Enter your preferred cuisine or 'exit': ")
        if cuisine.lower() == 'exit':
            break
        ingredients = input("Enter the ingredients you have (comma-separated): ").split(',')
        suggestions = assistant.invoke_model(ingredients, cuisine)
        print("Here are some recipe suggestions for you:")
        print(suggestions)

if __name__ == "__main__":
    main()