def main():
    S = int(input())
    if S < 3:
        print(0)
    else:
        mod = 10**9 + 7
        dp = [[0 for i in range(S+1)] for j in range(S+1)]
        dp[3][3] = 1
        for i in range(4, S+1):
            for j in range(3, S+1):
                dp[i][j] = (dp[i][j-1] + dp[i-j][j]) % mod
        print(dp[S][S])
