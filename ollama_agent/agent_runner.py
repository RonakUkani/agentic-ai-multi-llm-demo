"""
Agent setup and execution logic.
"""
from langchain.agents import initialize_agent, AgentType
import config_settings

"""
    Creates and configures the LangChain conversational agent.
"""
def create_agent(llm, tools, memory):
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=config_settings.VERBOSE_MODE,
        max_iterations=config_settings.MAX_ITERATIONS,
        handle_parsing_errors=True
    )

def run_agent(agent, user_input):
    """
    Runs the agent with a given user input.
    """
    result = agent.invoke({"input": user_input})
    return result.get("output", "No output found")
