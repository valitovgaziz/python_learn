import math

a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
    exit()
elif a== 0 and b == 0 and c != 0:
    print('No solution')
    exit()
D = math.pow(b, 2) - (4 * a * c)
if D > 0:
    x1 = round(((-b) - math.sqrt(D)) / (2 * a), 2)
    x2 = round(((-b) + math.sqrt(D)) / (2 * a), 2)
    x1 = '{:.2f}'.format(x1)
    x2 = '{:.2f}'.format(x2)
    if x1 > x2:
        print(f'{x1} {x2}')
    else:
        print(f'{x2} {x1}')
elif D == 0:
    x = round(-b / (2 * a), 2)
    x = '{:.2f}'.format(x)
    print(str(x))
else:
    print('No solution')
