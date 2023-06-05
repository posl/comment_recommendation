def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * (m + 1)
    for i in range(m + 1):
        b[i] = c[i] / a[n]
    for i in range(m, n - 1, -1):
        for j in range(n - i):
            b[j] -= a[j + i] * b[i]
    print(*b)
solve()
