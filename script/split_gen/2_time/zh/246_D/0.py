def solve(n):
    a = 0
    b = 0
    while True:
        if a**3 + a**2*b + a*b**2 + b**3 >= n:
            break
        b += 1
        if a**3 + a**2*b + a*b**2 + b**3 >= n:
            break
        a += 1
    return a**3 + a**2*b + a*b**2 + b**3
