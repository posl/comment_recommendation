def solve():
    s = input()
    t = 'atcoder'
    dp = [[0 for _ in range(8)] for _ in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(8):
            if s[i] == t[j]:
                dp[i + 1][j] = dp[i][j] + 1
            else:
                dp[i + 1][j] = dp[i][j]
            if j > 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - 1])
    print(len(s) - dp[len(s)][7])

if __name__ == '__main__':
    solve()