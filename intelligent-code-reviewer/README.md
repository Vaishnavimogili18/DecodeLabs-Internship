# 💻 Intelligent Code Reviewer & Explainer

An AI-powered developer utility that reviews source code, identifies bugs, explains code in simple language, and generates an improved version using **Google Gemini AI**.

## 🚀 Features

* 🐛 **Bug Detection** — Identifies syntax, logical, runtime, and potential coding issues.
* 💡 **Code Explanation** — Explains code in beginner-friendly language.
* ⚡ **Code Optimization** — Generates an improved version while maintaining the original purpose.
* 📂 **File Upload** — Supports `.py`, `.java`, and `.js` files.
* 🔍 **Automatic Language Detection** — Detects the programming language from the uploaded file extension.
* 📝 **Code Paste Support** — Users can directly paste code into the application.
* 🎨 **Markdown Rendering** — Displays explanations and code blocks with proper formatting.
* 🤖 **Gemini AI** — Uses Google's Gemini model for intelligent code analysis.
* 🌐 **Streamlit Interface** — Provides a simple and interactive web application.

## 🛠️ Technologies Used

* **Python**
* **Google Gemini API**
* **Streamlit**
* **python-dotenv**

## 📁 Project Structure

```text
intelligent-code-reviewer/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

> ⚠️ The `.env` file contains the Gemini API key and should never be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd intelligent-code-reviewer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the `.env` file

Create a file named `.env` in the project folder:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your own Gemini API key.

### 4. Run the application

```bash
streamlit run main.py
```

The application will open in your browser at the local Streamlit address.

## 🧑‍💻 How to Use

1. Open the application.
2. Upload a `.py`, `.java`, or `.js` file **or** paste code manually.
3. If a file is uploaded, the application automatically detects its programming language.
4. Click **🔍 Review Code**.
5. Gemini analyzes the code.
6. View the:

   * 🐛 Bug Report
   * 💡 Code Explanation
   * ⚡ Optimized Code

## 🔄 How It Works

```text
User Code
    ↓
File Upload / Code Input
    ↓
Convert Code to String
    ↓
Gemini AI
    ↓
Code Analysis
    ↓
Bug Report + Explanation + Optimized Code
    ↓
Markdown Rendering
    ↓
User
```

## 🧪 Example

### Input

```python
x = 10
y = 0

result = x / y

print(result)
```

### AI Review

The application can identify that dividing by zero causes a runtime error and provide an improved version that handles the situation safely.

## 🎯 Project Goal

The goal of this project is to create a developer-friendly AI utility that helps programmers understand their code, identify common problems, and improve code quality using natural-language AI assistance.

## 🔮 Future Improvements

* Support additional programming languages.
* Add code complexity analysis.
* Add security vulnerability detection.
* Add coding best-practice recommendations.
* Add side-by-side original and optimized code comparison.
* Add downloadable code-review reports.
* Add syntax-aware code analysis.
* Add GitHub repository integration.

## 👩‍💻 Author

**Vaishnavi Mogili**

Computer Science & Engineering Student

---

⭐ If you find this project useful, consider giving the repository a star!
