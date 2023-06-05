def f(n, x, y):
    if x > y:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return x
    return f(n-1, x, y) + (n-1) * f(n-2, x, y)
n, x, y = map(int, input().split())
print(f(n, x, y))
