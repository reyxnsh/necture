import streamlit as st
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


# -----------------------
# Environment Setup
# -----------------------

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# -----------------------
# Helper Functions
# -----------------------

def extract_video_id(url: str) -> str | None:
    """
    Extracts the YouTube video ID from a URL.
    Returns None if the URL is not a valid YouTube link.
    """
    parsed_url = urlparse(url)

    # Short links: youtu.be/VIDEO_ID
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")

    # Full links: youtube.com/watch?v=VIDEO_ID
    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        query_params = parse_qs(parsed_url.query)
        video_ids = query_params.get("v")
        if video_ids:
            return video_ids[0]

    return None


def fetch_transcript(video_id: str) -> list[dict] | None:
    """
    Fetches the YouTube transcript for a given video ID.
    Returns a list of transcript segments or None if unavailable.
    """
    try:
        return YouTubeTranscriptApi.get_transcript(video_id)
    except (TranscriptsDisabled, NoTranscriptFound):
        return None


def generate_notes(transcript_text: str) -> str:
    """
    Generates structured study notes from transcript text using Gemini.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are a teaching assistant helping a student study.

Convert the following lecture transcript into clear, structured study notes.

Rules:
- Use headings for topics
- Use bullet points
- Clearly define important terms
- Include examples if mentioned
- Keep explanations simple and concise
- Do NOT include filler or commentary

Transcript:
{transcript_text}
"""

    response = model.generate_content(prompt)
    return response.text


# -----------------------
# Streamlit App UI
# -----------------------

st.set_page_config(page_title="Necture")

st.title("Necture")
st.write("Turn YouTube lectures into clean study notes.")

st.divider()

youtube_url = st.text_input(
    "Paste a YouTube video link:",
    placeholder="https://www.youtube.com/watch?v=..."
)

if youtube_url:
    video_id = extract_video_id(youtube_url)

    if not video_id:
        st.error("Please enter a valid YouTube video link.")
    else:
        st.success("Valid YouTube link detected!")
        st.write("Video ID:", video_id)

        transcript = fetch_transcript(video_id)

        if not transcript:
            st.warning("No transcript available for this video.")
        else:
            full_text = " ".join(segment["text"] for segment in transcript)

            if st.button("Generate Study Notes"):
                with st.spinner("Generating notes..."):
                    notes = generate_notes(full_text)

                st.subheader("Study Notes")
                st.write(notes)
