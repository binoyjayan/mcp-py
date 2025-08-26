import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shellserver")

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
