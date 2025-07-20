from google.adk.agents import Agent
from pydantic import BaseModel, Field

class EmailOutput(BaseModel):
    subject: str = Field(description="The subject line of the email. need to be concise")
    body: str = Field(description="The main content of the email, should be well formated")



root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='email_agent',
    description='email_agent',
    instruction='You are a helpfull assistant that can write email for the user',
    output_schema=EmailOutput,
    output_key="email",
)
