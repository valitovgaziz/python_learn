first = input()
second = input()
ciphers = [int(first[0]), int(first[1]), int(second[0]), int(second[1])]
ciphers.sort()
result = str(ciphers[3]) + str(ciphers[1] + ciphers[2])[-1] + str(ciphers[0])
print(result)