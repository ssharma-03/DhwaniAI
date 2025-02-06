import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import webbrowser

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to transform song lyrics
def transform_lyrics(original_song, desired_theme):
    content = (
        f"You are a senior lyricist. Your task is to transform the given lyrics: '{original_song}' "
        f"to fit the theme: '{desired_theme}'. Ensure the output is creative, flows well, and contains "
        f"enough lyrics to perform for at least 30 seconds."
    )
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": content}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Button callback to open external link
def open_suno_link():
    webbrowser.open("https://suno.com/create?wid=default")
    return "Redirecting to Suno..."

# Streamlit UI
st.title("Song Lyrics Transformer 🎵")

# Inputs for the song lyrics and theme
original_song = st.text_area("Original Song Lyrics")
desired_theme = st.text_area("Desired Theme")

# Button to transform lyrics
if st.button("Transform Lyrics"):
    if original_song and desired_theme:
        result = transform_lyrics(original_song, desired_theme)
        st.text_area("Transformed Lyrics", value=result, height=200)
    else:
        st.warning("Please provide both original song lyrics and desired theme.")

# Button to redirect to Suno
if st.button("Go to Suno"):
    st.write("Redirecting to Suno...")
    open_suno_link()
