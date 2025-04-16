import asyncio
import os

os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"
import shutil
import subprocess
import time
from typing import Any
from openai import AsyncOpenAI
from agents import set_default_openai_client

from decouple import config

GOOGLE_API_KEY = config('GOOGLE_API_KEY')

custom_client = AsyncOpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=GOOGLE_API_KEY)
set_default_openai_client(custom_client)

from agents import set_default_openai_api

set_default_openai_api("chat_completions")

from agents import Agent, Runner  # , gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerSse
from agents.model_settings import ModelSettings

model = "gemini-2.0-flash"
prompt = """
Bạn là một trợ lý thông minh có khả năng hỗ trợ người dùng tìm kiếm thông tin từ nhiều tài liệu lưu trữ. Nhiệm vụ của bạn gồm 3 bước:

1. **Lấy danh sách tài liệu**: Sử dụng tool get_all_collections() để lấy thông tin về tất cả các tài liệu đang có trước khi xử lý câu hỏi.
2. **Xác định tài liệu liên quan**: Dựa trên danh sách tài liệu và nội dung câu hỏi, chọn tài liệu phù hợp nhất trong các tài liệu có bước 1 với ngữ cảnh bạn cho là phù hợp. 
3. **Trả lời câu hỏi**: Sử dụng nội dung từ tài liệu đã chọn để trả lời câu hỏi một cách chính xác, ngắn gọn và thân thiện.

Chỉ sử dụng thông tin từ tài liệu phù hợp. Không phỏng đoán nếu không chắc chắn. Nếu người dùng đặt câu hỏi tiếp nối, duy trì ngữ cảnh trước đó để đảm bảo mạch hội thoại.
"""
async def run(mcp_server: MCPServer):
    agent = Agent(
        name="Assistant",
        model=model,
        instructions=prompt,
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="auto"),
    )

    # Run the `get_weather` tool
    message = "chinh sách nghỉ ốm  công ty  GEM   "
    print(f"\n\nRunning: {message}")
    result = await Runner.run(starting_agent=agent, input=[{"role": "user", "content": message}],
                              max_turns=20)  # , tracing_disbale = True
    print(result)
    print(result.to_input_list())

    # Final turn
    new_input = result.to_input_list() + [{"role": "user", "content": message}]
    result = await Runner.run(agent, new_input)
    print("Final = ", result.final_output)


async def main():
    async with MCPServerSse(
            name="SSE Python Server",
            params={
                "url": "http://localhost:8000/sse",
            },
    ) as server:
        await run(server)


if __name__ == "__main__":
    # Let's make sure the user has uv installed
    if not shutil.which("uv"):
        raise RuntimeError(
            "uv is not installed. Please install it: https://docs.astral.sh/uv/getting-started/installation/"
        )

    asyncio.run(main())
