def generator():
    f = open('input.txt', 'r')
    for i, line in enumerate(f):
        if 'error' in line:
            yield i

for x in generator():
    print(x)


class A:
    def _init_(self, n):
        self.n = n

    def m1(self, x):
        print(x)

obj = A(5)
obj.m1(123)
