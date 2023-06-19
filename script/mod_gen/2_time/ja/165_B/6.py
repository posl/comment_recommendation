def calcYear(x):
    y = 0
    z = 100
    while z < x:
        z += z // 100
        y += 1
    return y
x = int(input())
print(calcYear(x))
