from huggingface_hub import InferenceClient
import json as json
from prompts import system_prompt as system_prompt

class Agent:
    def __init__(self,token,max_tokens=150,temperature=0.1,tools=None):
        """
        Initializes an Agent object with the given Hugging Face API token, maximum number of response tokens, and response temperature.
        
        Args:
            token (str): Hugging Face API token. Defaults to the token used in the example.
            max_tokens (int): Maximum number of tokens in the response. Defaults to 100.
            temperature (float): Response temperature. Defaults to 0.1.
            tools (dict): List of tools to use passed as {'tool_name1': tool1,...} Defaults to None.
        """
        try:
            self.model =InferenceClient(
            model = "microsoft/Phi-3.5-mini-instruct",
            #model="mistralai/Mistral-7B-Instruct-v0.3",
            token = token)
        except Exception as e:
            print(f"Error: Could not create inference client. {e}")
            raise e
        self.system_prompt = system_prompt
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.chat = [{'role': 'system', 'content': self.system_prompt}]
        self.tools = tools
    
    def get_chats(self):
        """
        Returns the current chat history.

        Returns:
            list: The current chat history. Each item is a dict with 'role' and 'content' keys.
        """
        return self.chat[1:]

    def ask(self,query,max_iter=5,verbose=True):
        """
        Asks the AI agent a question and returns its response.

        Args:
            query (str): The question to ask the AI agent.
            max_iter (int): (defautls to 5) The maximum no of times the agent will go in a thought loop
            verbose (bool): (defautls to True) Whether to print the thought loop

        Returns:
            response object
        """
        iteration = 0
        while iteration < max_iter:

            if len(self.chat) > 20:
                self.chat = self.chat[10:]

            self.chat.append({'role': 'user', 'content': query})
            response = self.model.chat_completion(
                messages = self.chat,
                temperature = 0,
                max_tokens= 500
            )

            out = response.choices[0].message.content
            try:
                out = json.loads(out)
            except Exception as e:
                print("Response Error")
                print(out)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                raise e
            
            ## added replace because the json object have '' in the string and the model picks that up from the
            ## chat history and gives '' in repsonse, beacuse of which the json.loads fails, so making it "" model will be able to follow the
            ## pattern better.
            self.chat.append({'role': 'assistant', 'content': str(out).replace("'",'"')})

            if out['key'] == 'action':
                # handlling tool call
                tool_name = out['content']['tool']
                if tool_name not in self.tools.keys():
                    self.chat.append({'role': 'user', 'content': f"Tool {tool_name} not found"})
                    continue
                args = out['content']['args']
                tool = self.tools[tool_name]
                response = tool(**args)
                query = response
                iteration += 1

                if verbose:
                    print("Calling tool")
                    print(f"Tool: {tool_name}")
                    print(f"Args: {args}")
                    print(f"Thought: {out['thought']}")
                    print(f"Tool Response: {response}")
                
            elif ((out['key'] == 'response') & (out['content'] != None)):
                if verbose:
                    print(f"Final response: {out['content']}")
                return out['content']
            else:
                if verbose:
                    print(f"Final response: {out}")
                return out

        print("Max iteration reached")
        return self.chat[-1]  
            
    