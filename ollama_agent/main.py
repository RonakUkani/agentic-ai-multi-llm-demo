"""
Main entry point for the Ollama Agent application.
"""
from llm_setup import initialize_llm, initialize_memory
from tools_setup import get_tools
from agent_runner import create_agent, run_agent

def main():
    llm = initialize_llm()
    memory = initialize_memory()
    tools = get_tools()
    agent = create_agent(llm, tools, memory)

    while True:
        user_query = input("\nYou: ").strip()
        if user_query.lower() in ["exit", "quit"]:
            print("👋 Conversation ended.")
            break

        output = run_agent(agent, user_query)
        print("\n🤖 Bot55:", output)


if __name__ == "__main__":
    main()