def caching_fibonacci():
    cache = {}  # Локальний кеш

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевірка кешу
        if n in cache:
            return cache[n]

        # Рекурсивне обчислення з кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
