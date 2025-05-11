import re
from typing import Callable, Generator
# Генерує дійсні числа з тексту, які відокремлені пробілами.

def generator_numbers(text: str) -> Generator[float, None, None]:

    # Шаблон: пробіл перед і після числа
    pattern = r'(?<=\s)\d+\.\d+(?=\s)'
    for match in re.findall(pattern, f' {text} '):
        yield float(match)

# Повертає суму всіх дійсних чисел, отриманих з генератора.
def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:

    return sum(func(text))


# Приклад використання
text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
