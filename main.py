'''ФУНКЦІЯ caching_fibonacci
    Створити порожній словник cache

    ФУНКЦІЯ fibonacci(n)
        Якщо n <= 0, повернути 0
        Якщо n == 1, повернути 1
        Якщо n у cache, повернути cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Повернути cache[n]

    Повернути функцію fibonacci
КІНЕЦЬ ФУНКЦІЇ caching_fibonacci'''



def caching_fibonacci():
    cache = {}


    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci( n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(10))

print(fib(20))



# Друге завдання :


def generator_numbers(text: str):
    for x in text.split():
        try:
            yield float(x)
        except ValueError:
            continue




def sum_profit(text: str, func):
    numbers = func(text)
    total = sum(numbers)
    return total

    


text = "Загальний дохід працівника складається з декількох частин:" \
" 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і " \
"324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

