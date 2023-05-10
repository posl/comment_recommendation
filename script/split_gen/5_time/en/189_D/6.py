def main():
    N = int(input())
    S = [input() for i in range(N)]
    #print(N)
    #print(S)
    dp = [[0 for j in range(2)] for i in range(N+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(N):
        if S[i] == 'AND':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][0] + 2 * dp[i][1]
        else:
            dp[i+1][0] = 2 * dp[i][0] + dp[i][1]
            dp[i+1][1] = dp[i][1]
    print(dp[N][1])
