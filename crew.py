# from crewai import Crew, Process
# from tasks import research_task, write_task
# from agents import news_researcher, news_writer
#
#
# # forming the tech focused crew with some enhanced configuration
# crew = Crew(
#     agents=[news_researcher, news_writer],
#     tasks=[research_task, write_task],
#     process=Process.sequential,
# )
#
# # starting the task execution process with enhanced feedback
#
# result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
# print(result)


from crewai import Crew
from tasks import collect_task, retrieve_task, respond_task

crew = Crew(
    agents=[collect_task.agent, retrieve_task.agent, respond_task.agent],
    tasks=[collect_task, retrieve_task, respond_task],
    verbose=True
)