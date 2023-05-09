def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 0: 0, 1: -, 2: +
    dp = [[0] * 3 for _ in range(n)]
    # 0: 0
    dp[0][0] = a[0]
    # 1: -
    dp[0][1] = -a[0]
    # 2: +
    dp[0][2] = a[0]
    for i in range(1, n):
        # 0: 0
        dp[i][0] = max(dp[i-1][0] + a[i], dp[i-1][1] + a[i], dp[i-1][2] + a[i])
        # 1: -
        dp[i][1] = max(dp[i-1][0] - a[i], dp[i-1][1] - a[i], dp[i-1][2] - a[i])
        # 2: +
        dp[i][2] = max(dp[i-1][0] + a[i], dp[i-1][1] + a[i], dp[i-1][2] + a[i])
    print(max(dp[-1]))

if __name__ == '__main__':
    main()