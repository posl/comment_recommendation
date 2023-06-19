def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dp[0][0][0] = 1
    for i in range(n):
        dp2 = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 1 and l == 2 and m == 3:
                            continue
                        if k == 2 and l == 1 and m == 3:
                            continue
                        if k == 1 and l == 3 and m == 2:
                            continue
                        if j == 1 and l == 2 and m == 3:
                            continue
                        if j == 1 and k == 2 and m == 3:
                            continue
                        dp2[k][l][m] += dp[j][k][l]
                        dp2[k][l][m] %= mod
        dp = dp2
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()