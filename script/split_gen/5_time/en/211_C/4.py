def main():
    S = input()
    MOD = 10 ** 9 + 7
    chokudai = 'chokudai'
    dp = [[0] * (len(chokudai) + 1) for _ in range(len(S) + 1)]
    for i in range(len(S) + 1):
        dp[i][0] = 1
    for i in range(1, len(S) + 1):
        for j in range(1, len(chokudai) + 1):
            if S[i - 1] != chokudai[j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
    print(dp[-1][-1])
