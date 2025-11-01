from ..core.llm_config import LLMConfig
from langchain_groq import ChatGroq

class LLM_util(LLMConfig): 

    def __init__(self):
        super().__init__()

    def get_llm(self): 
        """
        Returns an instance of LLM.
        """
        return ChatGroq(
            model=self.model_name,
            groq_api_key = self.api_key, 
            temperature=self.temperature
        )