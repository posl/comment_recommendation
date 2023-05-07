def solve(n, a, b):
    if n <= (a + b):
        return min(a, n)
    else:
        return a + (n - (a + b)) * (a - b)

if __name__ == '__main__':
    solve()