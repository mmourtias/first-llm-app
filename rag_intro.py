from pydoc import doc
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 

load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile"
)

from langchain_huggingface import HuggingFaceEmbeddings  
from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate


#Embeddings model
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Έγγραφα — η "γνωσιακή βάση" μας
docs = [
   "The Python list is a data structure that stores multiple items in a single variable.",
    "Functions in Python are defined with the def keyword.",
    "A dictionary in Python stores data in key-value pairs.",
    "Loops in Python include for loops and while loops.",
    "Python classes are created using the class keyword and support inheritance."
]

# Αποθήκευση των έγγραφων σε vector database
db = Chroma.from_texts(docs, embeddings_model)


# RAG function
def ask(question):
    # Βήμα 1: βρες τα πιο σχετικά έγγραφα
    relevant_docs = db.similarity_search(question, k=2)
    context = "\n".join([d.page_content for d in relevant_docs])
    
    # Βήμα 2: φτιάχνω prompt με context + ερώτηση
    template = ChatPromptTemplate.from_messages([
        ("system", """Απάντησε στην ερώτηση ΜΟΝΟ βασισμένος στο παρακάτω context.
        Αν η απάντηση δεν υπάρχει στο context, πες 'Δεν βρέθηκε στα έγγραφα'.
        
        Context: {context}"""),
        ("human", "{question}")
    ])
    
    chain = template | client
    response = chain.invoke({
        "context": context,
        "question": question
    })
    
    return response.content

# Δοκιμές
print(ask("How do I create a function in Python?"))
print("---")
print(ask("What is the capital of France?"))