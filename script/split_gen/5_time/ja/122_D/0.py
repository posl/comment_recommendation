def main():
    N = int(input())
    dp = [[[0 for i in range(4)] for j in range(4)] for k in range(4)]
    dp[3][2][1] = 1
    for n in range(N-3):
        dp_new = [[[0 for i in range(4)] for j in range(4)] for k in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 2 and k == 1 and l == 3:
                            continue
                        if j == 1 and k == 2 and l == 3:
                            continue
                        if j == 2 and k == 3 and l == 1:
                            continue
                        if i == 2 and k == 1 and l == 3:
                            continue
                        if i == 2 and j == 1 and l == 3:
                            continue
                        dp_new[j][k][l] += dp[i][j][k]
                        dp_new[j][k][l] %= 1000000007
        dp = dp_new
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= 1000000007
    print(ans)
