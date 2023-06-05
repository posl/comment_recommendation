def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(a[i], b[i] + 1):
            for k in range(j, b[i - 1] + 1):
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= mod
    ans = 0
    for i in range(a[-1], b[-1] + 1):
        ans += dp[-1][i]
        ans %= mod
    print(ans)
solve()
