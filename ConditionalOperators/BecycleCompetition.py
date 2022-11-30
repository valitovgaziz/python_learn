Pety = int(input())
Vasy = int(input())
Toly = int(input())
if Pety >= Vasy and Pety >= Toly:
    if Vasy >= Toly:
        a = "Петя"
        b = "Вася"
        c = "Толя"
    else:
        a = "Петя"
        b = "Толя"
        c = "Вася"
elif Vasy >= Pety and Vasy >= Toly:
    if Pety >= Toly:
        a = "Вася"
        b = "Петя"
        c = "Толя"
    else:
        a = "Вася"
        b = "Толя"
        c = "Петя"
elif Toly >= Pety and Toly >= Vasy:
    if Pety >= Vasy:
        a = "Толя"
        b = "Петя"
        c = "Вася"
    else:
        a = "Толя"
        b = "Вася"
        c = "Петя"

print(f'          {a}          ')
print(f'  {b}                  ')
print(f'                  {c}  ')
print(f'   II      I      III   ')