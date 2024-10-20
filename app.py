import random

def generate_number():
    """Генерирует четырехзначное число, в котором нет повторяющихся цифр."""
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def count_bulls_and_cows(secret, guess):
    """Считает количество быков и коров."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def is_valid_guess(guess):
    """Проверяет, что введенное число является четырехзначным и не содержит повторяющихся цифр."""
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4

def display_rules():
    """Выводит правила игры."""
    print("Правила игры 'Быки и коровы':")
    print("1. Я загадаю четырехзначное число, в котором нет повторяющихся цифр.")
    print("2. Ваша задача - угадать это число.")
    print("3. После каждой попытки я сообщу вам, сколько 'быков' и 'коров' вы угадали.")
    print("   - 'Бык' означает, что вы угадали цифру и её позицию.")
    print("   - 'Корова' означает, что вы угадали цифру, но не её позицию.")
    print("4. Вы можете ввести 'стоп', чтобы завершить игру в любой момент.")
    print("5. Удачи!\n")

def start_game():
    """Запускает игру."""
    secret_number = generate_number()
    attempts = 0
    print("Добро пожаловать в игру 'Быки и коровы'!")

    while True:
        guess = input("Введите ваш вариант (четыре разные цифры) или 'стоп' для выхода: ")

        if guess.lower() == 'стоп':
            print("Игра окончена. Спасибо за игру!")
            break

        if not is_valid_guess(guess):
            print("Некорректный ввод. Убедитесь, что вы ввели четыре разные цифры.")
            continue

        attempts += 1
        bulls, cows = count_bulls_and_cows(secret_number, guess)
        print(f"Быки: {bulls}, Коровы: {cows}")

        if bulls == 4:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток!")
            break

def main():
    display_rules()  # Показываем правила игры только один раз
    while True:
        command = input("Введите 'начать' для начала игры или 'выход' для завершения: ")
        if command.lower() == 'начать':
            start_game()
        elif command.lower() == 'выход':
            print("Выход из игры. До свидания!")
            break
        else:
            print("Некорректная команда. Пожалуйста, введите 'начать' или 'выход'.")

if __name__ == "__main__":
    main()
