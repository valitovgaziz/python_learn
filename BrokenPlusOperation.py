firstNumber = input()
secondNumber = input()
result = ""

if len(firstNumber) > len(secondNumber):
    for nextDigit in range(0, len(secondNumber)):
        firstDigit = int(firstNumber[len(firstNumber) - 1 - nextDigit])
        secondDigit = int(secondNumber[len(secondNumber) - 1 - nextDigit])
        nextSumDigit = firstDigit + secondDigit
        result = str(nextSumDigit)[-1] + result
    length = len(firstNumber) - len(secondNumber)
    result = str(firstNumber)[:length] + result
else:
    for nextDigit in range(0, len(firstNumber)):
        firstDigit = int(firstNumber[len(firstNumber) - 1 - nextDigit])
        secondDigit = int(secondNumber[len(secondNumber) - 1 - nextDigit])
        nextSumDigit = firstDigit + secondDigit
        result = str(nextSumDigit)[-1] + result
    length = len(secondNumber) - len(firstNumber)
    result = str(secondNumber)[:length] + result
print(result)