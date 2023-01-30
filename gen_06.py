def ad(x):
    length=len(x)

    for i in range(length-1,-1,-1):
        yield x[i]

for char in ad("abcdefghijklmnopqrstuvwxyz"):
    print(char)
