def solve(n):
    for a in range(1, 10**6):
        b = (n - a**3) / (a**2 + a) + 1
        if a**3 + a**2*b + a*b**2 + b**3 == n:
            return a**3 + a**2*b + a*b**2 + b**3
    return -1
