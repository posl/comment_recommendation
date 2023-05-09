def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if S[i] == "?":
                    for l in range(3):
                        dp[i+1][j][k] += dp[i][j][k]
                        dp[i+1][j][k] %= MOD
                        dp[i+1][l][j] += dp[i][j][k]
                        dp[i+1][l][j] %= MOD
                else:
                    dp[i+1][j][k] += dp[i][j][k]
                    dp[i+1][j][k] %= MOD
                    dp[i+1][ord(S[i])-ord("A")][j] += dp[i][j][k]
                    dp[i+1][ord(S[i])-ord("A")][j] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)
