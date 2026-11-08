# hello.py
import os

from llm import LLMClient
from fake_llm import FakeLLM


def main() -> None:
    llm = make_llm()
    answer = llm.ask("Ответь одним словом: работает?")
    print("Ответ модели:", answer)

def make_llm() -> LLMClient | FakeLLM:
    if os.environ.get("LLM_API_KEY") is None:
        return FakeLLM("задайте LLM_API_KEY")
    else:
        return LLMClient()


if __name__ == "__main__":
    main()