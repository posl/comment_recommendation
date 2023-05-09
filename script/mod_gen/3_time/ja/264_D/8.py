def solve():
    S = input()
    T = "atcoder"
    INF = 10**18
    dp = [[INF] * (len(T) + 1) for _ in range(len(S) + 1)]
    for i in range(len(S) + 1):
        dp[i][0] = 0
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    print(dp[len(S)][len(T)])

if __name__ == '__main__':
    solve()