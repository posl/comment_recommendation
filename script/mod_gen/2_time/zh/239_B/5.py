def floor(x):
    if x >= 0:
        return x // 10
    else:
        return -((-x + 9) // 10)
x = int(input())
print(floor(x))
