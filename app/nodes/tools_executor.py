from ..tools.input_processor_tools import input_validator, scenario_decider
from langchain.messages import ToolMessage
from ..utils.log_util import setup_logger

logger = setup_logger()

input_tools = [input_validator, scenario_decider]

tools = [input_validator, scenario_decider]
tools_by_name = {tool.name: tool for tool in tools}

def input_tools_excecutor(state: dict):
    """
    Response for executing all the tools called by LLM.
    """
    results = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        logger.info(f"Tool name to be executed: {tool_call['name']}")
        observation = tool.invoke(llm=state["llm"], kwargs=tool_call["args"])
        logger.info(f"Tool: {tool_call['name']}\nTool output: {observation}")
        results.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": results}
