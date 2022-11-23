sumDecimal = int(input())
numberBinary = input()
lastSum = 0

for nxt in range(0, len(numberBinary)):
    if numberBinary[-nxt - 1] == '1':
        lastSum += pow(2, nxt)
allSum = lastSum + sumDecimal
print(allSum)
