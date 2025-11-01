from langgraph.types import interrupt
from ..utils.log_util import setup_logger

logger = setup_logger()

def human_node(state: dict):
    """
    Interrupts the graph for the human input.
    """
    user_input = interrupt("Give me your reply")
    logger.info(f"Human input recieved: {user_input}")
    return {"messages": [("user", user_input)]}