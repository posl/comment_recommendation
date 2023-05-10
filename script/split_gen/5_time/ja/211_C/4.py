def solve():
    S = input()
    chokudai = 'chokudai'
    dp = [[0] * (len(S) + 1) for _ in range(len(chokudai) + 1)]
    for i in range(len(S) + 1):
        dp[0][i] = 1
    for i in range(1, len(chokudai) + 1):
        for j in range(1, len(S) + 1):
            if chokudai[i - 1] == S[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]
    print(dp[len(chokudai)][len(S)] % (10 ** 9 + 7))
solve()
