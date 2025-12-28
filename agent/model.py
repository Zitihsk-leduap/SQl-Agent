## this is used for calling the llm models 
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite", 
        temperature=0,
        api_key =os.getenv("GOOGLE_API_KEY"))