from mcp import ClientSession
from mcp.client.sse import sse_client


async def check():
    async with sse_client("http://0.0.0.0:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List avail tool
            tools = await session.list_tools()
            print(tools)

            # Call add tool
            result = await session.call_tool("add", arguments={"a": 4, "b": 6})
            print(result)

            # Get tax code
            result = await session.read_resource("resource://ma_so_thue")
            print("Tax code = {}".format(result))

            prompt = await session.get_prompt("review_sentences", arguments={"text": "hello"})
            print("Prompt = {}".format(prompt))


if __name__ == "__main__":
    import asyncio

    asyncio.run(check())
