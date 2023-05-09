def main():
    mod = 10 ** 9 + 7
    n = int(input())
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 1 and k == 0 and l == 2:
                        continue
                    if j == 1 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 2 and k == 1 and l == 0:
                        continue
                    dp[i + 1][k] += dp[i][j]
                    dp[i + 1][k] %= mod
    print(sum(dp[n]) % mod)
