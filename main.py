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



# Четверте завдання :



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner




def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower() if parts else ""
    args = parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if not args:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all (contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()    


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()