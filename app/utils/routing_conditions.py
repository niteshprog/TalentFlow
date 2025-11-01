# from ..nodes.tools_executor import input_tools_excecutor
from .log_util import setup_logger

logger = setup_logger()

def input_routing_conditions(state: dict): 
    """
    Contains logic for condition routing from/ to the input processing agent.
    """
    last_message = state["messages"][-1] if state["messages"] else None
    logger.info(f"Last message recieved to Input routing logic: {type(last_message)}")

    if last_message: 

        if hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0:
            logger.info(msg="Routed to Input Agent's tools.")
            return "input_tools"
        
        elif last_message.content == "validated": 
            logger.info(msg="Inputs are validated and parsed to JSON successfully.")
            return "next"
        
    logger.info("Routed for human input from the input processing agent.")
    return "human"
    

def human_continuation(state: dict): 
    """
    Logical flow to determine whether to continue after human input of not.
    """
    last_message = state["message"][-1]

    if last_message.content == "finished":
        return "finished"
    else: 
        return "continue"
