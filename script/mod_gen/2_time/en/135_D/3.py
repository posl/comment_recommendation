def main():
    S = input()
    N = len(S)
    M = 10**9 + 7
    dp = [[0]*13 for _ in range(N+1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        if s == "?":
            for j in range(10):
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
                    dp[i+1][(k*10+j)%13] %= M
        else:
            for k in range(13):
                dp[i+1][(k*10+int(s))%13] += dp[i][k]
                dp[i+1][(k*10+int(s))%13] %= M
    print(dp[N][5])

if __name__ == '__main__':
    main()