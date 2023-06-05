def solve(n, c):
    # i番目以前有几个W
    w = [0] * (n + 1)
    for i in range(n):
        w[i + 1] = w[i] + (1 if c[i] == 'W' else 0)
    # i番目以后有几个R
    r = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        r[i] = r[i + 1] + (1 if c[i] == 'R' else 0)
    return max(w[i] + r[i] for i in range(n + 1))

if __name__ == '__main__':
    solve()