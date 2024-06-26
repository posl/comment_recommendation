def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for j in range(w + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(w + 1):
            if j >= b[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - b[i]] + a[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[n][w])
