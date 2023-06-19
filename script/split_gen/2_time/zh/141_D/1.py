def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 ** (m - i))
    print(ans // (2 ** m))
