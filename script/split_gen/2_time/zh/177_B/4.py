def solve(s, t):
    # 动态规划
    # dp[i][j]表示s的前i个字符和t的前j个字符的最小编辑距离
    # dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
    # dp[i][j] = dp[i-1][j-1] if s[i] == t[j] else dp[i-1][j-1]+1
    # dp[i][j] = dp[i-1][j-1] + 1 if s[i] != t[j] else dp[i-1][j-1]
    # dp[i][0] = i
    # dp[0][j] = j
    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(1, len(s)+1):
        dp[i][0] = i
    for j in range(1, len(t)+1):
        dp[0][j] = j
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # dp[i-1][j-1]+1 表示替换
                # dp[i-1][j]+1 表示删除
                # dp[i][j-1]+1 表示插入
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[len(s)][len(t)]
