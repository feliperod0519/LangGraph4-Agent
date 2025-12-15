from dotenv import load_dotenv
import os
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE="""
You are a helpful assistant that can use tools to answer qustion.
"""

# seq = [1, 2, 3, 4, 5]
# a, b, *rest = seq
# # a is 1, b is 2, rest is [3, 4, 5]

def run_agent_reasoning(state:MessagesState)->MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke([{"role":"system","content":SYSTEM_MESSAGE},*state['messages']])
    return {"messages":[response]}

tool_node = ToolNode(tools)