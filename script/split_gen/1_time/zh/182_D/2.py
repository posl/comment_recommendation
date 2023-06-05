def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    minx = 0
    ans = 0
    for i in range(1, n+1):
        ans = max(ans, s[i] - minx)
        minx = min(minx, s[i])
    print(ans)
solve()
