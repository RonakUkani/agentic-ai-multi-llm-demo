"""
LLM setup for Ollama integration with LangChain.
"""
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
import config_settings

"""
Initializes the Ollama LLM instance.
"""
def initialize_llm():
    print(config_settings.__file__)
    return Ollama(model=config_settings.OLLAMA_MODEL, base_url=config_settings.OLLAMA_HOST)

"""
Initializes the conversation memory.
"""
def initialize_memory():
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)
