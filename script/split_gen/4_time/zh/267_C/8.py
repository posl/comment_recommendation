def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    res = -10**10
    for i in range(m, n+1):
        res = max(res, s[i] - s[i-m])
    print(res)
