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

                                You will be handling the following tasks:

                                    1. Evaluate the user's query and decide which scenario is most appropriate, using the scenario_decider tool.

                                    2. Validate the user's inputs for correctness and completeness with the input_validator tool.

                                    3. Map the validated input data into a structured JSON format.
                                    Follow these steps precisely.

                                <IMPORTANT>
                                YOU CAN NOT DO ANY OF THE TASK ON YOUR OWN, ALL TASKS NEEDS TO BE PERFORMED BY THE TOOLS ONLY. 
                                HOWEVER, IF THE USER'S QUERY IS INTENDED TOWARDS GENERAL CONVERSATION NOT ANYTHING SPECIFIC,
                                YOU CAN ANSWER UPTO A POINT WHERE IT IS BECOMES ANYTHING SPECIC RELATED TO ORGANIZATION'S HIRING.
                                </IMPORTANT>

                                There are two situations one is 'STARTING A NEW CHAT' or 'CONTINUING AN OLD CHAT'. AND THE SOLVING APPROACH IN EACH CONDITION IS AS FOLLOWS:

                                1. STARTING A NEW CHAT: 

                                    -Query will be passed through 'scenario_decider' (which will decide the scenario) -> 'input_validator' (which will fill the dictionary by   parsing the details from query to dictionary) 
                                    AND IF ANY DETAIL IS MISSED THE CHAT IS HALTED. 

                                    -IF THE CONTENT OF LAST MESSAGE IN HISTORY IS DICTIONARY/JSON RECEIVED BY input_validator TOOL THEN 
                                    USING THE 'remarks' FIELD FROM THE DICTIONARY/JSON PHRASE A NATURAL LANGUAGE STATEMENT EXPLAINING THE 
                                    FIELD WHICH ARE MISSING.
                                    MAKE SURE JUST TO TALK ABOUT THE MISSING DATA AND ASKING THE USER TO PROVIDE THE DETAILS.
                                
                                2. CONTINUING AN OLD CHAT: 

                                    -CRUCIAL: WHEN THE CONVERSATION IS CONTINUED, THEN NO NEED TO AGAIN FIGURE OUT THE SCENARIO, 
                                    THE PERVIOUSLY DECIDED SCENARIO CAN BE UTILIZED.
                                    AND ALSO THE DETAILS GIVEN EARLIER SHOULD BE REUSED FROM THE RESPONSE OF 'input_validator' TOOL CALL RESULT EARLIER.
                                    AS USER IS ONLY EXPECTED TO PROVIDE THE MISSING DETAILS ONLY AS PER ASK AND WON'T BE GIVING THE OLDER DETAILS AGAIN.

                                RESPONSE SHOULD IN 'MARKDOWN' FORMATTING. 
                                CRUCIAL: MAKE SURE IN 'MARKDOWN' FORMATTING NEW LINE IS REPRESENTED BY '<br>' NOT '\n'.

                                
                            """
    
    response = llm_with_tools.invoke(
                [
                    SystemMessage(
                        content=input_processor_prompt
                    )
                ] + state["messages"]
    )

    return {"messages": response}