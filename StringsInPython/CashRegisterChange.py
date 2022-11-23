costInBinary = input()
money = int(input())
costInDecimal = 0
change = 0

for nxt in range(0, len(costInBinary)):
    if costInBinary[-nxt - 1] == '1':
        costInDecimal += pow(2, nxt)
change = money - costInDecimal
print(change)
