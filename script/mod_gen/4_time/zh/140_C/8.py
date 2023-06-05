def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n):
        a[i] = min(b[i-1], b[i])
    return sum(a)

if __name__ == '__main__':
    solve()