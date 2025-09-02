import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
model = os.environ.get("GEMINI_MODEL", "models/gemini-1.5-pro-latest")
api_key = os.environ.get("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key, temperature=0.1)

math_server_path = os.path.join(os.path.dirname(__file__), "servers", "math_server.py")
stdio_server_params = StdioServerParameters(
    command="python",
    args=[math_server_path],
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        # Create a client session that performs heavy lifting of
        # communicating with the MCP server
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(llm, tools)
            response = await agent.ainvoke({"messages": [HumanMessage(content="What is 4096 + 1024 * 4")]})
            result = response["messages"][-1].content
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
