import asyncio
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shellserver")


@mcp.resource("file://readme")
async def get_readme() -> str:
    """
    Expose readme from the project root.

    Returns:
            str: Contents of the readme file or an error message.
    """
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "README.md file not found"
    except Exception as e:
        return f"Error reading README.md: {str(e)}"


@mcp.tool()
async def run_command(command: str) -> dict:
    """Execute a shell command and return structured results.

    Args:
            command: str
                    Command string passed to the system shell (`/bin/bash -c`). Avoid
                    untrusted / user-injected segments unless properly sanitized.
    Returns:
            Dict with keys:
                    stdout (str): Captured standard output ('' if none)
                    stderr (str): Captured standard error ('' if none)
                    exit_code (int): Process exit status (0 indicates success)
    """
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout_b, stderr_b = await process.communicate()
    return {
        "stdout": stdout_b.decode(),
        "stderr": stderr_b.decode(),
        "exit_code": process.returncode or 0,
    }


if __name__ == "__main__":
    mcp.run("stdio")
