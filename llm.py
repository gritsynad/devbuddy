# llm.py
import os

from openai import OpenAI


class LLMClient:
    """Обёртка над OpenAI-совместимым API.

    Провайдер меняется переменными окружения, код не меняется:
    OpenRouter, Ollama и другие понимают один и тот же протокол.
    """

    def __init__(self) -> None:
        if not os.environ.get("LLM_MODEL"):
            raise ValueError("Задайте LLM_MODEL — имя модели в переменных окружения")

        self.client = OpenAI(
            base_url=os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1"),
            api_key=os.environ.get("LLM_API_KEY", ""),
        )
        self.model = os.environ["LLM_MODEL"]

    def ask(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content