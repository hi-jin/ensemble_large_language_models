import openai


class OpenAI_API:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.__set_api_key()
    
    def __set_api_key(self):
        openai.api_key = self.api_key
