first = input()
second = input()
third = input()

if first < second and first < third:
    print(first)
elif second < first and second < third:
    print(second)
else:
    print(third)