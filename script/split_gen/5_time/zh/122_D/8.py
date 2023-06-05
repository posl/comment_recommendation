def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
    dp[3][3][3] = 1
    for i in range(n):
        temp = [[[0 for k in range(4)] for j in range(4)] for i in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if m == 0 and k == 1 and l == 2:
                            continue
                        if m == 1 and k == 0 and l == 2:
                            continue
                        if m == 0 and k == 2 and l == 1:
                            continue
                        if m == 0 and j == 1 and l == 2:
                            continue
                        if m == 0 and k == 1 and j == 2:
                            continue
                        temp[k][l][m] += dp[j][k][l]
                        temp[k][l][m] %= mod
        dp = temp
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)
