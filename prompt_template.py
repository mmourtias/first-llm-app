from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile"
)


# Το template ορίζει τη δομή του prompt με μεταβλητές ({subject}, {question})
# που θα συμπληρωθούν αργότερα στο invoke()
template = ChatPromptTemplate.from_messages([
    ("system", "Είσαι ένας ειδικός σε {subject}. Απαντάς πάντα ΜΟΝΟ στα ελληνικά."),
    ("human", "{question}")
])

# Ο τελεστής | συνδέει βήματα σε μια αλυσίδα (chain): template → client
# Το template γεμίζει τις μεταβλητές και περνάει το αποτέλεσμα στο client
chain = template | client

response = chain.invoke({
    "subject": "cooking ",
    "question": "Τι είναι το caramelization;"
})

print(response.content)