def solve(n):
    if n == 0:
        return 0
    a = 1
    while True:
        b = 1
        while True:
            x = a**3 + a**2*b + a*b**2 + b**3
            if x >= n:
                return x
            b += 1
        a += 1

if __name__ == '__main__':
    solve()