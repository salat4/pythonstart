choice = input(
    "Оберіть операцію (1 - перевести з Цельсія в Фаренгейт, 2 - перевести з Фаренгейта в Цельсія): ")
if choice == "1":
    celsius = float(input("Введіть температуру в градусах Цельсія: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} градусів Цельсія дорівнює {fahrenheit} градусів Фаренгейта.")
elif choice == "2":
    fahrenheit = float(input("Введіть температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} градусів Фаренгейта дорівнює {celsius} градусів Цельсія.")
else:
    print("Ви ввели некоректний вибір. Оберіть 1 або 2.")
