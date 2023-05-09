def solve(n):
    a = 0
    while a*a*a <= n:
        b = 0
        while a*a*a + a*a*b + a*b*b + b*b*b <= n:
            if a*a*a + a*a*b + a*b*b + b*b*b == n:
                return n
            b += 1
        a += 1
    return a*a*a + a*a*b + a*b*b + b*b*b
