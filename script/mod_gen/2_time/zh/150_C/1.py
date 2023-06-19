def solve(n, p, q):
    a, b = 0, 0
    for i in range(n):
        a = a * (n - i) + p[i] - 1
        b = b * (n - i) + q[i] - 1
    return abs(a - b)

if __name__ == '__main__':
    solve()