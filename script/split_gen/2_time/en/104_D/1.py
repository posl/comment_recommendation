def main():
    S = input()
    N = len(S)
    MOD = 10 ** 9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if S[i] == '?':
                    for c in range(3):
                        dp[i + 1][j][c] += dp[i][j][k]
                        dp[i + 1][j][c] %= MOD
                else:
                    dp[i + 1][j][ord(S[i]) - ord('A')] += dp[i][j][k]
                    dp[i + 1][j][ord(S[i]) - ord('A')] %= MOD
        for j in range(4):
            for k in range(4):
                dp[i + 1][j][k] += dp[i][j][k]
                dp[i + 1][j][k] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)
