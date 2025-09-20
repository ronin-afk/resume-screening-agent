# 📊 Smart ATS Resume Ranking System

A web-based tool that allows you to upload multiple resumes and rank them against a job description using **Google Gemini AI**. The system evaluates resumes with precision, providing match percentages, missing keywords, and concise profile summaries.

---

## 🛠 Features

- Upload multiple **PDF resumes** at once.
- Paste or input a **Job Description** for evaluation.
- Automatic **JD Match Percentage** calculation for each resume.
- Identification of **Missing Keywords** relative to the job description.
- Generates a **Profile Summary** highlighting candidate skills, experience, and strengths.
- Resumes are **ranked automatically** based on compatibility with the job description.
- Interactive **Streamlit UI** for easy usage.

---

## ⚡ How It Works

1. **Upload resumes** in PDF format.
2. **Paste the job description** into the text area.
3. Click **Rank Resumes**.
4. The app:
   - Extracts text from uploaded PDFs.
   - Sends each resume and JD to **Google Gemini AI** for evaluation.
   - Extracts JD match percentage and detailed analysis.
   - Sorts resumes based on score and displays ranking and detailed feedback.

---

## 📝 Installation

1. Clone this repository:

```
git clone https://github.com/ronin-afk/resume-screening-agent.git
cd Resume_ScreenAgent
```
2. Create and activate a virtual environment:
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4 .Create a .env file in the project root and add your Google API Key:
```
GOOGLE_API_KEY=your_google_api_key_here
```
🚀 Usage

Run the Streamlit app:
```
streamlit run app.py
```

Upload resumes in PDF format.

Paste the job description.

Click Rank Resumes to get the ranking and detailed evaluation.

📂 Project Structure
```
.
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (Google API Key)
└── README.md               # Project documentation
```
⚙️ Dependencies

Python 3.10+

Streamlit

PyPDF2

Google Generative AI Python SDK

python-dotenv

pandas

⚠️ Notes

Ensure you have a valid Google API Key with access to Gemini models.

Only PDF resumes are supported.

The evaluation depends on AI-generated responses; results may vary slightly.

Large resumes or multiple uploads may increase processing time.
