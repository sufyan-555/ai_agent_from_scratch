import os
from pprint import pprint as pp
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
out = agent.ask(query)

print(out)
print()
pp(agent.get_chats())
print("=======================================")

query = "what is 125 times 165?"
out = agent.ask(query)

print(out)
print()
pp(agent.get_chats())
print("=======================================")


query = "what is area of square with side length of 16.25?"
out = agent.ask(query)

print(out)
print()
pp(agent.get_chats())
print("=======================================")



### OUTPUT from the tool

# Final response: I'm Phi, an AI digital assistant. I don't have feelings, but I'm here and ready to help you!
# I'm Phi, an AI digital assistant. I don't have feelings, but I'm here and ready to help you!

# [{'content': 'how are you?', 'role': 'user'},
#  {'content': '{"key": "response", "content": "I"m Phi, an AI digital '
#              'assistant. I don"t have feelings, but I"m here and ready to help '
#              'you!"}',
#   'role': 'assistant'}]
# =======================================
# Calling tool
# Tool: calculator
# Args: {'num1': 125, 'num2': 165, 'operator': '*'}
# Thought: User asked for the product of 125 and 165. Advising the use of the calculator tool.
# Tool Response: result from tool: 20625.0, message: The result of 125.0 multiplication 165.0 is: 20625.0
# Final response: The product of 125 and 165 is 20625.
# The product of 125 and 165 is 20625.

# [{'content': 'how are you?', 'role': 'user'},
#  {'content': '{"key": "response", "content": "I"m Phi, an AI digital '
#              'assistant. I don"t have feelings, but I"m here and ready to help '
#              'you!"}',
#   'role': 'assistant'},
#  {'content': 'what is 125 times 165?', 'role': 'user'},
#  {'content': '{"key": "action", "content": {"tool": "calculator", "args": '
#              '{"num1": 125, "num2": 165, "operator": "*"}}, "thought": "User '
#              'asked for the product of 125 and 165. Advising the use of the '
#              'calculator tool."}',
#   'role': 'assistant'},
#  {'content': 'result from tool: 20625.0, message: The result of 125.0 '
#              'multiplication 165.0 is: 20625.0',
#   'role': 'user'},
#  {'content': '{"key": "response", "content": "The product of 125 and 165 is '
#              '20625."}',
#   'role': 'assistant'}]
# =======================================
# Calling tool
# Tool: calculator
# Args: {'num1': 16.25, 'num2': 16.25, 'operator': '*'}
# Thought: User asked for the area of a square with a side length of 16.25. Advising the use of the calculator tool with the square of the side length.
# Tool Response: result from tool: 264.0625, message: The result of 16.25 multiplication 16.25 is: 264.0625
# Final response: The area of a square with a side length of 16.25 is 264.0625 square units.
# The area of a square with a side length of 16.25 is 264.0625 square units.

# [{'content': 'how are you?', 'role': 'user'},
#  {'content': '{"key": "response", "content": "I"m Phi, an AI digital '
#              'assistant. I don"t have feelings, but I"m here and ready to help '
#              'you!"}',
#   'role': 'assistant'},
#  {'content': 'what is 125 times 165?', 'role': 'user'},
#  {'content': '{"key": "action", "content": {"tool": "calculator", "args": '
#              '{"num1": 125, "num2": 165, "operator": "*"}}, "thought": "User '
#              'asked for the product of 125 and 165. Advising the use of the '
#              'calculator tool."}',
#   'role': 'assistant'},
#  {'content': 'result from tool: 20625.0, message: The result of 125.0 '
#              'multiplication 165.0 is: 20625.0',
#   'role': 'user'},
#  {'content': '{"key": "response", "content": "The product of 125 and 165 is '
#              '20625."}',
#   'role': 'assistant'},
#  {'content': 'what is area of square with side length of 16.25?',
#   'role': 'user'},
#  {'content': '{"key": "action", "content": {"tool": "calculator", "args": '
#              '{"num1": 16.25, "num2": 16.25, "operator": "*"}}, "thought": '
#              '"User asked for the area of a square with a side length of '
#              '16.25. Advising the use of the calculator tool with the square '
#              'of the side length."}',
#   'role': 'assistant'},
#  {'content': 'result from tool: 264.0625, message: The result of 16.25 '
#              'multiplication 16.25 is: 264.0625',
#   'role': 'user'},
#  {'content': '{"key": "response", "content": "The area of a square with a side '
#              'length of 16.25 is 264.0625 square units."}',
#   'role': 'assistant'}]
# =======================================