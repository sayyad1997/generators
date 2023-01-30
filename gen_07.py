def gen(x):
    a,b=1,2

    for i in range(x):
        a,b=b,a+b
        yield a

c=gen(12)

for i in c:
    print(i)


def gen(x):
    a,b=1,2

    for i in range(x):
        a,b=b,a+b
        yield a
def square (x):
    for i in x:
        yield i**2

print(sum(square(gen(12))))