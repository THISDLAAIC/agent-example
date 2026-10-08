from model import Model

class Agent:

    def __init__(self, model: Model):
        self.model = model
        self.messages = []

    def start_loop(self):
        while True:
            prompt = input("You: ")
            self.messages.append({"role": "user", "content": prompt})
            response = self.model.generate_message(self.messages)
            print(f"Agent: {response}")

            self.messages.append({"role": "assistant", "content": response})