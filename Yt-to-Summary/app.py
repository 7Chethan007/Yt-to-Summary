import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- IMPROVED PROMPT DESIGN ---
# This prompt forces the model to be a "Content Specific" note-taker rather than a generic summarizer.
system_prompt = """
You are an advanced AI Content Strategist and Professional Note-Taker. Your task is to analyze the following YouTube video transcript and generate a comprehensive, "University-Level" study guide. 

The goal is that a reader must fully understand the specific value, technical details, and core message of the video WITHOUT needing to watch it.

Please structure your response exactly as follows:

1.  **EXECUTIVE SUMMARY (TL;DR):**
    * Provide a 3-5 sentence high-level overview of the video's main topic and purpose.

2.  **CORE CONCEPTS & KEY TAKEAWAYS:**
    * List the 5-7 most critical points discussed.
    * Use bullet points.
    * *Crucial:* Do not be vague. Instead of saying "The speaker discussed tools," say "The speaker recommended tools like X, Y, and Z for specific tasks."

3.  **DETAILED BREAKDOWN:**
    * Divide the video content into logical sections (e.g., "Step 1," "The Problem," "The Solution").
    * Elaborate on the arguments, tutorials, or stories shared in the transcript.
    * Include specific numbers, dates, code snippets (if technical), or quotes if they are pivotal.

4.  **ACTIONABLE INSIGHTS / CONCLUSION:**
    * What should the viewer do with this information?
    * Summarize the final verdict or closing thoughts.

TRANSCRIPT DATA:
"""

# --- HELPER FUNCTIONS ---

def get_video_id(url):
    """
    Extracts the video ID from various YouTube URL formats.
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def extract_transcript_details(video_id):
    """
    Fetches the transcript data from the YouTube API.
    """
    try:
        # Get the transcript
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine the list of dictionaries into a single string
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except TranscriptsDisabled:
        st.error("Subtitles are disabled for this video.")
        return None
    except NoTranscriptFound:
        st.error("No transcript found for this video language.")
        return None
    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None

def generate_gemini_content(transcript_text, prompt):
    """
    Sends the transcript to Gemini Pro for summarization.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")
        # combine the system prompt with the actual transcript
        full_prompt = prompt + transcript_text
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

# --- STREAMLIT UI ---

st.set_page_config(page_title="Smart Video Notes", page_icon="📝", layout="wide")

st.title("📝 AI Professional Video Summarizer")
st.markdown("Transform YouTube videos into comprehensive, structured study notes.")

# Input section
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = get_video_id(youtube_link)
    
    if video_id:
        # Display thumbnail
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=False, width=500)
    else:
        st.warning("Please enter a valid YouTube URL.")

# Button to trigger action
if st.button("Generate Detailed Notes"):
    if not youtube_link:
        st.warning("Please enter a YouTube link first.")
    else:
        video_id = get_video_id(youtube_link)
        
        if video_id:
            with st.spinner("Extracting transcript and generating professional notes... This may take a moment."):
                # 1. Get Transcript
                transcript_text = extract_transcript_details(video_id)

                if transcript_text:
                    # 2. Generate Summary
                    summary = generate_gemini_content(transcript_text, system_prompt)
                    
                    if summary:
                        st.markdown("---")
                        st.subheader("Here are your detailed notes:")
                        st.markdown(summary)