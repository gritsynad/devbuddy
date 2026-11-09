

import math

import unicodedata

"""
грубая оценка числа токенов в тексте по учебной модели
"""
def estimate_tokens(text: str) -> int:
    if text == "":
        return 0
    chars = list(text)
    number = 0.0
    for char in chars:
        number += get_char_tokens(char)
    return math.ceil(number)

def get_char_tokens(char) -> float:
    name = unicodedata.name(char, "")
    if "CYRILLIC" in name:
        return 0.5
    return 0.25

"""
влезет ли запрос в окно модели
"""
def fits_in_context(prompt_tokens: int,
                    diff_tokens: int,
                    context_window: int,
                    output_reserve: int) -> bool:
    return prompt_tokens + diff_tokens + output_reserve <= context_window

"""
месячная стоимость агента
"""
def monthly_cost(prs_per_day: int,
                 input_tokens: int,
                 output_tokens: int,
                 price_in: float,
                 price_out: float,
                 days: int = 22) -> float:
    one_input_cost = (input_tokens / 1_000_000) * price_in
    one_output_cost = (output_tokens / 1_000_000) * price_out
    one_pr_cost = one_input_cost + one_output_cost
    one_day_cost = one_pr_cost * prs_per_day
    month_cost = one_day_cost * days
    return round(month_cost, 2)


