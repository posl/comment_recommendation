def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - i - 1
    b.sort()
    return b[n // 2] + sum(abs(b[i] - b[n // 2]) for i in range(n))

if __name__ == '__main__':
    solve()