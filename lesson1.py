s = int(input('enter time '))
h = s // 3600
x = s % 3600
m = x // 60
sec = x % 60
print(f'{h} {m} {sec}')