from langchain_core.tools import tool
from langchain.tools import ToolRuntime
from langchain_groq import ChatGroq
from ..prompts.scenarios.scenario_descriptions import prompt as scenario_decider_prompt
from ..prompts.scenarios.input.scenario1 import prompt as hiring_prompt
from ..prompts.scenarios.input.scenario2 import prompt as resignation_prompt
from langchain_core.messages import BaseMessage
from dataclasses import dataclass

@dataclass
class ContextSchema:
    llm: ChatGroq


@tool
def scenario_decider(messages: list[BaseMessage], runtime: ToolRuntime[ContextSchema]): 
    """
    Detects the scenario to which the user query belongs.

    Args: 
        message(list[BaseMessage]): Whole conversation history.
    """
    llm = runtime.context.llm
    query = messages[-1].content
    decider_prompt = scenario_decider_prompt
    response = llm.invoke(decider_prompt + "\nUser Query: " + query)
    return response.content

@tool
def input_validator(messages: list[BaseMessage], scenario: str, runtime: ToolRuntime[ContextSchema]):
    """
    Validates the details given in the query that every details is present or not and parses it to JSON for further processing.

    Args: 
        message(list[BaseMessage]): Whole conversation history.
        scneario(str): Scenario decided on the basis of user's query.
    """
    # scenario = messages[-2].content
    llm = runtime.context.llm
    validator_prompt = hiring_prompt if scenario == "scenario1" else resignation_prompt
    response = llm.invoke(validator_prompt + "\nConversation trace:" + str(messages))
    return response.content


