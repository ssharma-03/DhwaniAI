import os
import gradio as gr
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

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# Song Lyrics Transformer 🎵")
    
    with gr.Row():
        original_input = gr.Textbox(label="Original Song Lyrics")
        theme_input = gr.Textbox(label="Desired Theme")
    
    result_output = gr.Textbox(label="Transformed Lyrics", interactive=False)
    
    transform_button = gr.Button("Transform Lyrics")
    transform_button.click(transform_lyrics, inputs=[original_input, theme_input], outputs=result_output)
    
    suno_button = gr.Button("Go to Suno")
    suno_button.click(open_suno_link, outputs=result_output)

# Launch the Gradio app
app.launch()
