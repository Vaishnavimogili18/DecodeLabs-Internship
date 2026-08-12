from dotenv import load_dotenv
from google import genai
import os
import logging


# -------------------------
# Logging configuration
# -------------------------

logging.basicConfig(
    filename="chatbot.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------
# System instruction
# -------------------------

SYSTEM_INSTRUCTION = """
You are a helpful AI assistant.

Your job is to help the user learn programming and technology.

Rules:

1. Explain concepts clearly and simply.
2. Give examples when useful.
3. If the user asks for coding help, explain the logic before giving the complete solution.
4. Be encouraging but do not give unnecessary information.
5. Remember the conversation context provided by the application.
"""


# -------------------------
# Memory configuration
# -------------------------

MAX_HISTORY = 10


# -------------------------
# Create Gemini client
# -------------------------

def create_client():

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in .env file"
        )

    return genai.Client(
        api_key=api_key
    )


# -------------------------
# Add user message
# -------------------------

def add_user_message(history, message):

    history.append({
        "role": "user",
        "parts": [
            {
                "text": message
            }
        ]
    })


# -------------------------
# Add AI message
# -------------------------

def add_ai_message(history, message):

    history.append({
        "role": "model",
        "parts": [
            {
                "text": message
            }
        ]
    })


# -------------------------
# Limit conversation memory
# -------------------------

def limit_history(history):

    if len(history) > MAX_HISTORY:

        del history[:-MAX_HISTORY]


# -------------------------
# Get AI response
# -------------------------

def get_ai_response(client, history):

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=history,
            config={
                "system_instruction": SYSTEM_INSTRUCTION
            }
        )

        return response.text

    except Exception as e:

        logging.error(
            "Gemini API error: %s",
            e,
            exc_info=True
        )

        return None


# -------------------------
# Show conversation history
# -------------------------

def show_history(history):

    print("\n--- Conversation History ---")

    if not history:

        print("No conversation yet.")

    for message in history:

        role = message["role"]
        text = message["parts"][0]["text"]

        if role == "user":

            print("You:", text)

        elif role == "model":

            print("AI:", text)

    print("----------------------------\n")


# -------------------------
# Main application
# -------------------------

def main():

    client = create_client()

    conversation_history = []

    print("================================")
    print("       CUSTOM AI CHATBOT")
    print("================================")
    print("Type 'exit' to quit.")
    print("Type 'clear' to erase memory.")
    print("Type 'history' to view memory.")
    print()

    while True:

        user_input = input("You: ").strip()

        # -------------------------
        # Exit
        # -------------------------

        if user_input.lower() == "exit":

            print("Goodbye!")

            break

        # -------------------------
        # Clear memory
        # -------------------------

        if user_input.lower() == "clear":

            conversation_history.clear()

            print("Memory cleared!\n")

            continue

        # -------------------------
        # Show history
        # -------------------------

        if user_input.lower() == "history":

            show_history(conversation_history)

            continue

        # -------------------------
        # Empty input
        # -------------------------

        if not user_input:

            print("Please enter something.\n")

            continue

        # -------------------------
        # Add user message
        # -------------------------

        add_user_message(
            conversation_history,
            user_input
        )

        limit_history(conversation_history)

        # -------------------------
        # Get AI response
        # -------------------------

        ai_response = get_ai_response(
            client,
            conversation_history
        )

        # -------------------------
        # API error
        # -------------------------

        if ai_response is None:

            print(
                "⚠️ Something went wrong "
                "while contacting Gemini."
            )

            conversation_history.pop()

            print("Please try again.\n")

            continue

        # -------------------------
        # Add AI response
        # -------------------------

        add_ai_message(
            conversation_history,
            ai_response
        )

        limit_history(conversation_history)

        # -------------------------
        # Display response
        # -------------------------

        print("AI:", ai_response)

        print()


# -------------------------
# Program entry point
# -------------------------

if __name__ == "__main__":

    main()