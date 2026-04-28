from langchain_groq import ChatGroq
from dotenv import load_dotenv 

load_dotenv()

client = ChatGroq(
    model = "llama-3.3-70b-versatile"
)

response = client.invoke("Τι ακριβως έιναι το AI engineering;")

print("=== Πρώτη απάντηση ===")
print(response.content) 


from langchain_core.messages import HumanMessage, SystemMessage 

messages = [ 
    SystemMessage(content="Απαντάς ΠΑΝΤΑ στα ελληνικά με μια πρόταση μόνο, έχωντας κατανοητό ύφος."),
    HumanMessage(content = "Πες μου τι ειναι το AI engineering;")
]

response = client.invoke(messages)

print("=== Δεύτερη απάντηση ===")
print(response.content)