def solve():
    N = int(input())
    mod = 998244353
    ans = 0
    dp = [[0, 0, 0] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(10):
                if j == 0:
                    if k == 0:
                        dp[i + 1][0] += dp[i][0]
                    else:
                        dp[i + 1][1] += dp[i][0]
                elif j == 1:
                    if k == 0:
                        dp[i + 1][0] += dp[i][1]
                    elif k == 9:
                        dp[i + 1][2] += dp[i][1]
                    else:
                        dp[i + 1][1] += dp[i][1]
                elif j == 2:
                    if k == 9:
                        dp[i + 1][2] += dp[i][2]
                    else:
                        dp[i + 1][1] += dp[i][2]
                dp[i + 1][0] %= mod
                dp[i + 1][1] %= mod
                dp[i + 1][2] %= mod
    for i in range(3):
        ans += dp[N][i]
    print(ans % mod)
