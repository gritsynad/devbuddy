# Заглушка
class FakeLLM:

    def __init__(self, answer) -> None:
        self.answer = answer

    def ask(self, prompt: str) -> str:
        return self.answer