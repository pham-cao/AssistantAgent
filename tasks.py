from crewai import Task
from tools import tool
# from agents import news_researcher, news_writer
#
# # researcher task
# research_task = Task(
#     description=(
#         "Identify the next big trend in {topic}."
#         "Focus on identifying pros and cons and the overall narrative."
#         "Your final report should clearly articulate the key points,"
#         "its market opportunities, and potential risks."
#     ),
#     expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
#     tools=[tool],
#     agent=news_researcher
# )
#
# # writing task with language model configuration
# write_task = Task(
#     description=(
#         "Compose an insightful article on {topic}."
#         "Focus on the latest trends and how it's impacting the industry."
#         "This article should be easy to understand, engaging, and positive."
#     ),
#     expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
#     tools=[tool],
#     agent=news_writer,
#     async_execution=False,
#     output_file='news.md'
# )

from agents import info_collector, retriever, support_advisor

collect_task = Task(
    description="Phân tích câu hỏi sau từ sinh viên: `{question}`. Xác định họ đang hỏi về vấn đề gì (học phí, môn học, giấy tờ...)",
    expected_output="Tên loại yêu cầu + tóm tắt nội dung câu hỏi.",
    agent=info_collector
)

retrieve_task = Task(
    description="Dựa trên loại yêu cầu: `{requirement_type}`, hãy tìm thông tin chính xác từ tài liệu nhà trường.",
    expected_output="Thông tin chính thức từ tài liệu, được trích dẫn rõ ràng.",
    agent=retriever
)

respond_task = Task(
    description="Dựa trên thông tin truy xuất: `{retrieved_info}`, hãy trả lời sinh viên bằng giọng điệu thân thiện, dễ hiểu.",
    expected_output="Câu trả lời hoàn chỉnh, rõ ràng, như một cố vấn học vụ.",
    agent=support_advisor
)