import subprocess
import streamlit as st
from ppt_data_gen import slide_data_gen
from ppt_gen import ppt_gen
import random
from datetime import datetime
import time

# Define the function to get installed models first
def get_installed_models():
    try:
        # Run ollama list command and capture output
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        # Split output into lines and skip the header line
        lines = result.stdout.strip().split('\n')[1:]
        # Extract model names from each line
        models = [line.split()[0] for line in lines if line]
        return models
    except Exception as e:
        # Fallback to default models if command fails
        st.warning(f"Could not fetch installed models: {str(e)}")
        return []

# Function to select Ollama model
def select_ollama_model():
    models = get_installed_models()
    selected_model = st.selectbox("Select Ollama model:", models)
    return selected_model

st.title("PPT Generator")

# Input for topic
topic = st.text_input("Enter a topic:")

# Slider for number of slides
num_slides = st.slider("Select number of slides:", min_value=3, max_value=20, value=7)

# Add language selection dropdown
languages = ["English", "French", "Spanish", "German", "Ukrainian", "Arabic"]  # Added Ukrainian and Arabic
language = st.selectbox("Select Language:", languages, index=0)

# Get selected model and language
ollama_model = select_ollama_model()

if st.button("Generate") and topic:
    # Initialize progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    # List of random status messages
    messages = [
        "Hold your horses—better yet, knit them a sweater while you wait",
        "Time flies when you’re watching cat videos. Try it",
        "If waiting were a sport, you’d be a gold medalist. Flex those skills",
        "Patience is a virtue, and so is binge-watching your favorite show",
        "Why not take a power nap? I’ll wake you up… maybe",
        "Hang tight—perfect time for a snack break! Got popcorn?",
        "Waiting is just the universe’s way of saying, “Do a little dance!”",
        "Hold on—time to practice your air guitar solo",
        "Think of this as a short intermission. Grab a soda and some popcorn",
        "While you’re waiting, why not perfect your paper airplane technique?"
    ]

    # Shuffle messages to ensure randomness
    random.shuffle(messages)

    # Function to update status message with a dancing cursor
    def update_status_with_cursor(message):
        cursor_states = ['|', '/', '-', '\\']
        for cursor in cursor_states:
            status_text.text(f"{message} {cursor}")
            time.sleep(0.25)  # Change cursor every 0.25 seconds

    # Update status with a random message and dancing cursor
    for _ in range(4):  # Display each message for 4 seconds
        if messages:
            update_status_with_cursor(messages.pop())

    # Generate slide data with the selected language
    data = slide_data_gen(topic, num_slides, ollama_model, language)
    progress_bar.progress(50)

    # Update status with another random message and dancing cursor
    for _ in range(4):  # Display each message for 4 seconds
        if messages:
            update_status_with_cursor(messages.pop())

    ppt_file = ppt_gen(data)
    progress_bar.progress(100)

    # Reset status
    status_text.text("Presentation ready for download!")
    progress_bar.empty()

    # Create a file name using the topic, model, and current date
    date_stamp = datetime.now().strftime("%Y%m%d")
    sanitized_topic = topic.replace(" ", "_")[:10]  # Truncate topic to 10 characters
    file_name = f"{sanitized_topic}_{ollama_model}_{date_stamp}.pptx"

    st.download_button(
        label="Download Presentation",
        data=ppt_file,
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )
else:
    st.warning("Please enter a topic to generate the presentation.")
