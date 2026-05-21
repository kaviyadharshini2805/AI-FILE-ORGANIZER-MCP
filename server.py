from mcp.server.fastmcp import FastMCP
from tools.files_tools import (
    list_files,
    create_folder,
    move_file
)

mcp = FastMCP("AI File Organizer")

@mcp.tool()
def get_files(path: str):
    return list_files(path)

@mcp.tool()
def make_folder(path: str):
    return create_folder(path)

@mcp.tool()
def move(source: str, destination: str):
    return move_file(source, destination)

if __name__ == "__main__":
    print("MCP Server Running...")
    mcp.run(transport="stdio")