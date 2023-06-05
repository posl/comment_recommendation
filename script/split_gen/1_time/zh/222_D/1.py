def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    # 用dp[i][j]表示长度为i，第i个数为j的方案数
    dp = [[0] * 3001 for i in range(n + 1)]
    for i in range(a[0], b[0] + 1):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(a[i - 1], b[i - 1] + 1):
            for k in range(j, b[i - 2] + 1):
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= mod
    print(sum(dp[n]) % mod)
solve()
