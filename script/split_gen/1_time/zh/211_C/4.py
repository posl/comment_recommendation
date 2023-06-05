def main():
    s = input()
    chokudai = "chokudai"
    mod = 10 ** 9 + 7
    dp = [0] * 9
    dp[0] = 1
    for i in range(len(s)):
        for j in range(8, -1, -1):
            if s[i] == chokudai[j]:
                dp[j + 1] += dp[j]
                dp[j + 1] %= mod
    print(dp[8])
