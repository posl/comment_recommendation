def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    # 0 から n までの部分列について、それぞれの部分列の要素の総和の最小値を求める
    # dp[i][j] := 部分列 a[i:j] の要素の総和の最小値
    # dp[i][j] = min(dp[i][k] + dp[k][j]) (i <= k < j)
    dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 0
    for width in range(1, n + 1):
        for i in range(n + 1 - width):
            j = i + width
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp[i][j] += sum(a[i:j])
    # dp[i][j] を使って、部分列 a[0:n] の要素の総和の最小値を求める
    # dp[i][j] を使って、部分列 a[i:n] の要素の総和の最小値を求める
    # dp[i][j] を使って、部分列 a[0:j] の要素の総和の最小値を求める
    # dp[i][j] を使って、部分列 a[i:j] の要素の総和の最小値を求める
    ans = min(dp[0][n], dp[0][n] + l, dp[0][n] + r, dp[0][n] + l + r)
    for i in range(n):
        ans = min(ans, dp[0][i] + dp[i][n] + r)
    for i in range(n):
        ans = min(ans, dp[0][i] + dp[i][n] + l)
    for i in range
