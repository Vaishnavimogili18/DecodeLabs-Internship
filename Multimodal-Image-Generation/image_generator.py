from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os


# --------------------------------
# 1. Load Environment Variables
# --------------------------------

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN not found in .env")


# --------------------------------
# 2. Create Hugging Face Client
# --------------------------------

client = InferenceClient(
    provider="fal-ai",
    api_key=hf_token
)


# --------------------------------
# 3. Get User Input
# --------------------------------

print("=" * 60)
print("        MULTIMODAL IMAGE GENERATION STUDIO")
print("=" * 60)
prompt = input("\nEnter your image description: ").strip()

if not prompt:
    print("Error: Prompt cannot be empty.")
    exit()


aspect_ratio = input(
    "Enter aspect ratio (1:1 / 16:9 / 9:16): "
).strip()

if aspect_ratio not in ["1:1", "16:9", "9:16"]:
    print("Error: Invalid aspect ratio.")
    exit()


try:
    resolution = int(
        input("Enter resolution (512 / 768 / 1024): ")
    )

except ValueError:
    print("Error: Resolution must be a number.")
    exit()


if resolution not in [512, 768, 1024]:
    print("Error: Resolution must be 512, 768, or 1024.")
    exit()


try:
    count = int(
        input("How many images do you want? ")
    )

except ValueError:
    print("Error: Image count must be a number.")
    exit()


if count < 1 or count > 4:
    print("Error: Image count must be between 1 and 4.")
    exit()


# --------------------------------
# 4. Calculate Image Dimensions
# --------------------------------

if aspect_ratio == "1:1":

    width = resolution
    height = resolution

elif aspect_ratio == "16:9":

    width = resolution
    height = int(resolution * 9 / 16)

elif aspect_ratio == "9:16":

    width = int(resolution * 9 / 16)
    height = resolution

else:

    print("Invalid aspect ratio.")
    exit()


# --------------------------------
# 5. Display Settings
# --------------------------------

print("\n" + "=" * 60)
print("Generation Settings")
print("=" * 60)

print(f"Prompt       : {prompt}")
print(f"Aspect Ratio : {aspect_ratio}")
print(f"Resolution   : {resolution}")
print(f"Width        : {width}")
print(f"Height       : {height}")
print(f"Image Count  : {count}")


# --------------------------------
# 6. Generate Images
# --------------------------------

for i in range(count):

    print(f"\nGenerating image {i + 1} of {count}...")

    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell",
        width=width,
        height=height
    )

    # Create output folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/generated_image_{i + 1}.png"

    image.save(filename)

    print(f"Image saved: {filename}")

    # Display generated image
    image.show()


# --------------------------------
# 7. Completion Message
# --------------------------------

print("\n" + "=" * 60)
print("Image generation completed successfully!")
print("=" * 60)