import os
from groq import Groq
from dotenv import load_dotenv
from organizer import organize_folder

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

user_input = input("Enter command: ")

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

print("\nAI Response:")
print(ai_reply)

if "ORGANIZE" in ai_reply:
    organize_folder("test_folder")
    print("\nFolder organized successfully!")