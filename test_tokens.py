from tokens import estimate_tokens, fits_in_context, monthly_cost


def test_empty_text():
    assert estimate_tokens("") == 0


def test_english():
    # 11 символов латиницы -> ceil(11 / 4) = 3
    assert estimate_tokens("hello world") == 3


def test_russian():
    # 6 кириллических букв -> ceil(6 / 2) = 3
    assert estimate_tokens("привет") == 3


def test_mixed():
    # кириллица 6 -> 3 токена, прочие 8 символов -> 2 токена
    assert estimate_tokens("Привет, world!") == 5


def test_code():
    # 20 прочих символов -> ceil(20 / 4) = 5
    assert estimate_tokens("def main():\n    pass") == 5


def test_fits_true():
    assert fits_in_context(1500, 4000, 8000, 1000) is True


def test_fits_false():
    # 1500 + 6000 = 7500, а окно минус резерв даёт 7000
    assert fits_in_context(1500, 6000, 8000, 1000) is False


def test_fits_exact_edge():
    assert fits_in_context(0, 0, 100, 100) is True
    assert fits_in_context(1, 0, 100, 100) is False


def test_monthly_luna():
    # 440 ревью: (6000/1M * 0.10 + 1000/1M * 0.50) * 440
    assert monthly_cost(20, 6000, 1000, 0.10, 0.50) == 0.48


def test_monthly_sol():
    assert monthly_cost(20, 6000, 1000, 2.00, 10.00) == 9.68


def test_monthly_single_review():
    assert monthly_cost(1, 6000, 1000, 10.00, 50.00, days=1) == 0.11