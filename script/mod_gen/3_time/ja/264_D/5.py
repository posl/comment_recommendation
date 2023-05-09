def solve():
    s = input()
    atcoder = "atcoder"
    dp = [[0 for _ in range(8)] for _ in range(len(s))]
    dp[0][0] = 1 if s[0] == "a" else 0
    for i in range(1, len(s)):
        dp[i][0] = dp[i - 1][0] + 1 if s[i] == "a" else dp[i - 1][0]
    for i in range(1, len(s)):
        for j in range(1, 8):
            if s[i] == atcoder[j]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[-1][-1] % (10 ** 9 + 7))

if __name__ == '__main__':
    solve()