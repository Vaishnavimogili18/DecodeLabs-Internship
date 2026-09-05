import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ==========================================
# LOAD API KEY
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Intelligent Code Reviewer",
    page_icon="💻",
    layout="wide"
)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("💻 Code Reviewer")

    st.write(
        "An AI-powered developer utility "
        "for reviewing and explaining code."
    )

    st.divider()

    st.subheader("✨ Features")

    st.write("🐛 Bug Detection")
    st.write("💡 Code Explanation")
    st.write("⚡ Code Optimization")
    st.write("📂 File Upload")
    st.write("🔍 Automatic Language Detection")

    st.divider()

    st.caption("Powered by Gemini AI")


# ==========================================
# CODE REVIEW FUNCTION
# ==========================================

def review_code(code, language):

    system_instruction = """
You are an expert software developer and code reviewer.

Analyze the code provided by the user.

Your response must contain exactly these three sections:

## 🐛 Bug Report

Identify:
- Syntax errors
- Logical errors
- Runtime errors
- Bad coding practices
- Potential problems

If there are no major bugs, say:
No major bugs found.

## 💡 Code Explanation

Explain what the code does in simple language
that a beginner can understand.

## ⚡ Optimized Code

Provide an improved version of the code.

Keep the same overall purpose of the original code.

Put the improved code inside a Markdown code block.

Do not invent bugs that do not exist.
"""

    prompt = (
        "Programming Language: " + language + "\n\n"
        "Here is the code that needs to be reviewed:\n\n"
        + code
        + "\n\nReview this code according to the instructions."
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=system_instruction + "\n\n" + prompt
    )

    return response.text


# ==========================================
# MAIN TITLE
# ==========================================

st.title("💻 Intelligent Code Reviewer & Explainer")

st.markdown(
    "Analyze your code with **Gemini AI** and get "
    "bug detection, simple explanations, and optimized code."
)

st.divider()


# ==========================================
# FILE UPLOAD
# ==========================================

st.subheader("📂 Upload Your Code")

uploaded_file = st.file_uploader(
    "Supported files: Python (.py), Java (.java), JavaScript (.js)",
    type=["py", "java", "js"]
)


# ==========================================
# LANGUAGE DETECTION
# ==========================================

if uploaded_file is not None:

    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension == "py":
        language = "python"

    elif file_extension == "java":
        language = "java"

    elif file_extension == "js":
        language = "javascript"

    st.success(
        f"✅ File uploaded: {uploaded_file.name}"
    )

    st.info(
        f"🔍 Detected language: **{language}**"
    )

else:

    language = st.selectbox(
        "Select Programming Language",
        ["python", "java", "javascript"]
    )


# ==========================================
# CODE INPUT
# ==========================================

st.subheader("📝 Your Code")

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    st.code(
        code,
        language=language
    )

else:

    code = st.text_area(
        "Paste your code below:",
        height=300,
        placeholder="Paste your Python, Java, or JavaScript code here..."
    )


# ==========================================
# REVIEW BUTTON
# ==========================================

st.divider()

if st.button(
    "🔍 Review Code",
    use_container_width=True
):

    if not code.strip():

        st.warning(
            "⚠️ Please upload a file or enter some code first."
        )

    else:

        with st.spinner(
            "🤖 Gemini is analyzing your code..."
        ):

            try:

                result = review_code(
                    code,
                    language
                )

                st.success(
                    "✅ Code review completed!"
                )

                st.divider()

                st.subheader("📊 AI Code Review")

                st.markdown(result)

            except Exception as e:

                st.error(
                    "❌ Something went wrong:\n\n"
                    + str(e)
                )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Intelligent Code Reviewer & Explainer • "
    "Built with Python, Streamlit and Gemini AI"
)
