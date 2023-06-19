def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x + y
    else:
        return calc(n-1, x, y) + calc(n-2, x, y) + x
n, x, y = map(int, input().split())
print(calc(n, x, y))
