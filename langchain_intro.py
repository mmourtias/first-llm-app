from langchain_groq import ChatGroq
from dotenv import load_dotenv 


load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Προσέγγιση 1: απλό string invoke — χωρίς system prompt, χωρίς ρόλους
response = client.invoke("Τι είναι το machine learning;")

print("=== Πρώτη απάντηση ===")
print(response.content)


# Προσέγγιση 2: με SystemMessage + HumanMessage — ελέγχεις τη συμπεριφορά του μοντέλου
# SystemMessage: οδηγίες προς το μοντέλο (δεν το βλέπει ο χρήστης)
# HumanMessage: το μήνυμα του χρήστη
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Απαντάς ΠΑΝΤΑ στα ελληνικά με μια πρόταση μόνο."),
    HumanMessage(content="Τι είναι το machine learning;")
]

response = client.invoke(messages)

print("=== Δεύτερη απάντηση ===")
print(response.content)
