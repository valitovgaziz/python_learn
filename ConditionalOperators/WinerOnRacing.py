Pety = int(input())
Vasy = int(input())
Toly = int(input())

if Pety > Vasy and Pety > Toly:
    if Vasy > Toly:
        print('1. Петя')
        print('2. Вася')
        print('3. Толя')
    else:
        print('1. Петя')
        print('2. Толя')
        print('3. Вася')
elif Vasy > Pety and Vasy > Toly:
    if Pety > Toly:
        print('1. Вася')
        print('2. Петя')
        print('3. Толя')
    else:
        print('1. Вася')
        print('2. Толя')
        print('3. Петя')
elif Toly > Pety and Toly > Vasy:
    if Pety > Vasy:
        print('1. Толя')
        print('2. Петя')
        print('3. Вася')
    else:
        print('1. Толя')
        print('2. Вася')
        print('3. Петя')