def divisors(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d
