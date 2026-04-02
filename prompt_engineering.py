from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Κακό prompt — ασαφές
bad_prompt = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "πες μου για την Python"}]
)

# Καλό prompt — συγκεκριμένο
good_prompt = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Είσαι senior Python engineer. Απαντάς με bullet points, μέγιστο 5 σημεία, χωρίς εισαγωγή."
        },
        {
            "role": "user", 
            "content": "Ποια είναι τα 5 πιο σημαντικά πράγματα που πρέπει να ξέρει ένας junior Python developer για να γράφει clean code;"
        }
    ]
)

print("=== ΚΑΚΟ PROMPT ===")
print(bad_prompt.choices[0].message.content)
print("\n=== ΚΑΛΟ PROMPT ===")
print(good_prompt.choices[0].message.content)