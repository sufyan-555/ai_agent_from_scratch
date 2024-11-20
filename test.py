import os
from dotenv import load_dotenv
from agent import Agent 
from tools import calculator
load_dotenv()
api = os.environ['hf_api']

tools = {
    "calculator": calculator
}

agent = Agent(token=api, tools=tools,)

query = "how are you?"
out = agent.ask(query,verbose=True)

print(out)
print()
print(agent.get_chats())
print("=======================================")

query = "what is 125 times 165?"
out = agent.ask(query,verbose=True)

print(out)
print()
print(agent.get_chats())
print("=======================================")