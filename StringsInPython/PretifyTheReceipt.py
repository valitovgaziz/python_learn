name = input()
cost = int(input())
weight = int(input())
money = int(input())
dd = 3
nameStr = 'Товар:' + ' ' * (35 - 6 - len(name)) + name
costInStr = f"{weight}кг * {cost}руб/кг"
costStr = 'Цена:' + ' ' * (35 - len(costInStr) - 5) + costInStr
totalInStr = f"{cost * weight}руб"
totalStr = 'Итого:' + ' ' * (35 - 6 - len(totalInStr)) + totalInStr
pushInStr = f"{money}руб"
pushStr = 'Внесено:' + ' ' * (35 - len(pushInStr) - 8) + pushInStr
changInStr = f"{money - cost * weight}руб"
changStr = 'Сдача:' + ' ' * (35 - 6 - len(changInStr)) + changInStr
print('{:=^35}'.format('Чек'))
print(nameStr)
print(costStr)
print(totalStr)
print(pushStr)
print(changStr)
print('=' * 35)
