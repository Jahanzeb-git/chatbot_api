Project Title: FastAPI-Powered AI Chatbot with API Key Management and Rate Limiting
Overview
This project is a FastAPI-based application that provides an AI-powered chatbot using Hugging Face's inference API. The application includes features for managing API keys, rate-limiting requests, and handling user interactions securely. It is designed for developers looking to integrate AI chatbot functionality into their applications with robust access control mechanisms.

Features
AI-Powered Chatbot:

Leverages Hugging Face's InferenceClient to provide AI-driven responses.
Pre-configured with a system prompt to act as a knowledgeable assistant for data science, AI, and general knowledge.
API Key Management:

Generates unique, one-time API keys for users.
Tracks used API keys to prevent reuse and unauthorized access.
Prevents multiple API key generation requests from the same IP address.
Rate Limiting:

Limits the number of requests per IP address (e.g., 100 requests/day and 20 requests/minute) using slowapi.
Error Handling and Logging:

Captures and logs errors related to HTTP requests, API key usage, and server exceptions.
Logs stored in app.log for debugging and monitoring.
Secure Environment:

Uses .env files to store sensitive information like API keys.
Ensures sensitive files are ignored using .gitignore.


API Endpoints
1. Generate API Key
URL: /generate_api
Method: GET
Description: Generates a one-time API key for users based on their IP address.

Response Example:

json
Copy code
{
    "One Time API key": "1a2b3C4d5E6f7G8h9I0J1K2L3M4N5O6",
    "Generation Time": "2024-11-23 15:45:00",
    "!": "Don't share this secret API key."
}
2. Generate AI Response
URL: /response
Method: POST
Headers:

x-api-key: User's API key
Body:

json
Copy code
{
    "system_prompt": "You are a helpful assistant.",
    "message": "What is the capital of France?",
    "tokens": 100
}
Response Example:

json
Copy code
{
    "role": "assistant",
    "content": "The capital of France is Paris."
}
Rate Limiting:

Maximum of 100 requests per day per IP.
Maximum of 20 requests per minute per IP.


Contact
For issues or inquiries, please reach out to:
Jahanzeb Ahmed
Email: jahanzebahmed.mail@gmail.com
GitHub: jahanzeb-git