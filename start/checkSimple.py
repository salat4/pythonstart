import math

number = int(input("Введіть число: "))

is_prime = True
for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} - просте число.")
else:
    print(f"{number} - не просте число.")
