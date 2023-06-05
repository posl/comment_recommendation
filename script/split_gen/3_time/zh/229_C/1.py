def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #dp[i][j] i:第i种奶酪 j:总重量  dp[i][j] = max(dp[i-1][j], dp[i-1][j-b[i]]+a[i])
    dp = [[0]*(w+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j < b[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-b[i-1]]+a[i-1], dp[i-1][j])
    print(dp[n][w])
