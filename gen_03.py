def gen():
    x=(i for i in range(1,45))
    yield x

for y in gen():
    for z in y:
        print(z)