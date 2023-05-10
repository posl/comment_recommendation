def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(N)
    #print(S)
    #dp[i][j] = i番目までの論理式に対するjの値の数
    dp = [[0 for i in range(2)] for j in range(N+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(N):
        if S[i] == 'AND':
            dp[i+1][0] += dp[i][0] * 2 + dp[i][1]
            dp[i+1][1] += dp[i][1]
        else:
            dp[i+1][0] += dp[i][0]
            dp[i+1][1] += dp[i][1] * 2 + dp[i][0]
    #print(dp)
    print(dp[N][1])
