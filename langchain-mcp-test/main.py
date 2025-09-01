import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOpenAI()

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
            tools = await session.list_tools()
            print(f"Tools loaded: {tools}")
            agent = create_react_agent(llm, tools)

if __name__ == "__main__":
    asyncio.run(main())
