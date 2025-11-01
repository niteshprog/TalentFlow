from langgraph.graph import StateGraph, START, END, MessagesState
from .nodes.retrieval_agent import retrieval_agent
from .nodes.input_processor_agent import input_processor_node as input_processor
from .nodes.human import human_node as human
from .utils.routing_conditions import input_routing_conditions, human_continuation
from .nodes.tools_executor import input_tools_excecutor 
from langgraph.checkpoint.memory import MemorySaver
from dataclasses import dataclass
from langchain_groq import ChatGroq #TODO: change the import

@dataclass
class ContextSchema:
    llm: ChatGroq

agent_builder = StateGraph(MessagesState, context_schema=ContextSchema)   

#nodes addition 
agent_builder.add_node("input_processor", input_processor)
agent_builder.add_node("human", human)
agent_builder.add_node("retrieval_agent", retrieval_agent)
agent_builder.add_node("input_tools", input_tools_excecutor)
# agent_builder.add_node("input_routing_conditions", input_routing_conditions)


#routing 
agent_builder.add_edge(START, "input_processor")
agent_builder.add_conditional_edges("input_processor", 
                                    input_routing_conditions, 
                                    {
                                        "input_tools": "input_tools", 
                                        "human": "human", 
                                        "next": "retrieval_agent"
                                    }
                                )
agent_builder.add_conditional_edges("human", 
                                    human_continuation, 
                                    {
                                        "finished": END, 
                                        "continue": "input_processor"
                                    })
# agent_builder.add_edge("tools", "input_processor")
agent_builder.add_edge("input_tools", "input_processor")
agent_builder.add_edge("retrieval_agent", END)

#builder compilation
checkpointer = MemorySaver()
agent = agent_builder.compile(
    checkpointer=checkpointer
)