number = input()
arrayOfNumber = []

twase = number.replace(number[0], "", 1).lstrip('0')
if len(twase) == 2:
    arrayOfNumber.append(int(twase))

twase = number.replace(number[0], "", 1)[::-1].lstrip('0')
if len(twase) == 2:
    arrayOfNumber.append(int(twase))

twase = number.replace(number[1], "", 1).lstrip('0')
if len(twase) == 2:
    arrayOfNumber.append(int(twase))

twase = number.replace(number[1], "", 1)[::-1].lstrip('0')
if len(twase) == 2:
    arrayOfNumber.append(int(twase))

twase = number.replace(number[2], "", 1).lstrip('0')
if len(twase) == 2:
    arrayOfNumber.append(int(twase))

twase = number.replace(number[2], "", 1)[::-1].lstrip('0')
if len(twase) == 2:
    arrayOfNumber.append(int(twase))

arrayOfNumber.sort()
print(arrayOfNumber)
print(f'{arrayOfNumber[0]} {arrayOfNumber[len(arrayOfNumber) - 1]}')
