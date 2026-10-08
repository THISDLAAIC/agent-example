import json

from openai import OpenAI

from agent import Agent
from model import OpenAIModel

with open("config.json", "r") as config_file:
    config = json.load(config_file)

model = None

if config["provider_type"] == 'openai':
    model = OpenAIModel(
        OpenAI(
            base_url=config['provider_base_url'],
            api_key=config['provider_api_key']
        ),
        config['provider_model_name']
    )

agent = Agent(
    model
)
agent.start_loop()
