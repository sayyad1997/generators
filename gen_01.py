def gen():
    n=1
    yield n

    n+=1
    yield n

    n+=1
    yield n

x=gen()

print(next(x))
print(next(x))
print(next(x))
print(next(x))