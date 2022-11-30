first = int(input())
second = int(input())
third = int(input())

if (first + second) > third and (second + third) > first and (third + first) > second:
    print('YES')
else:
    print('NO')