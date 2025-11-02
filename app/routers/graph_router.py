from fastapi import APIRouter
from ..graph import agent
from langgraph.types import Command
from langchain.messages import HumanMessage
from ..utils.llm_util import LLM_util

llm = LLM_util().get_llm()

router = APIRouter(tags=["graph_router"])

@router.get("/start-chat")
async def start_chat(thread_id: str, response: str = None): 
    thread_config = {"configurable": {"thread_id": thread_id}}
    
    state = agent.invoke(
        {
            "finished": False,
            "needs_human": False, 
            # "messages": [HumanMessage(content=response)]
            "messages": [{"type": "user", "content": response}]
        }, 
        config=thread_config, 
        context={"llm": llm}
        )

    return {
        "message": state["messages"][-1].content,
        "thread_config": thread_config
    }

@router.get("/chat-continue")
def continue_chat(thread_id: str, response: str):
    thread_config = {"configurable": {"thread_id": thread_id}}
    state = agent.invoke(
        Command(resume = response),
        config=thread_config, 
        context={"llm": llm})

    return {            
        "message": state["messages"][-1].content,
        "state": state,
        "thread_id": thread_id
    }