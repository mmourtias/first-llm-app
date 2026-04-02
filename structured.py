from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": """Είσαι ένας assistant που εξάγει πληροφορίες από κείμενο.
            Απαντάς ΠΑΝΤΑ σε JSON format με αυτά ακριβώς τα πεδία:
            {
                "name": "το όνομα του ατόμου",
                "age": την ηλικία ως αριθμός,
                "city": "η πόλη"
            }
            Τίποτα άλλο εκτός από το JSON."""
        },
        {
            "role": "user",
            "content": "Η Μαρία είναι νέα και μένει κάπου στην Ελλάδα αλλά δεν ξέρω πού."
        }
    ]
)

# Παίρνει το κείμενο της απάντησης
raw = response.choices[0].message.content

# Το μετατρέπει σε Python dictionary
data = json.loads(raw)

print("Raw response:", raw)
print("---")
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])