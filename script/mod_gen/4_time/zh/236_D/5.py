def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    dp = [[0 for _ in range(1 << n)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(1 << n):
            if j & (1 << i):
                for k in range(i + 1, n):
                    if j & (1 << k):
                        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j ^ (1 << i) ^ (1 << k)] + a[i][k])
    print(dp[n][(1 << n) - 1])

if __name__ == '__main__':
    main()