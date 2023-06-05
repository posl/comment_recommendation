def dp(n, m, q, w, v, x, query):
    dp = [[0 for i in range(100)] for j in range(100)]
    for i in range(n):
        for j in range(m):
            for k in range(100):
                if k - w[i] >= 0:
                    dp[i+1][j+1][k] = max(dp[i][j+1][k], dp[i][j][k-w[i]] + v[i])
                else:
                    dp[i+1][j+1][k] = dp[i][j+1][k]
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(100):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
    for i in range(q):
        ans = 0
        for j in range(query[i][0], query[i][1]+1):
            ans += x[j-1]
        print(dp[n][m][ans])
n, m, q = map(int, input().split())
w = [0 for i in range(n)]
v = [0 for i in range(n)]
x = [0 for i in range(m)]
for i in range(n):
    w[i], v[i] = map(int, input().split())
for i in range(m):
    x[i] = int(input())
query = [[0 for i in range(2)] for j in range(q)]
for i in range(q):
    query[i][0], query[i][1] = map(int, input().split())
dp(n, m, q, w, v, x, query)
