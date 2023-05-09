def main():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        if S[i] == "A" or S[i] == "?":
            dp[i][i][0] = 1
        if S[i] == "B" or S[i] == "?":
            dp[i][i][1] = 1
        if S[i] == "C" or S[i] == "?":
            dp[i][i][2] = 1
    for i in range(N):
        for j in range(i + 1, N):
            if S[j] == "A" or S[j] == "?":
                dp[i][j][0] = (dp[i][j - 1][0] + dp[i][j - 1][1] + dp[i][j - 1][2]) % mod
            if S[j] == "B" or S[j] == "?":
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1] + dp[i][j - 1][2]) % mod
            if S[j] == "C" or S[j] == "?":
                dp[i][j][2] = (dp[i][j - 1][0] + dp[i][j - 1][1] + dp[i][j - 1][2]) % mod
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += dp[i][j][2]
            ans %= mod
    print(ans)

if __name__ == '__main__':
    main()