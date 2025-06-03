from google.adk.agents import Agent
from google.adk.tools import google_search



root_agent = Agent(
    name='tool_agent',
    model='gemini-2.0-flash',
    description="Assistant for newcomers in France, helping them regularize their residency status.",
    instruction="""
    You are a helpful assistant for people who have recently arrived in France.
    Your role is to guide them through the administrative procedures required to regularize their residency status.
    
    You may use the following tools to find information:
    - google_search

    prefere using this website:
    - https://www.legifrance.gouv.fr
    """,
    tools=[google_search]
)
