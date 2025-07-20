from google.adk.agents import Agent


root_agent = Agent(
    name="formula1_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer formula1 question"
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about formula 1"
    ),

)