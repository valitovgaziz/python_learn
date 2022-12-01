n = int(input("Введите число: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 3 == 1:
            print("* ", end="")
        elif j % 3 == 2:
            print("# ", end="")
        else:
            print("@ ", end="")
    print("")