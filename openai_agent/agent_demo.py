import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.tools import DuckDuckGoSearchRun

# 1. Set your API key
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"  # Replace with your key

# 2. Create LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 3. Create a Web Search Tool
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="WebSearch",
        func=search.run,
        description="Use this to search the web for up-to-date information"
    )
]

# 4. Create the Agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 5. Run the Agent
print("\n🤖 Agentic AI Demo\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = agent.run(user_input)
    print(f"AI: {response}\n")
