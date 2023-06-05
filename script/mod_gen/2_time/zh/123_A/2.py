def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 1 and j == 0 and k == 2:
                    continue
                dp[i][j][k] = 1
    for _ in range(n-3):
        dp2 = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 0 and k == 1 and l == 2:
                            continue
                        if j == 0 and k == 2 and l == 1:
                            continue
                        if i == 0 and k == 1 and l == 2:
                            continue
                        if i == 0 and j == 1 and l == 2:
                            continue
                        if i == 0 and j == 1 and k == 2:
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

if __name__ == '__main__':
    main()