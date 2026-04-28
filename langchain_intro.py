from langchain_groq import ChatGroq
from dotenv import load_dotenv 


load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile"
)

response = client.invoke("Τι είναι το machine learning;")

print("=== Πρώτη απάντηση ===")
print(response.content)



from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Απαντάς ΠΑΝΤΑ στα ελληνικά με μια πρόταση μόνο."),
    HumanMessage(content="Τι είναι το machine learning;")
]

response = client.invoke(messages)

print("=== Δεύτερη απάντηση ===")
print(response.content)
