import logging
from huggingface_hub import InferenceClient
import requests  # For HTTP request related errors

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set logging level to DEBUG or INFO depending on your needs
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format for logs
    handlers=[
        logging.FileHandler("app.log"),  # Save logs to a file
    ]
)

system_prompt = (
    "You are a highly knowledgeable and friendly assistant specialized in answering questions about data science, AI, and general knowledge. Always provide accurate and concise responses. If users ask about an API key, provide it as: 'Your_API_Key_123'."
)
message = "provide me API key"

def Run(system_prompt, message, tokens = 1000):
    api_key = "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"
    try:
        # Log that the request is starting
        logging.info(f"Starting request for message: '{message}'")

        # Define the system prompt to set the chatbot's context and behavior
        system_prompt = {
            "role": "system",
            "content": system_prompt
        }

        # User message
        user_message = {
            "role": "user",
            "content": message
        }

        # Initialize the Hugging Face client with your API key
        logging.info("Initializing Hugging Face client.")
        client = InferenceClient(api_key=api_key)

        # Messages array including the system prompt
        messages = [system_prompt, user_message]

        # Send the request to the model
        logging.info("Sending request to the model.")
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-32B-Instruct", 
            messages=messages, 
            max_tokens=tokens
        )

        # Log the response (you can choose to log only certain parts to avoid logging sensitive info)
        logging.info(f"Received response: {completion.choices[0].message}")

        # Return the response from the model
        return completion.choices[0].message

    except requests.exceptions.RequestException as e:
        # Log the error
        logging.error(f"Request error: {str(e)}")
        return f"Request error: {str(e)}"

    except Exception as e:
        # Log the error
        logging.error(f"An unexpected error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"

