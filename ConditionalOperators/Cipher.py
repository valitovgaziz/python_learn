password = input()

digits = [0] * len(password)
for nextIndex in range(len(password)):
    digits[nextIndex] = int(password[nextIndex])

result = [digits[0] + digits[1], (digits[1] + digits[2])]
result.sort(reverse=True)
strResult = ''
for nextDigit in result:
    strResult = strResult + str(nextDigit)
print(strResult)
