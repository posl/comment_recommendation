def main():
    N = int(input())
    MOD = 10**9 + 7
    # dp[i][j][k][l] := i 文字目までで、j 文字目の直前の文字が k で、
    # j 文字目の直前の文字の直前の文字が l であるような文字列の数
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 0 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    for m in range(4):
                        dp[i + 1][m][j][k] += dp[i][j][k][l]
                        dp[i + 1][m][j][k] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)
