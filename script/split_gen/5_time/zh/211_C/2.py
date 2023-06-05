def main():
    s = input()
    mod = 10**9+7
    chokudai = "chokudai"
    dp = [[0 for _ in range(len(chokudai)+1)] for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(len(chokudai)+1):
            dp[i+1][j] += dp[i][j]
            if j < len(chokudai) and s[i] == chokudai[j]:
                dp[i+1][j+1] += dp[i][j]
    print(dp[len(s)][len(chokudai)]%mod)
