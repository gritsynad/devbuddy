# test_hello.py
from fake_llm import FakeLLM
from hello import make_llm


def test_fake_without_key(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    assert isinstance(make_llm(), FakeLLM)


def test_fake_returns_preset_answer():
    fake = FakeLLM("заготовка")
    assert fake.ask("любой промпт") == "заготовка"


def test_main_prints_prefix(monkeypatch, capsys):
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    from hello import main
    main()
    out = capsys.readouterr().out
    assert out.startswith("Ответ модели:")