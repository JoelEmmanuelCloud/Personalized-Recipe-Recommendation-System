# Personalized Recipe Recommendation System

## Overview
This project implements a personalized recipe recommendation system using the Anthropic Claude model from Amazon Bedrock. It generates recipe suggestions based on user-specified ingredients and cuisine preferences. The system also includes safety and guidance mechanisms to ensure focused and appropriate interactions.

## Installation

### Prerequisites
- Python 3.8 or higher
- Boto3
- python-dotenv

### Setup
1. Clone this repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install boto3 python-dotenv

## Configure your AWS credentials:
You will need `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`.

These should be set in a .env file in the root directory of the project as follows:

```bash
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_SESSION_TOKEN=your_session_token
```

## Usage
To use the recipe assistant:

1. Navigate to the project directory.
2. Run the script using:

   ```bash
   python main.py
   ```

3. Follow the on-screen prompts to enter your preferred cuisine and the ingredients you have.

## Example
```bash
- Enter your preferred cuisine or 'exit': Italian
- Enter the ingredients you have (comma-separated): tomato, basil, garlic
- Here are some recipe suggestions for you:
[Generated suggestions based on the input]

```

## Additional Information
- **Safety and Guidance**: The system ensures that all inputs are strictly related to food and cooking to maintain the focus and appropriateness of interactions.
- **Input Validation**: The system validates that only alphanumeric characters are used for ingredients and alphabetic characters for cuisine, ensuring clean and expected inputs.
- **Model Interaction**: This system uses the anthropic.claude-v2 model through AWS's Bedrock service to generate responses based on the context set by the user's inputs.