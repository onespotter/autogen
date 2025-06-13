from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

API_KEY= os.getenv("OPENAI_API_KEY")

model_client=OpenAIChatCompletionClient(model="gpt-4o", api_key=API_KEY)
myFirstAgent=AssistantAgent(name="MYFIRSTNAME", model_client=model_client)

async def main():
    result= await myFirstAgent.run(task="Tell me about autogen AI Agent?")
    print(result)

asyncio.run(main())
