name = input()
cost = int(input())
weight = int(input())
money = int(input())

print(f'''
Чек
{name} - {weight}кг - {cost}руб/кг
Итого: {cost * weight}руб
Внесено: {money}руб
Сдача: {money - (cost * weight)}руб''')
