def solve():
    s = input()
    t = "atcoder"
    dp = [[float('inf') for _ in range(len(t))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(len(t)):
            if i == 0 and j == 0:
                dp[i][j] = 0 if s[i] == t[j] else 1
            elif i == 0:
                dp[i][j] = dp[i][j-1] if s[i] == t[j] else dp[i][j-1] + 1
            elif j == 0:
                dp[i][j] = dp[i-1][j] if s[i] == t[j] else dp[i-1][j] + 1
            else:
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
    print(dp[-1][-1])
solve()
