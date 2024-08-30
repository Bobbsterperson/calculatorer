import pytest
# import re
from calculatorer import calc


# def calculate(expression: str) -> float:
#     return validations(expression)

# def validations(expression):
#     if "," in expression:
#         raise ValueError("no ',' pls")
#     elif "(" in expression and ")" not in expression:
#         raise ValueError("open '(' but not closed")
#     elif ")" in expression and "(" not in expression:
#         raise ValueError("closed ')' but not opened")
#     elif "**" in expression or "//" in expression:
#         pass
#     elif re.search(r'[\+\-\*/]{2,}', expression):
#         raise ValueError("more than one operator")
#     elif "]" in expression or "[" in expression or "{" in expression or "}" in expression:
#         raise ValueError("no brackets pls")
#     elif "/ 0" in expression or "// 0" in expression:
#         raise ZeroDivisionError("division by zero error")
#     try:
#         result = eval(expression)
#         return result
#     # except ZeroDivisionError as e:
#     #     raise ZeroDivisionError(f"Division by zero error: {str(e)}")
#     except NameError as e:
#         raise ValueError(f"Invalid expression with undefined variable: {str(e)}")
#     except Exception as e:
#         raise ValueError(f"Invalid expression: {str(e)}")


@pytest.mark.parametrize("n, expected_result", [
    ("1 + 2", 3),
    ("2 * 3", 6),
    ("10 / 2", 5),
    ("5 - 1", 4),
    ("1 + (3 * 6 - 2) / 2", 9.0),
    ("(2 + 3) * (4 - 2)", 10),
    ("3 * (2 + 1) / 2 + 7 - 1", 10.5),
    ("0 / 10", 0),
    ("2 ** 3", 8),
    ("0.1 - 0.2", -0.1),
    ("00.1 - 0.2", -0.1),
    ("8 % 2", 0),
    ("2 ** 3 ** 2", 512),
    ("0.01 * 6", 0.06),
    ("10 ** 20", 100000000000000000000),
    ("80 // 4", 20),
    ("5 * 0", 0),
    ("+ 3", 3),
    ("-2 + -1", -3),
    ("-2 * -1", 2),
    ("-1 - (-1)", 0),
    ("1 * 6", 6),
])
def test_calculate(n, expected_result):
    try:
        actual_result = calc(n)
        assert actual_result == expected_result, f"Failed for '{n}': expected {expected_result}, got {actual_result}"
    except Exception as e:
        pytest.fail(f"Unexpected exception for '{n}': {e}")

@pytest.mark.parametrize("n", [
    "10 / 0",
    "1,000 + 1",
    "a * 4",
    "(2 + 3",
    "2 + 3)",
    "1a + 2",
    "1 *- 2",
    "* 1",
    "4 -",
    "/ 3",
    "2 + 3 /",
    "8 %% 2",
    "2 ** 3  2",
    "[2]",
    "__",
    "0000000000000001 * 6",
    "2 + (3 * 4",
    "salamander",
])
def test_invalid_cases(n):
    with pytest.raises((ValueError, ZeroDivisionError)):
        calc(n)
