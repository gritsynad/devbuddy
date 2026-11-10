from prompts import build_review_prompt

DIFF = 'x = {"a": 1}\nprint(f"итого: ${x}")'
RULES = ["не используй global", "проверяй границы списков"]


def test_rules_as_list():
    prompt = build_review_prompt(DIFF, RULES)
    assert "- не используй global" in prompt
    assert "- проверяй границы списков" in prompt


def test_diff_verbatim():
    prompt = build_review_prompt(DIFF, RULES)
    assert DIFF in prompt


def test_format_example_present():
    prompt = build_review_prompt("a = 1", ["правило"])
    assert '"comments"' in prompt


def test_survives_special_chars():
    nasty = 'цена = ${x} и словарь {"k": "v"}'
    prompt = build_review_prompt(nasty, ["правило"])
    assert nasty in prompt


def test_multiple_rules_on_separate_lines():
    prompt = build_review_prompt("a = 1", RULES)
    lines = [line for line in prompt.splitlines() if line.startswith("- ")]
    assert len(lines) >= 2