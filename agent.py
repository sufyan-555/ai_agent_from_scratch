from huggingface_hub import InferenceClient
from prompts import system_prompt as system_prompt

model = InferenceClient(
    model = "microsoft/Phi-3.5-mini-instruct",
    token = "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"
)


class Agent:
    def __init__(self,token,max_tokens=100,temperature=0.1):
        """
        Initializes an Agent object with the given Hugging Face API token, maximum number of response tokens, and response temperature.
        
        Args:
            token (str): Hugging Face API token. Defaults to the token used in the example.
            max_tokens (int): Maximum number of tokens in the response. Defaults to 100.
            temperature (float): Response temperature. Defaults to 0.1.
        """
        self.model =InferenceClient(
        model = "microsoft/Phi-3.5-mini-instruct",
        token = token)
        self.system_prompt = system_prompt
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.chat = [{'role': 'system', 'content': self.system_prompt}]
    
    def get_chats(self):
        """
        Returns the current chat history.

        Returns:
            list: The current chat history. Each item is a dict with 'role' and 'content' keys.
        """
        return self.chat

    def ask(self,query):
        """
        Asks the AI agent a question and returns its response.

        Args:
            query (str): The question to ask the AI agent.

        Returns:
            response object
        """
        self.chat.append({'role': 'user', 'content': query})
        if len(self.chat) > 20:
            self.chat = self.chat[10:]
        response = self.model.chat_completion(
            messages = self.chat,
            temperature = 0,
            max_tokens= 500
        )
        self.chat.append({'role': 'assistant', 'content': response.choices[0].message.content})
        return response.choices[0].message.content
    