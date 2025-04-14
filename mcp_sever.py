from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="mcp-sever")


@mcp.tool()
def add(a: int, b: int) -> int:
    """add two numbers"""
    return a + b


@mcp.resource("resource://ma_so_thue")
def get_ma_so_thue() -> str:
    """get tax code"""
    return "0987654321"


@mcp.prompt()
def review_sentences(text: str) -> str:
    return "review this sentence"


if __name__ == "__main__":
    print("Listening...")
    mcp.run(transport="sse")
