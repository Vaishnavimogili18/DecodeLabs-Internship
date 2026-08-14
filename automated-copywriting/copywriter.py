from dotenv import load_dotenv
from google import genai
import os
from datetime import datetime


# ============================================================
# GET FLOAT INPUT
# ============================================================

def get_float_input(prompt, minimum, maximum):

    while True:

        try:

            value = float(input(prompt))

            if minimum <= value <= maximum:

                return value

            print(
                f"Please enter a value between "
                f"{minimum} and {maximum}."
            )

        except ValueError:

            print("Please enter a valid number.")


# ============================================================
# GET TEXT INPUT
# ============================================================

def get_text_input(prompt):

    while True:

        value = input(prompt).strip()

        if value:

            return value

        print("Please enter a value. It cannot be empty.")


# ============================================================
# GET MENU CHOICE
# ============================================================

def get_menu_choice(prompt, minimum, maximum):

    while True:

        choice = input(prompt).strip()

        if choice.isdigit():

            choice = int(choice)

            if minimum <= choice <= maximum:

                return choice

        print(
            f"Please enter a number between "
            f"{minimum} and {maximum}."
        )


# ============================================================
# GET YES / NO INPUT
# ============================================================

def get_yes_no(prompt):

    while True:

        choice = input(prompt).strip().lower()

        if choice in ("y", "n"):

            return choice

        print(
            "Please enter 'y' for yes or 'n' for no."
        )
def show_history(history):

    print("\n" + "=" * 60)
    print("                 GENERATION HISTORY")
    print("=" * 60)

    if not history:

        print("No generations yet.")

        print("=" * 60)

        return

    for i, item in enumerate(history, start=1):

        print(f"\n[{i}] {item['product']}")

        print(f"Platform    : {item['platform']}")

        print(f"Tone        : {item['tone']}")

        print(f"Temperature : {item['temperature']}")

        print(f"Top P       : {item['top_p']}")

        print("-" * 60)

        print(item["copy"])

    print("=" * 60)
def show_single_history(history, number):

    if number < 1 or number > len(history):

        print(
            f"\n❌ Invalid history number."
            f" Choose between 1 and {len(history)}."
        )

        return

    item = history[number - 1]

    print("\n" + "=" * 60)

    print(
        f"              GENERATION {number}"
    )

    print("=" * 60)

    print(
        f"Product     : {item['product']}"
    )

    print(
        f"Platform    : {item['platform']}"
    )

    print(
        f"Tone        : {item['tone']}"
    )

    print(
        f"Temperature : {item['temperature']}"
    )

    print(
        f"Top P       : {item['top_p']}"
    )

    print("\n" + "-" * 60)

    print(item["copy"])

    print("=" * 60)

def show_help():
        print("\n" + "=" * 60)
        print("                    AVAILABLE COMMANDS")
        print("=" * 60)

        print("\nhistory")
        print("    Show all generated copies.")

        print("\nhistory <number>")
        print("    Show a specific generated copy.")

        print("\nclear-history")
        print("    Clear current session history.")

        print("\nhelp")
        print("    Show available commands.")

        print("=" * 60)
# ============================================================
# SAVE GENERATED COPY
# ============================================================

def save_copy(
    product_name,
    platform,
    tone,
    temperature,
    top_p,
    generated_copy
):

    filename = "marketing_copy.txt"

    with open(filename, "a", encoding="utf-8") as file:

        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("GENERATED MARKETING COPY\n")
        file.write("=" * 60 + "\n")

        file.write(
            f"Date: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        file.write(
            f"Product: {product_name}\n"
        )

        file.write(
            f"Platform: {platform}\n"
        )

        file.write(
            f"Tone: {tone}\n"
        )

        file.write(
            f"Temperature: {temperature}\n"
        )

        file.write(
            f"Top P: {top_p}\n"
        )

        file.write("\n")

        file.write(generated_copy)

        file.write("\n")

        file.write("=" * 60 + "\n")

    print(
        "\n✅ Copy saved to marketing_copy.txt"
    )


# ============================================================
# GENERATE MARKETING COPY
# ============================================================

def generate_copy(
    client,
    prompt,
    temperature,
    top_p
):

    try:

        response = client.models.generate_content(

            model="gemini-3.5-flash-lite",

            contents=prompt,

            config={
                "temperature": temperature,
                "top_p": top_p
            }
        )

        return response.text

    except Exception as e:

        print(
            "\n⚠️ Something went wrong "
            "while contacting Gemini."
        )

        print(
            "Please check your internet connection "
            "and try again."
        )

        print("\nError details:")

        print(e)

        return None


# ============================================================
# LOAD API KEY
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


if not api_key:

    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )


client = genai.Client(
    api_key=api_key
)


# ============================================================
# GENERATION HISTORY
# ============================================================

generation_history = []


# ============================================================
# APPLICATION HEADER
# ============================================================

print("\n" + "=" * 60)

print(
    "       AUTOMATED COPYWRITING & TONE TRANSFORMER"
)

print("=" * 60)

print(
    "Generate marketing copy for different platforms."
)

print("=" * 60)


# ============================================================
# MAIN APPLICATION LOOP
# ============================================================

while True:

    print("\n" + "=" * 60)
    print("Commands:")
    print("  history")
    print("  history <number>")
    print("  clear-history")
    print("  help")
    print("  exit")
    print("=" * 60)

    command = input(
        "\nEnter command or press Enter to create copy: "
    ).strip().lower()

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if command == "exit":

        print("\nGoodbye!")

        break


    # --------------------------------------------------------
    # HISTORY
    # --------------------------------------------------------

    if command == "history":

        show_history(
            generation_history
        )

        continue


    # --------------------------------------------------------
    # SINGLE HISTORY
    # --------------------------------------------------------

    if command.startswith("history "):

        parts = command.split()

        if len(parts) == 2 and parts[1].isdigit():

            history_number = int(parts[1])

            show_single_history(
                generation_history,
                history_number
            )

        else:

            print(
                "\n❌ Usage: history <number>"
            )

        continue


    # --------------------------------------------------------
    # CLEAR HISTORY
    # --------------------------------------------------------

    if command == "clear-history":

        generation_history.clear()

        print(
            "\n✅ Generation history cleared."
        )

        continue


    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    if command == "help":

        show_help()

        continue
    # --------------------------------------------------------
    # PRODUCT INPUT
    # --------------------------------------------------------

    product_name = get_text_input(
        "\nProduct Name: "
    )

    product_description = get_text_input(
        "Product Description: "
    )


    # --------------------------------------------------------
    # PLATFORM SELECTION
    # --------------------------------------------------------

    print("\nChoose a platform:")

    print("1. LinkedIn")
    print("2. Instagram")
    print("3. Email")

    platform_choice = get_menu_choice(
        "Enter your choice (1-3): ",
        1,
        3
    )


    if platform_choice == 1:

        platform = "LinkedIn"

    elif platform_choice == 2:

        platform = "Instagram"

    else:

        platform = "Email"


    # --------------------------------------------------------
    # TONE SELECTION
    # --------------------------------------------------------

    print("\nChoose a tone:")

    print("1. Professional")
    print("2. Friendly")
    print("3. Persuasive")
    print("4. Exciting")

    tone_choice = get_menu_choice(
        "Enter your choice (1-4): ",
        1,
        4
    )


    if tone_choice == 1:

        tone = "Professional"

    elif tone_choice == 2:

        tone = "Friendly"

    elif tone_choice == 3:

        tone = "Persuasive"

    else:

        tone = "Exciting"


    # --------------------------------------------------------
    # MODEL PARAMETERS
    # --------------------------------------------------------

    temperature = get_float_input(
        "Temperature (0.0 - 2.0): ",
        0.0,
        2.0
    )

    top_p = get_float_input(
        "Top P (0.0 - 1.0): ",
        0.0,
        1.0
    )


    # --------------------------------------------------------
    # PLATFORM-SPECIFIC INSTRUCTIONS
    # --------------------------------------------------------

    if platform == "LinkedIn":

        platform_instruction = """
Create a professional LinkedIn post.

Focus on:
- Business value
- Credibility
- Clear product benefits
- A strong opening
- A professional call to action

Keep the formatting suitable for LinkedIn.
"""


    elif platform == "Instagram":

        platform_instruction = """
Create an engaging Instagram caption.

Focus on:
- Attention-grabbing opening
- Product benefits
- Engaging language
- Clear call to action
- A few relevant emojis
- Relevant hashtags
"""


    elif platform == "Email":

        platform_instruction = """
Create a marketing email.

Include:
- A compelling subject line
- Clear introduction
- Product benefits
- Strong call to action

Keep the email concise and professional.
"""


    # --------------------------------------------------------
    # DYNAMIC PROMPT TEMPLATE
    # --------------------------------------------------------

    prompt = f"""
Create professional marketing copy
for the following product.

Product Name:
{product_name}

Product Description:
{product_description}

Target Platform:
{platform}

Desired Tone:
{tone}

Platform-Specific Instructions:
{platform_instruction}

Match the requested tone.

Do not explain your process.

Return only the final marketing copy.
"""


    # --------------------------------------------------------
    # PROMPT PREVIEW
    # --------------------------------------------------------

    preview_choice = get_yes_no(
        "\nShow generated prompt before sending? (y/n): "
    )


    if preview_choice == "y":

        print("\n" + "=" * 60)

        print(
            "                  GENERATED PROMPT"
        )

        print("=" * 60)

        print(prompt)

        print("=" * 60)


    # --------------------------------------------------------
    # GENERATE COPY
    # --------------------------------------------------------

    generated_copy = generate_copy(
        client,
        prompt,
        temperature,
        top_p
    )


    # --------------------------------------------------------
    # HANDLE API ERROR
    # --------------------------------------------------------

    if generated_copy is None:

        print(
            "\nCopy generation failed."
        )

        retry = get_yes_no(
            "Try again? (y/n): "
        )

        if retry == "y":

            continue

        else:

            break


    # --------------------------------------------------------
    # ADD SUCCESSFUL GENERATION TO HISTORY
    # --------------------------------------------------------

    generation_history.append({

        "product": product_name,

        "platform": platform,

        "tone": tone,

        "temperature": temperature,

        "top_p": top_p,

        "copy": generated_copy

    })


    # --------------------------------------------------------
    # DISPLAY GENERATED COPY
    # --------------------------------------------------------

    print("\n" + "=" * 60)

    print(
        "              GENERATED MARKETING COPY"
    )

    print("=" * 60)


    print(
        f"Platform    : {platform}"
    )

    print(
        f"Tone        : {tone}"
    )

    print(
        f"Temperature : {temperature}"
    )

    print(
        f"Top P       : {top_p}"
    )


    print("\n" + "-" * 60)

    print(generated_copy)

    print("=" * 60)


    # --------------------------------------------------------
    # SAVE COPY
    # --------------------------------------------------------

    save_choice = get_yes_no(
        "\nSave this copy to a file? (y/n): "
    )


    if save_choice == "y":

        save_copy(
            product_name,
            platform,
            tone,
            temperature,
            top_p,
            generated_copy
        )


    # --------------------------------------------------------
    # GENERATE ANOTHER COPY
    # --------------------------------------------------------

    again = get_yes_no(
        "\nGenerate another copy? (y/n): "
    )


    if again != "y":

        print(
            "\nThank you for using"
        )

        print(
            "Automated Copywriting & Tone Transformer!"
        )

        break