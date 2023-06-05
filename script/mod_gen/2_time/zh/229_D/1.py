def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #dp[i][w]表示前i个物品中总重量不超过w时的最大价值
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= B[i]:
                dp[i+1][w] = max(dp[i][w], dp[i+1][w-B[i]]+A[i])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

if __name__ == '__main__':
    main()