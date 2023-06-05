def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    # dp[i][j][k] := 3文字目がi, 2文字目がj, 1文字目がkであるような文字列の個数
    # i, j, kはそれぞれ0 := 'A', 1 := 'C', 2 := 'G', 3 := 'T'を表す
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i == 0 and j == 1 and k == 2) or (i == 0 and j == 2 and k == 1) or (i == 1 and j == 0 and k == 2):
                    continue
                dp[i][j][k] = 1
    for _ in range(3, N):
        dp2 = [[[0] * 4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if (j == 0 and k == 1 and l == 2) or (j == 0 and k == 2 and l == 1) or (j == 1 and k == 0 and l == 2) or (i == 0 and k == 1 and l == 2) or (i == 0 and j == 1 and l == 2):
                            continue
                        dp2[j][k][l] += dp[i][j][k]
                        dp2[j][k][l] %= MOD
        dp = dp2
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= MOD
    print(ans)
