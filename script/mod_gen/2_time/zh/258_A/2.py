def solve():
    n = int(input())
    x = []
    y = []
    p = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        p.append(c)
    INF = 10 ** 9
    # dp[i][j]表示第i个蹦床训练j次能访问的蹦床
    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = INF
            else:
                if p[i] * j >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                    dp[i][j] = 1
    # floyd
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    res = INF
    for i in range(n):
        res = min(res, max(dp[i]))
    print(res + 1)
solve()
