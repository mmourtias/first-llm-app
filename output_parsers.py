from langchain_groq import ChatGroq 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

client = ChatGroq(
    model="llama-3.3-70b-versatile"
) 


# Ο parser μετατρέπει την απάντηση σε string
parser = StrOutputParser()

template = ChatPromptTemplate.from_messages([
    ("system", "Είσαι ένας ειδικός σε {subject}. Απαντάς πάντα ΜΟΝΟ στα ελληνικά."),
    ("human", "{question}")
])

chain = template | client | parser

result = chain.invoke({"subject": "Python language",
    "question": "Ποιες είναι οι 3 πιο χρήσιμες built-in functions;"
})

print(result)
print(type(result))