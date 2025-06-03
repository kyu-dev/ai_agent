from google.adk.agents import Agent


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "formula1 "
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about formula 1"
    ),

)