import os
import warnings
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

# To avoid display of warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-pro-latest")

# Set up the LLM
llm = ChatGoogleGenerativeAI(
    model=model_name, temperature=0.5, google_api_key=api_key
)

tools = load_tools(["wikipedia", "llm-math"], llm=llm)
memory = ConversationBufferWindowMemory(memory_key="chat_history", k=2, return_messages=True)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory
)

result1 = agent.invoke("What is the capital of United States?")
result2 = agent.invoke("Who was its president in 2023?")
print(result1)
print(result2)
