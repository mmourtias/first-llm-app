from groq import Groq
from dotenv import load_dotenv
import os

# Φορτώνει το API key από το .env αρχείο
load_dotenv()

# Δημιουργεί τον client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Κάνει το πρώτο API call
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Πες μου ένα σύντομο γεια στα ελληνικά."
        }
    ]
)

# Τυπώνει την απάντηση
print(response.choices[0].message.content)