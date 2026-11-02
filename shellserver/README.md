# shellserver

A minimal [MCP](https://modelcontextprotocol.io) server built with the Python SDK. It exposes a single tool that runs terminal commands.

## Tool

### `terminal_tool`

Runs a shell command and returns its exit code, stdout and stderr.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `command` | string | required | The shell command to execute |
| `timeout` | int | `30` | Seconds to wait before the command is killed |

## Setup

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
```

## Run

```sh
uv run server.py
```

The server communicates over stdio.

## Use with Claude Code

```sh
claude mcp add shellserver -- uv --directory /absolute/path/to/shellserver run server.py
```

## Use with Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "shellserver": {
      "command": "uv",
      "args": ["--directory", "/absolute/path/to/shellserver", "run", "server.py"]
    }
  }
}
```

## Security

This tool executes arbitrary commands with your user's permissions and no restrictions. Only connect it to clients you trust.
