def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # dp[i][j][k] = i番目までの式で、j番目の変数がkの場合の数
    dp = [[[0 for _ in range(2)] for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    dp[0][0][1] = 1
    for i in range(N):
        if S[i] == "AND":
            dp[i+1][0][0] = dp[i][0][0]
            dp[i+1][0][1] = dp[i][0][1]
            for j in range(1, N+1):
                dp[i+1][j][0] = dp[i][j][0] + dp[i][j-1][1]
                dp[i+1][j][1] = dp[i][j][1]
        else:
            dp[i+1][0][0] = dp[i][0][0]
            dp[i+1][0][1] = dp[i][0][1]
            for j in range(1, N+1):
                dp[i+1][j][0] = dp[i][j][0]
                dp[i+1][j][1] = dp[i][j][0] + dp[i][j-1][1]
    print(dp[N][N][1])
