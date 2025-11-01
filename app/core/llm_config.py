import os 
from dotenv import load_dotenv

load_dotenv()

class LLMConfig: 

    def __init__(self): 
        self.model_name = os.getenv("GROQ_MODEL")
        self.api_key = os.getenv("GROQ_API_KEY")
        self.temperature = 0.7