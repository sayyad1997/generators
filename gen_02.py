def gen():
    n=1
    yield n

    n+=1
    yield n

for i in gen():
    print(i)