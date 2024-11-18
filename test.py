import os
from dotenv import load_dotenv
from agent import Agent 
from tools import calculator
load_dotenv()
api = os.environ['hf_api']

tools = [{
    "tool_name": "calculator",
    "tool": calculator
}]

agent = Agent(token=api, tools=tools,)

query = "how are you?"
out = agent.ask(query,verbose=True)

print(out)
print()
print(agent.get_chats())
print("=======================================")

query = "what is area of sqare of side lenght 16.25"
out = agent.ask(query,verbose=True)

print(out)
print()
print(agent.get_chats())
print("=======================================")