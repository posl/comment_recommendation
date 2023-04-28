Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)

    dp = [[-1 for i in range(N+1)] for j in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            for k in range(M):
                if C[k] == j+1:
                    dp[i+1][C[k]] = max(dp[i+1][C[k]], dp[i][j] + Y[k])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i])

    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[N][i])
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i + 1])
        for j in range(m):
            if i + 1 >= c[j]:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - c[j]] + y[j])
        dp[i + 1] += x[i]
    print(dp[n])

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    ans = 0
    for i in range(n):
        ans += x[i]
    for i in range(m):
        min = 10**9
        for j in range(n):
            if c[i] <= j + 1:
                if min > x[j] - y[i] * (j + 1 - c[i]):
                    min = x[j] - y[i] * (j + 1 - c[i])
        if min > 0:
            ans -= min
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = []
    C = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i])
            for k in range(M):
                if j+1 == C[k]:
                    dp[i+1][1] = max(dp[i+1][1], dp[i][j] + Y[k])
    print(max(dp[-1]))

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for _ in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)

    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
            if j+1 in C:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j]+Y[C.index(j+1)])

    print(max(dp[N]))

main()

=======
Suggestion 6

def main():
    #N M
    #X_1 X_2 ... X_N
    #C_1 Y_1
    #C_2 Y_2
    #.
    #.
    #.
    #C_M Y_M
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = []
    for i in range(M):
        CY.append(list(map(int, input().split())))
    #print(N, M)
    #print(X)
    #print(CY)
    #N, M = 6, 3
    #X = [2, 7, 1, 8, 2, 8]
    #CY = [[2, 10], [3, 1], [5, 5]]

    #dp[i][j] i番目までのコインでj回まで連続して表が出ている状態で得られる最大の金額
    #dp[i][j] = max(dp[i-1][j+1], dp[i-1][j]) + X[i]
    #dp[i][j] = max(dp[i-1][j+1], dp[i-1][j]) + Y[i]
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j]) + X[i]

    for i in range(N):
        for j in range(N):
            if i+1 == CY[j][0]:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j] + CY[j][1])

    #print(dp)
    print(max(dp[N]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        a, b = map(int, input().split())
        c.append(a)
        y.append(b)
    dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            if j + 1 in c:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][j] + y[c.index(j + 1)])
    print(max(dp[n]))

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        c_, y_ = map(int, input().split())
        c.append(c_)
        y.append(y_)
    dp = [[-10**18]*(n+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + x[i])
            for k in range(m):
                if j+1 == c[k]:
                    dp[i+1][0] = max(dp[i+1][0], dp[i][j] + y[k])
    print(max(dp[-1]))

=======
Suggestion 9

def solve():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0]*m
    y = [0]*m
    for i in range(m):
        c[i],y[i] = map(int, input().split())
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = max(dp[i+1], dp[i]+x[i])
        for j in range(m):
            if i+1 >= c[j]:
                dp[i+1] = max(dp[i+1], dp[i+1-c[j]]+y[j])
    print(dp[n])

=======
Suggestion 10

def solve():
    n, m = map(int, input().split())
    x = [int(i) for i in input().split()]
    c = [0] * n
    y = [0] * n
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    c = c[:m]
    y = y[:m]
    ans = 0
    for i in range(n):
        ans += x[i]
    for i in range(n - 1):
        if c[i] == c[i + 1]:
            y[i + 1] = 0
    for i in range(n):
        ans += y[i]
    print(ans)
