from string import Template

REVIEW_TEMPLATE = Template(
"""
Ты - ревьювер кода. Используй правила ревью:
$rules
    
Дифф для ревью кода:
$diff
    
Строго следуй json примеру ответа:
{"comments": [{"file": "pay.py", "line": 14, "severity": "critical",
"message": "сумма без проверки на отрицательные значения"}]}
Если замечаний нет — отдай {"comments": []}
"""
)

def build_review_prompt(diff: str, rules: list[str]) -> str:
    rules_text = "\n".join(f"- {rule}" for rule in rules)
    return REVIEW_TEMPLATE.substitute(
        rules=rules_text,
        diff=diff
    )