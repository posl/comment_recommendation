def solve():
    # S = int(input())
    S = 1729
    mod = 10**9 + 7
    dp = [[0]*(S+1) for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(S+1):
        for j in range(S+1):
            for k in range(3, S-i-j+1):
                dp[i+k][j] += dp[i][j]
                dp[i+k][j] %= mod
            for k in range(3, S-i-j+1):
                dp[i][j+k] += dp[i][j]
                dp[i][j+k] %= mod
    print(dp[S][S])

if __name__ == '__main__':
    solve()