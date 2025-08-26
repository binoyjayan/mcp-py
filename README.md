# MCP 

## Building npm project

```
npm install
npm run build
```

## Install uv

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## mcpdoc

https://github.com/langchain-ai/mcpdoc

Install dependencies using `uv`

```
uv venv
source .venv/bin/activate
uv pip install .
```

### Check uvx path

```
source .venv/bin/activate
which uvx
```

### Test server locally

Use the same `uvx` as obtained in the venv above.

```
uvx --from mcpdoc mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
    --transport sse \
    --port 8082 \
    --host localhost
```

## MCP Inspector

```
npx @modelcontextprotocol/inspector
```

Connect to `mcpdoc` from MCP Inspector's WebUI interface.

Click Tools->List tools

Run list_doc_sources tool.

Copy the URL: https://python.langchain.com/llms.txt

Run the tool fetch_docs using this URL.

## Test mcpdoc with claude

Note: Use the uvx binary path used in the venv.

```
{
  "mcpServers": {
    "langgraph-docs-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "mcpdoc",
        "mcpdoc",
        "--urls",
        "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt",
        "--transport",
        "stdio",
        "--port",
        "8082",
        "--host",
        "localhost"
      ]
    }
  }
}

```

## Troubleshooting

Error:
```
langgraph-docs-mcp] [error] spawn uvx ENOENT
```

## Python project and initialize venv

```
un init shellserver
cd shellserver
uv venv
source .venv/bin/activate
```

## References

https://modelcontextprotocol.io/docs/getting-started/intro
https://docs.cursor.com/en/context/mcp
https://github.com/modelcontextprotocol/quickstart-resources
https://github.com/emarco177/mcp-crash-course

