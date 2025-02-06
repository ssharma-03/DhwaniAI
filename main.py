import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# User inputs
original_song = input("Enter your original song lyrics: ")
desired_song_theme = input("Enter the theme for new song lyrics: ")

# Prompt content with explicit length requirement
content = (
    f"You are a senior lyricist. Your task is to transform the given lyrics: '{original_song}' "
    f"to fit the theme: '{desired_song_theme}'. Ensure the output is creative, flows well, and contains "
    f"enough lyrics to perform for at least 30 seconds."
)

# Create chat completion request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
    model="llama-3.3-70b-versatile",
)

# Print the response
print("Transformed Lyrics:")
print(chat_completion.choices[0].message.content)
