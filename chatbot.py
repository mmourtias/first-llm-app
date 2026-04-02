from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Το ιστορικό της συνομιλίας — ξεκινάει με το system prompt
messages = [
    {
        "role": "system",
        "content": "Είσαι ένας σαρκαστικός assistant που απαντάει πάντα με χιούμορ και δεν παίρνει τίποτα στα σοβαρά."
    }
]

print("Chatbot έτοιμο! Γράψε 'quit' για έξοδο.\n")

while True:
    # Παίρνει input από τον χρήστη
    user_input = input("Εσύ: ")
    
    if user_input.lower() == "quit":
        break
    
    # Προσθέτει το μήνυμα του χρήστη στο ιστορικό
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Στέλνει ΟΛΟΚΛΗΡΟ το ιστορικό στο API
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    # Παίρνει την απάντηση
    assistant_message = response.choices[0].message.content
    
    # Προσθέτει την απάντηση στο ιστορικό
    messages.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    print(f"Bot: {assistant_message}\n")