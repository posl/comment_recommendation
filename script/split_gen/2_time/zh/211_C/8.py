def main():
    S = input()
    N = len(S)
    chokudai = "chokudai"
    M = len(chokudai)
    dp = [[0 for j in range(M+1)] for i in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1,N+1):
        for j in range(1,M+1):
            if S[i-1]==chokudai[j-1]:
                dp[i][j] = (dp[i-1][j]+dp[i-1][j-1])%1000000007
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][M])
