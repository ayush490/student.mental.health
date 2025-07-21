cat <<EOF > README.md
# Student Lifestyle & Mental Health Analyzer

A multi-page Streamlit web app that collects student lifestyle, academic, emotional, and environmental metrics — then uses **Gemini AI (LLM)** to provide personalized mental health insights and suggestions.

## 🚀 Features

- Google-Form-like multi-page input experience  
- Collects detailed lifestyle, academic, social, and emotional data  
- Uses Google's **Gemini Pro (LLM)** to analyze and give smart feedback  
- API key secured with \`.env\` (not pushed to GitHub)  
- Built for SDE3 university-level mental health projects

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up your \`.env\` file:**

Create a \`.env\` file in the root folder and add your Gemini API key:

```ini
GEMINI_API_KEY=your-api-key-here
```

> **Never share or push this file. It’s ignored via \`.gitignore\`.**

## 💡 How It Works

The app consists of multiple form-based pages:

1. **Personal Info**  
2. **Lifestyle Metrics**  
3. **Academic & Routine**  
4. **Emotional & Social**  
5. **Environment & Financial Factors**  
6. **Result Page** (LLM feedback)

After collecting responses, the app sends a prompt to **Gemini Pro (\`gemini-2.5-pro\`)** to analyze the student’s mental health and return personalized insights.

## Run the App

```bash
streamlit run app.py
```

Replace \`app.py\` with your actual Python file name if different.

## Deployed Web Link



## Project Structure

```
your-repo/
├── app.py               # Main Streamlit app
├── .env                 # Your local API key (not tracked)
├── .gitignore           # Ignores .env and other temp files
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

##FAQ

**Q: Can I add charts or risk scoring?**  
Yes! Just ask Gemini to return a JSON with tags and visualize with \`st.bar_chart\`.

**Q: Is my data stored?**  
Not unless you build in logging or export features — currently all local/session-based.

##Author

Made by Ayush Gohel  
> For SDE3 – Mental Health & AI Project

##License

This project is open-source under the MIT License.
EOF
