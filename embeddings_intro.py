from langchain_groq import ChatGroq
from dotenv import load_dotenv 

load_dotenv() 

client = ChatGroq(
    model="llama-3.3-70b-versatile"
)

from langchain_huggingface import HuggingFaceEmbeddings 

embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "Το machine learning είναι υποκλάδος της τεχνητής νοημοσύνης."

vector = embeddings_model.embed_query(text)

print(f"Κείμενο: {text}")
print(f"Μέγεθος διανύσματος: {len(vector)}")
print(f"Πρώτες 5 τιμές: {vector[:5]}")


#vector database
from langchain_chroma import Chroma

# Μερικά έγγραφα για αποθήκευση
docs = [
    "Το machine learning είναι υποκλάδος της τεχνητής νοημοσύνης.",
    "Η Python είναι δημοφιλής γλώσσα προγραμματισμού.",
    "Τα neural networks μιμούνται τον ανθρώπινο εγκέφαλο.",
    "Το overfitting συμβαίνει όταν το μοντέλο απομνημονεύει τα δεδομένα.",
    "Η Αθήνα είναι η πρωτεύουσα της Ελλάδας."
]

# Δημιουργεί vector database τοπικά
db = Chroma.from_texts(docs, embeddings_model)

# Semantic search
query = "neural networks artificial intelligence"
results = db.similarity_search(query, k=2)

print(f"\nQuery: {query}")
print("\nΠιο σχετικά αποτελέσματα:")
for r in results:
    print(f"- {r.page_content}")