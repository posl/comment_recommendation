def burger(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    else:
        a = 2 ** (n + 2) - 3
        if x <= 1 + a // 2:
            return burger(n - 1, x - 1)
        else:
            return 2 ** (n + 1) - 1 + burger(n - 1, x - 2 - a // 2)
n, x = map(int, input().split())
print(burger(n, x))
