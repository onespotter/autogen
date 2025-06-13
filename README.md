solo# autogen

AutoGen is a framework for building AI Agents and applications.
Microsoft product.

AutoGen has 2 versiosn: 
- AutoGen 0.2 ( AG2)
- AutoGen 0.4 (Microsoft started ) :
   +Async foundation
   +faster
   +More flexible.
   +Layered API design :
      ++ AgentChat => Quick and high level. focused on tasks
      ++ Core Layer => Low level

-   ![image](https://github.com/user-attachments/assets/e6ad4282-8d16-4b69-8e74-12ab8e142a57)
    +Better observability

-   https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/

-   https://microsoft.github.io/autogen/stable//index.html
-   Agents are hepful to write blogs, analyzing , debugging etc.

python -m venv autogen-env
source autogen-env/bin/activate

+Installation of AutoGen
https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/index.html

  ++ pip install -U "autogen-agentchat"
  ++dotenv
  ++pydantic
  ++asyncio

To create an agent => Need LLM 
- Human Intelligence
- Artificial Intelligence

- Install :
      pip install "autogen-ext[openai]"
      pip install -U "autogen-ext[ollama]"
      pip install autogen_core
- AutoGen extensions: 



https://microsoft.github.io/autogen/stable/user-guide/extensions-user-guide/index.html


# AutoGen, Langchain, Crewai, LlamaIndex
AutoGen is a multi agent AI system with an asynchronous, event driven architecture. 
Scalable and allows dynamic agent interactions.
#AutoGen vs Langchain
- Achitecture: Langchain has a chainbased sequential execution model whereas autogen has event driven async architecture.
- Multi Agent Capabilities => Autogen excels in autonomous multi-agent collboration. Langchain focuses on a single-agent workflow with structred steps.
- Observability: Autogen has better event tracking and langchian has basic tracing
- Scalability : Autogen can easily scaling on complex agent netwroks, langchain synchronous design  it struggle with large scale system.
- Use case : Autogen good for collborative AI


