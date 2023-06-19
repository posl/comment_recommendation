def solve(n, a, b, s):
    if n % 2 == 0:
        if a < b:
            return (a * n) // 2
        else:
            return b * n
    else:
        if a < b:
            return a + (a * (n - 1)) // 2
        else:
            return b + b * (n - 1)
