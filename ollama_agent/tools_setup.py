"""
Tools setup for LangChain Agent.
"""
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
import config_settings

"""
Returns a list of tools available for the agent.
"""
def get_tools():

    search_tool = DuckDuckGoSearchRun()

    return [
        Tool(
            name=config_settings.SEARCH_TOOL_NAME,
            func=search_tool.run,
            description=config_settings.SEARCH_TOOL_DESCRIPTION
        )
    ]
