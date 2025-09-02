from fastmcp import FastMCP

mcp = FastMCP("Research Prompt")

@mcp.prompt()
def get_research_prompt(topic: str) -> str:
    return f"Research the topic of {topic}."

if __name__ == "__main__":
    # mcp.run(transport="http", host="127.0.0.1", port=8080)
    mcp.run()
