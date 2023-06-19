def round_up(x, y):
    z = x
    for i in range(y):
        if z % 10 == 0:
            break
        z += 1
    return z
x, k = map(int, input().split())
print(round_up(x, k))
