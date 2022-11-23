N = int(input())
M = int(input())
time = int(input())
inHour = int(time / 60)
inMin = time - inHour * 60
hour = 0

if inHour > 24:
    inHour = inHour - int(inHour / 24) * 24

if (N + inHour) >= 24:
    hour = N + inHour - 24
else:
    hour = inHour + N

if (inMin + M) >= 60:
    minute = inMin + M - 60
    hour = hour + 1
else:
    minute = inMin + M

if hour == 24:
    hour = 0
result = f"{hour:02d}:{minute:02d}"
print(result)
