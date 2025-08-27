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

Run server via uv.

```
uv run python server.py
```

## Test using Claude desktop

### Testing locally

```json
{
  "mcpServers": {
    "shellserver": {
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/shellserver-dir",
        "run",
        "server.py"
      ]
    }
  }
}
```

### Testing in a container

```json
{
  "mcpServers": {
    "shellserver": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--init",
        "-e",
        "DOCKER_CONTAINER=true",
        "mcp-shellserver"
      ]
    }
  }
}
```


## Test using MCP Inspector

### Command

If the command is run via `uv`, provide full path.
```
/path/to/uv
```

### Arguments

```
--directory /path/to/project/directory run server.py
```
