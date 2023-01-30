def sayyad(x):
    length=len(x)

    for i in range(length-1,-1,-1):
        yield x[i]

for y in sayyad("python learning is the easiest language"):
    print(y)