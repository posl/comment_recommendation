def burger(n, x):
    if n == 0:
        return 1
    elif x == 1:
        return 0
    elif x <= 1 + (2 ** (n + 1) - 3):
        return burger(n - 1, x - 1)
    else:
        return 2 ** n + burger(n - 1, x - 2 ** (n + 1) + 2)
print(burger(*map(int, input().split())))
