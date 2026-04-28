from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile"
)


template = ChatPromptTemplate.from_messages([
    ("system", "Είσαι ένας ειδικός σε {subject}. Απαντάς πάντα ΜΟΝΟ στα ελληνικά."),
    ("human", "{question}")
])

chain = template | client

response = chain.invoke({
    "subject": "machine learning",
    "question": "Τι είναι το overfitting;"
})

print(response.content)