number = input()
cipherArray = [len(number)]
minCipher = int(number[0])
maxCipher = int(number[0])
for nextIndex in range(len(number)):
    nextNumber = int(number[nextIndex])
    if minCipher > nextNumber:
        minCipher = nextNumber
    if maxCipher < nextNumber:
        maxCipher = nextNumber
number = number.replace(str(minCipher), '', 1)
number = number.replace(str(maxCipher), '', 1)
if (maxCipher + minCipher) == int(number[0]) * 2:
    print("YES")
else:
    print("NO")
