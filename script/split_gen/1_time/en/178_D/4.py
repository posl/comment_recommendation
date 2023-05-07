def main():
    S = int(input())
    dp = [[0 for _ in range(S+1)] for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(1,S+1):
        for j in range(1,S+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % (10**9+7)
    print(dp[S][S])
