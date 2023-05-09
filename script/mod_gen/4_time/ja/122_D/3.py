def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    dp[3][3][3] = 1
    for i in range(n):
        next = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2: continue
                        if k == 0 and j == 1 and m == 2: continue
                        if l == 0 and j == 1 and m == 2: continue
                        if k == 1 and l == 0 and m == 2: continue
                        if k == 0 and l == 2 and m == 1: continue
                        next[l][m][j] += dp[k][l][m]
                        next[l][m][j] %= mod
        dp = next
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()