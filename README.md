# mcp-servers

A collection of projects for learning and experimenting with the [Model Context Protocol](https://modelcontextprotocol.io) (MCP).

## Projects

| Folder | Description |
|--------|-------------|
| [mcp-crash-course](mcp-crash-course) | Python project for the MCP crash course, using `langchain-mcp-adapters` to connect LangChain to MCP servers. |
| [quickstart-resources](quickstart-resources) | Official MCP quickstart examples: weather servers and clients in Go, Python, Ruby, Rust and TypeScript. |
| [shellserver](shellserver) | Minimal Python MCP server that exposes a `terminal_tool` for running shell commands. |

Each folder has its own README with setup and usage details.

## Requirements

- Python 3.10+ and [uv](https://docs.astral.sh/uv/) for the Python projects
- Other toolchains (Node, Go, Ruby, Rust) only for the matching `quickstart-resources` examples

## Getting started

```sh
git clone https://github.com/jsierrav14/mcp-servers.git
cd mcp-servers/mcp-crash-course
uv sync
```

## Notes

`quickstart-resources` is copied from [modelcontextprotocol/quickstart-resources](https://github.com/modelcontextprotocol/quickstart-resources) and keeps its original license.
