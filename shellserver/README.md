# Shell Server (MCP)

Implements a simple Model Context Protocol (MCP) server exposing shell
execution tools using the official
[python SDK](https://github.com/modelcontextprotocol/python-sdk).

## Tools

1. `run_shell(command: str)` - executes a command string via the shell.

## Install

Uses python venv

```
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run the server (stdio)

```
python server.py
```

Or via the MCP CLI (if you want discovery / manifest features once available):
```
mcp run python server.py
```

The server advertises two tools; a client can invoke them per MCP spec.

