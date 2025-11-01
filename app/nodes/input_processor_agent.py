from .tools_executor import input_tools
from langchain.messages import SystemMessage
from langgraph.runtime import Runtime
from dataclasses import dataclass
from langchain_groq import ChatGroq 
@dataclass
class ContextSchema:
    llm: ChatGroq


def input_processor_node(state: dict,  runtime: Runtime[ContextSchema]) :
    """
    Input processing node responsible for validating all the input recieved from the user and parsing it in required format for next step.
    """
    # state["llm"] = runtime.context.llm
    # llm_with_tools = state["llm"].bind_tools(input_tools)
    llm_with_tools = runtime.context.llm.bind_tools(input_tools)
    input_processor_prompt = """
                                You are an expert scenario-decider and input validator.

                                <IMPORTANT>
                                YOU CAN NOT DO ANY OF THE TASK ON YOUR OWN, ALL TASKS NEEDS TO BE PERFORMED BY THE TOOLS ONLY. 
                                HOWEVER, IF THE USER'S QUERY IS INTENDED TOWARDS GENERAL CONVERSATION NOT ANYTHING SPECIFIC,
                                YOU CAN ANSWER UPTO A POINT WHERE IT IS BECOMES ANYTHING SPECIC RELATED TO ORGANIZATION'S HIRING.
                                </IMPORTANT>

                                Your task is to:

                                    1. Evaluate the user's query and decide which scenario is most appropriate, using the scenario_decider tool.

                                    2. Validate the user's inputs for correctness and completeness with the input_validator tool.

                                    3. Map the validated input data into a structured JSON format.
                                    Follow these steps precisely.
                            """
    
    response = llm_with_tools.invoke(
                [
                    SystemMessage(
                        content=input_processor_prompt
                    )
                ] + state["messages"]
    )

    return {"messages": response}