def main():
    S = input()
    target = "chokudai"
    mod = 10**9+7
    dp = [[0 for _ in range(len(target)+1)] for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(len(target)):
            if S[i] == target[j]:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % mod
            else:
                dp[i+1][j+1] = dp[i][j+1]
    print(dp[len(S)][len(target)])
