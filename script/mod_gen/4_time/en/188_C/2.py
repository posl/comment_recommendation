def solve(n, a):
    a = [0] + a
    for i in range(1, n + 1):
        a = [max(a[2 * j - 1], a[2 * j]) for j in range(1, 2 ** (n - i + 1) + 1)]
    return a[1]

if __name__ == '__main__':
    solve()