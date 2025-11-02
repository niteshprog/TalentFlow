# from ..nodes.tools_executor import input_tools_excecutor
from .log_util import setup_logger
import json, re

logger = setup_logger()

def parse_llm_json(content: str) -> dict:
    """Parse JSON from LLM output, handling markdown code blocks and cleaning up the content."""
    content = content.strip()
    
    # Remove markdown code blocks using regex
    json_match = re.search(r'```(?:json)?\s*([\s\S]*?)```', content, re.MULTILINE)
    if json_match:
        content = json_match.group(1)
    else:
        # If no code blocks found, try to extract just the JSON object
        json_match = re.search(r'({[\s\S]*})', content)
        if json_match:
            content = json_match.group(1)
    
    # Clean up the content
    content = content.strip()
    
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON: {e}")
        raise

def input_routing_conditions(state: dict): 
    """
    Contains logic for condition routing from/ to the input processing agent.
    """
    last_message = state["messages"][-1] if state["messages"] else None
    history_length = len(state["messages"])
    logger.info(f"Last message recieved to Input routing logic: {type(last_message)}")

    if last_message: 

        if hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0:
            logger.info(msg="Routed to Input Agent's tools.")
            return "input_tools"
        
        elif history_length >= 2 and state["messages"][-2].name == "input_validator" and not last_message.content: 
            # content = last_message.content
            content = state["messages"][-2].content
            # parsed_result = parse_llm_json(content)
            parsed_result = json.loads(content)
            if parsed_result['remarks'] == "validated": 
                return "next"
            else: 
                return "input_tools"
        
    logger.info("Routed for human input from the input processing agent.")
    return "human"
    

def human_continuation(state: dict): 
    """
    Logical flow to determine whether to continue after human input of not.
    """
    last_message = state["messages"][-1]

    if last_message.content == "finished":
        return "finished"
    else: 
        return "continue"
