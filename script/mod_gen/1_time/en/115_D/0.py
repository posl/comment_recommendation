def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + 2 ** (n - 1):
        return burger(n - 1, x - 1)
    else:
        return 2 ** n + burger(n - 1, x - 2 - 2 ** (n - 1))
n, x = map(int, input().split())
print(burger(n, x))
