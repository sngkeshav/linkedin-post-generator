from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")

llm = ChatGroq(groq_api_key=API_KEY, model="llama-3.3-70b-versatile")