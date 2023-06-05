def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # dp[i][j] 表示前i个物品中，总重量为j的情况下，总价值最大为多少
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j - a[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]] + b[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][w])

if __name__ == '__main__':
    main()