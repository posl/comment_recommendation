def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * f(n - 1)
print(f(10))
