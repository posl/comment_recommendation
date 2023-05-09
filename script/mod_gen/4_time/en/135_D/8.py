def main():
    #input
    S = input()
    M = 10**9+7
    #compute
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
                    dp[i+1][(k*10+j)%13] %= M
        else:
            for k in range(13):
                dp[i+1][(k*10+int(S[i]))%13] += dp[i][k]
                dp[i+1][(k*10+int(S[i]))%13] %= M
    #output
    print(dp[-1][5])

if __name__ == '__main__':
    main()