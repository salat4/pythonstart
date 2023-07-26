firstNumber = float(input())
secondNumber = float(input())
thirdNumber = float(input())
numberArray = [firstNumber, secondNumber, thirdNumber]


def insertSort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and current_value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value


insertSort(numberArray)
print(numberArray)
