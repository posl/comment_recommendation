def f(n, a, b):
    x = n // a
    y = n // b
    z = n // (a * b)
    return n * (n + 1) // 2 - x * (x + 1) // 2 * a - y * (y + 1) // 2 * b + z * (z + 1) // 2 * a * b
