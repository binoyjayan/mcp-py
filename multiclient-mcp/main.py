import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
model = os.environ.get("GEMINI_MODEL", "models/gemini-1.5-pro-latest")
api_key = os.environ.get("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key, temperature=0.1)

math_server_path = os.path.join(os.path.dirname(__file__), "servers", "math_server.py")
weather_server_path = os.path.join(
    os.path.dirname(__file__), "servers", "weather_server.py"
)


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [math_server_path],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8080/mcp",
                "transport": "streamable_http",
            },
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(model=llm, tools=tools)
    response = await agent.ainvoke(
        {"messages": [HumanMessage(content="What is the weather in London?")]}
    )
    result = response["messages"][-1].content if "messages" in response else response
    print("Result:", result)

    response = await agent.ainvoke(
        {"messages": [HumanMessage(content="What 1024 + 1024 * 2?")]}
    )
    result = response["messages"][-1].content if "messages" in response else response
    print("Result:", result)


if __name__ == "__main__":
    asyncio.run(main())
