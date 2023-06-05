def main():
    n = int(input())
    a = [[0] * n for i in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    dp = [[0] * (1 << n) for i in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(1 << n):
            for k in range(n):
                if (j >> k & 1) == 0:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j | (1 << k)] + a[i][k])
    print(dp[0][0])

if __name__ == '__main__':
    main()