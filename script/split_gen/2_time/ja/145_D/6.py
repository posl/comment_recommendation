def main():
    # input
    X, Y = map(int, input().split())
    # compute
    MOD = 10**9+7
    dp = [[0]*(Y+1) for _ in range(X+1)]
    dp[0][0] = 1
    for i in range(X+1):
        for j in range(Y+1):
            if i == 0 and j == 0:
                continue
            if i-1 >= 0 and j-2 >= 0:
                dp[i][j] += dp[i-1][j-2]
            if i-2 >= 0 and j-1 >= 0:
                dp[i][j] += dp[i-2][j-1]
            dp[i][j] %= MOD
    # output
    print(dp[X][Y])
