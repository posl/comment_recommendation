def calc(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return (n // 2) * (n - 1)
    else:
        return n * ((n - 1) // 2)
