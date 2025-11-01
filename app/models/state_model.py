from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
from ..utils.llm_util import LLM_util
from langchain_groq import ChatGroq #TODO: need to change the import 
import operator

llm: ChatGroq = LLM_util().get_llm() #TODO: change type of the class

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm: ChatGroq  #TODO: change type of the class
    llm_calls: int
    need_human: bool = False
    finished: bool = False
    # validated: bool = False