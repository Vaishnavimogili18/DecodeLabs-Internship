# Custom AI Chatbot with Memory

A conversational terminal-based AI chatbot built with Python and Google's Gemini API.

The chatbot maintains conversation history during a session, allowing it to remember previous messages and respond using the conversation context.

## Features

- Conversational AI using Gemini API
- In-memory conversation history
- Remembers previous user messages
- Clear conversation memory
- View conversation history
- Maximum conversation history limit
- System instructions for consistent behavior
- Error handling
- Error logging
- API key stored securely using environment variables

## Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv

## Project Structure

```text
custom-ai-chatbot/
│
├── .env
├── .gitignore
├── chatbot.log
├── chatbot.py
└── README.md
