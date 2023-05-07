def main():
    N = int(input())
    dp = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 2:
                continue
            if i == 0 and j == 3:
                continue
            if i == 1 and j == 0:
                continue
            if i == 1 and j == 3:
                continue
            if i == 2 and j == 1:
                continue
            dp[i][j] = 1
    for _ in range(N - 1):
        ndp = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == 0 and j == 2 and k == 1:
                        continue
                    if i == 0 and j == 2 and k == 3:
                        continue
                    if i == 0 and j == 3 and k == 1:
                        continue
                    if i == 1 and j == 0 and k == 2:
                        continue
                    if i == 1 and j == 3 and k == 2:
                        continue
                    if i == 2 and j == 1 and k == 0:
                        continue
                    ndp[j][k] += dp[i][j]
        dp = ndp
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[i][j]
    print(ans % (10**9 + 7))

if __name__ == '__main__':
    main()