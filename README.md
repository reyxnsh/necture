<h1 align="center">Necture</h1>

<p align="center">
  <strong>Turn YouTube lectures into clean, structured study notes.</strong>
</p>

<p align="center">
  A lightweight Streamlit app that helps students extract key concepts,
  explanations, and examples from YouTube educational videos.
</p>

---

## 🚀 What is Necture?

**Necture** is a personal productivity tool that converts YouTube lecture videos  
into **clear, readable study notes** using AI.

Instead of re-watching long videos, you can:
- Paste a YouTube link
- Generate structured notes
- Focus on understanding, not transcription

---

## ✨ Features

- 📎 Paste a YouTube video link
- 🧠 Extract key concepts and definitions
- 📝 Generate clean, bullet-point study notes
- ⚡ Fast, simple, and distraction-free
- 🖥️ Runs locally (no deployment required)

---

## 🧠 How It Works (High-Level)

1. User provides a YouTube link  
2. Captions are fetched from YouTube  
3. Transcript is chunked into manageable sections  
4. AI processes each chunk to extract:
   - Main ideas
   - Definitions
   - Examples  
5. Notes are merged into a structured summary

---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|------------|
| Language     | Python |
| UI Framework | Streamlit |
| Video Data   | YouTube Transcript API |
| AI           | OpenAI API |
| Environment  | Virtualenv |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/necture.git
cd necture
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
```bash
OPENAI_API_KEY=your_api_key_here
```
### 5. Run the application
```bash
streamlit run app.py
```
