from groq import Groq 
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [ 
{
"role": "system",
"content": """
 Είσαι ένας code reviewer που εξετάζει τον κώδικα ενός προγράμματος
και δίνει συμβουλές για τον κώδικα ώστε να γίνει πιο αποδοτικός.
Το ύφος της συμβουλής σου θέλω να είναι σοβαρό και πολύ κατανοητό,
καθώς ο προγραμματιστής ενδέχεται να είναι νέος με λίγη εμπειρία.
Απαντάς ΠΑΝΤΑ και ΜΟΝΟ στα ελληνικά, χωρίς καμία λέξη από άλλη γλώσσα.
Αυτό που θέλω να κοιτάς στον κώδικα είναι : 
- Η δομή του κώδικα
- Η σωστή χρήση των μεταβλητών, των συναρτήσεων και των κλάσεων
- Το πως μπορεί να γίνει πιο αποδοτικός και γρήγορος ο κώδικας
- Το πως μπορει να γίνει ο κώδικας πιο απλός και πιο εύκολος στην κατανόηση
- Τέλος θέλω στα errors που μπορεί να υπάρξουν να δίνεις τις κατάλληλες επεξηγήσεις και 
συμβουλές για το πως να τα διορθώσει ο χρήστης.
- θέλω να δίνεις παραδείγματα βελτιωμένου κώδικα όταν κάτι μπορεί να γραφτεί καλύτερα. """
    
}]

print("Code Reviewer έτοιμο! Γράψε 'quit' για έξοδο.\n")

while True:
    print("Εσύ (επικόλλησε κώδικα και πάτα Enter δύο φορές):")
    lines = []
    quit_requested = False
    while True:
        line = input()
        if line.lower() == "quit":
            quit_requested = True
            break
        if line == "":
            break
        lines.append(line)

    if quit_requested:
        break

    user_input = "\n".join(lines)

    messages.append({"role":"user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    assistant_message = response.choices[0].message.content

    messages.append({"role":"assistant", "content": assistant_message})

    print(f"Code Reviewer: {assistant_message}\n")