def generator(num):
    print('start')
    while num>0:
        yield num
        num-=1

val=generator(10)
print(next(val))
print(next(val))
print(next(val))
print(next(val))
for x in val:
    print(x)
