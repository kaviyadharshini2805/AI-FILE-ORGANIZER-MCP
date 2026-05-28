import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from organizer import organize_folder

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="AI File Organizer",
    page_icon="📂"
)

st.title("📂AI File Organizer")
st.write("Organize files using AI commands.")

user_input = st.text_input(
    "Enter your command:"
)

if st.button("Run AI Organizer"):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": """
You are an AI file organizer assistant.

If the user wants to organize files,
reply ONLY with:
ORGANIZE
"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    ai_reply = response.choices[0].message.content

    st.subheader("AI Response")
    st.write(ai_reply)

    if "ORGANIZE" in ai_reply:

        organize_folder("test_folder")

        st.success("✅ Folder organized successfully!")