import math

a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0:
    print('Infinite solutions')
    exit()
D = math.pow(b, 2) - (4 * a * c)
if D > 0:
    x1 = ((-b) - math.sqrt(D)) / (2 * a)
    x2 = ((-b) + math.sqrt(D)) / (2 * a)
    x1 = '{:.2f}'.format(x1)
    x2 = '{:.2f}'.format(x2)
    print(f'{x1} {x2}')
elif D == 0:
    x = -b / (2 * a)
    x = '{:.2f}'.format(x)
    print(str(x))
else:
    print('No solution')
