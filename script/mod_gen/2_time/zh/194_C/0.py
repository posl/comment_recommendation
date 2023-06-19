def solve(n, a):
    s = 0
    for i in range(1, n):
        s += (a[i] - a[i-1]) * (a[i] - a[i-1]) * (n - i) * i
    return s

if __name__ == '__main__':
    solve()