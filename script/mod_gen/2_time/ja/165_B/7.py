def getYear(x):
    y = 0
    a = 100
    while True:
        a = int(a * 1.01)
        y += 1
        if a >= x:
            return y
x = int(input())
print(getYear(x))
