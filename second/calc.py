firstNumber = int(input("First Number"))
secondNumber = int(input("Second Number"))
operation = input("Operation")
match operation:
    case"+":
        answer = firstNumber + secondNumber
        print(answer)
    case"-":
        answer = firstNumber - secondNumber
        print(answer)
    case"/":
        answer = firstNumber / secondNumber
        print(answer)
    case"*":
        answer = firstNumber * secondNumber
        print(answer)
