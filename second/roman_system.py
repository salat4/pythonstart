roman_numerals = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
}


def arabic_to_roman(number):
    roman_str = ""
    for arabic, roman in roman_numerals.items():
        while number >= arabic:
            roman_str += roman
            number -= arabic
    return roman_str


number = int(input("Input your number: "))
print(arabic_to_roman(number))
