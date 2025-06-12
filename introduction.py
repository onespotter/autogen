from autogen_core.models import UserMessage
from autogen_ext.models.ollama import OllamaChatCompletionClient
import asyncio

ollama_model_client= OllamaChatCompletionClient(model="llama3.2")

async def main():
    resposne = await ollama_model_client.create([UserMessage(content="what is autogen AI?", source="user")])
    print(resposne)
    await ollama_model_client.close()

asyncio.run(main())
