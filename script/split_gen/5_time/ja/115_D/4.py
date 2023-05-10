def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + burger(n - 1, x - 2):
        return burger(n - 1, x - 2)
    else:
        return 1 + burger(n - 1, x - 2 - burger(n - 1, x - 2))
n, x = map(int, input().split())
print(burger(n, x))
