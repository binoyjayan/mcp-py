# Fastmcp test

## Claude config


## Stdio


```json
{
  "mcpServers": {
    "research-prompt": {
      "command": "/path/to//uv",
      "args": [
        "--directory",
        "/path/to/fastmcp-test",
        "run",
        "main.py"
      ]
    }
  }
}
```

## Http

```json
{
  "mcpServers": {
    "research-prompt": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

## Session token

```
npx @modelcontextprotocol/inspector
Starting MCP inspector...
⚙️ Proxy server listening on localhost:6277
🔑 Session token: <--- token --->
```

Update the token in Session configuration in MCP Inspector UI
Also use the URL specified in the FastMCP log.
