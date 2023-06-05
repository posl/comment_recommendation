def solve():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = 0
    for i in range(n):
        d = max(d, a[i] - a[i - 1])
    d = max(d, k - a[n - 1] + a[0])
    print(k - d)
