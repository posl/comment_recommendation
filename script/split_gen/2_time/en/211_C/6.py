def main():
    MOD = 10**9 + 7
    S = input()
    n = len(S)
    dp = [[0]*(n+1) for _ in range(9)]
    for i in range(9):
        dp[i][0] = 1
    for i in range(n):
        for j in range(9):
            if S[i] == "chokudai"[j]:
                dp[j][i+1] = dp[j][i] + dp[j-1][i]
            else:
                dp[j][i+1] = dp[j][i]
    print(dp[-1][-1] % MOD)
main()
