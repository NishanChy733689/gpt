import ollama 
class chatBot:
    def __init__(self, model, temp, max_token):
        self.model=model
        self