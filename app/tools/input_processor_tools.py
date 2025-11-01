from langchain_core.tools import tool
from langchain_groq import ChatGroq
from ..prompts.scenarios.scenario_descriptions import prompt as scenario_decider_prompt
from ..prompts.scenarios.input.scenario1 import prompt as hiring_prompt
from ..prompts.scenarios.input.scenario2 import prompt as resignation_prompt



@tool
def scenario_decider(llm: ChatGroq, query: str): 
    """
    Detects the scenario to which the user query belongs.

    Args: 
        query(str):  Query for which the scenarios needs to be decided.
    """

    decider_prompt = scenario_decider_prompt
    response = llm.invoke(decider_prompt + "\nUser Query: " + query)
    return response.content

@tool
def input_validator(llm: ChatGroq, query: str, scenario: str):
    """
    Validates the details given in the query that every details is present or not and parses it to JSON for further processing.

    Args: 
        query(str): User's query from which details are to be extracted
        scenario(str): Scenario under which the user's query falls. Decided by by 'scenario_decider' tool.
    """

    validator_prompt = hiring_prompt if scenario == "scenario1" else resignation_prompt
    response = llm.invoke(validator_prompt + "\nUser query:" + query)
    return response.content


