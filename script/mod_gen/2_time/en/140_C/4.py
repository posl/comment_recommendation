def solve(n, b):
    a = [0] * n
    a[0] = b[0]
    a[-1] = b[-1]
    for i in range(1, n-1):
        a[i] = min(b[i], a[i-1])
    return sum(a)

if __name__ == '__main__':
    solve()