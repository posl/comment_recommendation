def solver(x, y):
    if x + y == 0:
        return 1
    elif x + y == 1:
        return 0
    else:
        if x > y:
            x, y = y, x
        return solver(x, y - 1) + solver(x - 1, y - 2)
x, y = map(int, input().split())
print(solver(x, y))
