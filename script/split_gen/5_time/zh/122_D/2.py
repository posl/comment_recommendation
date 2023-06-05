def main():
    N = int(input())
    mod = 10 ** 9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for _ in range(N):
        dp2 = [[[0] * 4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if (j == 0 and k == 1 and l == 2) or (j == 0 and k == 2 and l == 1) or (j == 1 and k == 0 and l == 2) or (i == 0 and k == 1 and l == 2) or (i == 0 and j == 1 and l == 2):
                            continue
                        dp2[j][k][l] += dp[i][j][k]
                        dp2[j][k][l] %= mod
        dp = dp2
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)
