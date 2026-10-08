from abc import ABC, abstractmethod

from openai import OpenAI


class Model(ABC):
    @abstractmethod
    def generate_message(self, messages) -> str:
        pass


class OpenAIModel(Model):
    def __init__(self, openai_client: OpenAI, model_name: str):
        self.openai_client = openai_client
        self.model_name = model_name

    def generate_message(self, messages):
        response = self.openai_client.chat.completions.create(
            model="deepseek-flash",
            messages=messages,
        )

        return response.choices[0].message.content

class AnthropicModel(Model):
    pass