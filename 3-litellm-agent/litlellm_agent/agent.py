from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os

model = LiteLlm(
    model="openrouter/deepseek/deepseek-r1-0528-qwen3-8b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

root_agent = Agent(
    model=model,
    name='litlellm_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)


