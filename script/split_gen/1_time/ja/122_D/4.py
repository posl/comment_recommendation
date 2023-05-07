def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[0]*4 for _ in range(4)] for _ in range(n+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i == 0 and j == 2 and k == 1) or (i == 0 and j == 1 and k == 2):
                    continue
                if (i == 0 and j == 2 and k == 0) or (i == 0 and j == 0 and k == 2):
                    continue
                if (i == 0 and j == 1 and k == 0) or (i == 0 and j == 0 and k == 1):
                    continue
                if (i == 1 and j == 0 and k == 2) or (i == 2 and j == 0 and k == 1):
                    continue
                dp[3][i][j] += 1
    for i in range(4,n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j == 0 and k == 2 and l == 1) or (j == 0 and k == 1 and l == 2):
                        continue
                    if (j == 0 and k == 2 and l == 0) or (j == 0 and k == 0 and l == 2):
                        continue
                    if (j == 0 and k == 1 and l == 0) or (j == 0 and k == 0 and l == 1):
                        continue
                    if (j == 1 and k == 0 and l == 2) or (j == 2 and k == 0 and l == 1):
                        continue
                    dp[i+1][k][l] += dp[i][j][k]
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[n][i][j]
    print(ans%mod)
