def f(n, m):
    if n < 0: return 0
    if n == 0: return 1
    return f(n - m, m) + f(n, m + 1)
print(f(int(input()), 1))
