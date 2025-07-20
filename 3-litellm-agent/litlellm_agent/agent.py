from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import random
import os

def get_dad_joke():
    jokes = [
      "why bird fly? cause they dont walk"
    ]
    return random.choice(jokes)

model = LiteLlm(    
    model="openrouter/meta-llama/llama-4-scout:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

root_agent = Agent(
    model=model,
    name='litlellm_agent',
    description='dad jokes agent',
    instruction="""
     you are a funny assistant tath can replly by joke using that : tool'get_that_joke'
    """,
    tools=[get_dad_joke],
    
)


