
# Multimodal Image Generation Studio

An AI-powered Python application that converts natural language descriptions into digital artwork using a text-to-image API.

The application allows users to enter an image prompt and configure the image aspect ratio, resolution, and number of images to generate. Generated images are saved locally and displayed to the user.

## 🚀 Features

* Generate images from natural-language prompts
* Text-to-image API integration
* Multiple image generation
* Aspect ratio selection
* Resolution selection
* Input validation
* Automatic output directory creation
* Save generated images locally
* Display generated images
* Secure API key management using environment variables

## 🛠️ Technologies Used

* Python
* Hugging Face Inference Providers
* Hugging Face Hub Python SDK
* FLUX.1-schnell
* Pillow
* python-dotenv

## ⚙️ How It Works

The application follows this workflow:

1. User enters a natural-language image description.
2. User selects an aspect ratio.
3. User selects the desired resolution.
4. User specifies the number of images.
5. The application validates the inputs.
6. The prompt is sent to the image-generation API.
7. The generated image is received as image data.
8. The image is saved as a PNG file.
9. The generated image is displayed to the user.

## 📐 Supported Settings

### Aspect Ratios

The application supports:

* `1:1`
* `16:9`
* `9:16`

### Resolutions

The application supports:

* `512`
* `768`
* `1024`

### Image Count

Users can generate between:

* 1 and 4 images

## 📁 Project Structure

```text
Multimodal-Image-Generation/
│
├── image_generator.py
├── README.md
├── .gitignore
├── .env
│
└── outputs/
    └── generated_image_1.png
```

> `.env` and `.venv` should not be uploaded to GitHub.

## 🔑 Environment Setup

Create a `.env` file in the project directory:

```text
HF_TOKEN=your_huggingface_token
```

Never share your API token publicly.

## 📦 Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install huggingface_hub python-dotenv pillow
```

## ▶️ Run the Application

Run:

```bash
python image_generator.py
```

The application will ask for:

```text
Enter your image description:
Enter aspect ratio (1:1 / 16:9 / 9:16):
Enter resolution (512 / 768 / 1024):
How many images do you want?
```

Generated images are saved inside the `outputs` folder.

## 🔒 Security

API credentials are loaded from environment variables instead of being written directly into the Python source code.

The `.gitignore` file prevents `.env` and `.venv` from being committed to the repository.

## 🎯 Internship Project

This project was developed as part of a Generative AI internship project focused on text-to-image generation and handling generated image data.

## 👩‍💻 Author

Vaishnavi Mogili
