import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Вгадайте число від 1 до 100: "))
            attempts += 1

            if guess == secret_number:
                print(
                    f"Вітаємо, ви вгадали число {secret_number} за {attempts} спроб!")
                break
            elif guess < secret_number:
                print("Спробуйте більше число.")
            else:
                print("Спробуйте менше число.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")


guess_number()
