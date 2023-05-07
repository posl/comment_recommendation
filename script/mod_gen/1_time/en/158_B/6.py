def solve(n, a, b):
    if a == 0:
        return 0
    elif b == 0:
        return n
    else:
        return (n // (a + b)) * a + min(a, n % (a + b))

if __name__ == '__main__':
    solve()