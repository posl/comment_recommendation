def main():
    s = input()
    s_len = len(s)
    target = "chokudai"
    target_len = len(target)
    dp = [[0 for j in range(s_len+1)] for i in range(target_len+1)]
    for i in range(s_len+1):
        dp[0][i] = 1
    for i in range(1, target_len+1):
        for j in range(1, s_len+1):
            if target[i-1] == s[j-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % (10**9+7)
            else:
                dp[i][j] = dp[i][j-1]
    print(dp[target_len][s_len])
