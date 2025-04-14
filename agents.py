import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# call gemini model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',
                            verbose=True,
                            temperature=0.5,
                            goggle_api_key=os.getenv('GOOGLE_API_KEY'))               

info_collector = Agent(
    role="Information Collector",
    goal="Hiểu câu hỏi của sinh viên và xác định yêu cầu cần hỗ trợ",
    backstory="Là trợ lý học vụ, có khả năng nắm bắt nhu cầu sinh viên rất nhanh.",
    verbose=True,
    memory=True,
    llm=llm
)

retriever = Agent(
    role="Knowledge Retriever",
    goal="Tìm kiếm thông tin liên quan từ tài liệu quy định và học vụ",
    backstory="Thông thạo các quy định và thông tin trường đại học.",
    verbose=True,
    memory=True,
    llm=llm
)

support_advisor = Agent(
    role="Student Support Advisor",
    goal="Trả lời sinh viên một cách rõ ràng, thân thiện và chính xác",
    backstory="Là người hướng dẫn sinh viên, luôn giúp các bạn giải tỏa thắc mắc học tập.",
    verbose=True,
    memory=True,
    llm=llm
)

#
#
#
#
# # create a senior researcher agent with memory and verbose mode
#
# news_researcher = Agent(
#         role="Senior Researcher",
#         goal="Uncover ground breaking technologies in {topic}",
#         verbose=True,
#         memory=True,
#         backstory=( "Driven by curiosity, you're at the forefront of"
#         "innovation, eager to explore and share knowledge that could change"
#         "the world."
#         ),
#         tools=[tool],
#         llm=llm,
#         allow_delegation=True
# )
#
# # creating a write agent with custom tools responsible in writing news blog
#
# news_writer = Agent(
#     role="Writer",
#     goal="Narrate compelling tech stories about {topic}",
#     verbose=True,
#     memory=True,
#     backstory=(
#          "With a flair for simplifying complex topics, you craft"
#          "engaging narratives that captivate and educate, bringing new"
#          "discoveries to light in an accessible manner."
#     ),
#     tools=[tool],
#     llm=llm,
#     allow_delegation=False
# )