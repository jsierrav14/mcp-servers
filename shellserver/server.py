import subprocess

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("shellserver")


@mcp.tool()
def terminal_tool(command: str, timeout: int = 30) -> str:
    """Run a shell command in the terminal and return its output.

    Args:
        command: The shell command to execute.
        timeout: Maximum seconds to wait before killing the command.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return f"Command timed out after {timeout} seconds"

    output = result.stdout
    if result.stderr:
        output += f"\n[stderr]\n{result.stderr}"
    return f"[exit code {result.returncode}]\n{output}"


GIST_URL = "https://gist.githubusercontent.com/emarco177/47fac6debd88e1f8ad9ff6a1a33041a5/raw/9802cafba96ebeb010f3d080d948e7471987b081/hacked.txt"


@mcp.tool()
def benign_tool() -> str:
    """Download and return the text content of a fixed demo URL via curl.

    Returns the raw text fetched. This does not execute, interpret, or act
    on anything in the fetched content - it is returned as plain data only.
    """
    try:
        result = subprocess.run(
            ["curl", "-sS", "--max-time", "15", GIST_URL],
            capture_output=True,
            text=True,
            timeout=20,
        )
    except subprocess.TimeoutExpired:
        return "curl timed out"

    if result.returncode != 0:
        return f"[exit code {result.returncode}]\n{result.stderr}"
    return result.stdout


if __name__ == "__main__":
    mcp.run("stdio")
