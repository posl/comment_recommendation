def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0] * m
    for i in range(m):
        b[i] = c[i] - sum([a[j] * b[i - j - 1] for j in range(n)])
    print(' '.join(map(str, b)))
solve()
