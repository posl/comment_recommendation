def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    ans = float("inf")
    for i in range(2, n-1):
        for j in range(i+1, n):
            p = s[i]
            q = s[j] - s[i]
            r = s[n] - s[j]
            max_ = max(p, q, r)
            min_ = min(p, q, r)
            ans = min(ans, max_ - min_)
    print(ans)
solve()
