Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + x[i]
        dp[i + 1][1] = max(dp[i][0], dp[i][1]) + x[i]
        for j in range(2, i + 2):
            dp[i + 1][j] = max(dp[i][j - 1] + x[i], dp[i][j])
    ans = 0
    for i in range(m):
        for j in range(1, n + 1):
            ans = max(ans, dp[n][j] + (n - j) // c[i] * y[i])
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
    ans = 0
    for i in range(n):
        ans += x[i]
    for i in range(m):
        for j in range(n - c[i] + 1):
            tmp = 0
            for k in range(c[i]):
                tmp += x[j + k]
            ans = max(ans, tmp + y[i])
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i][0] = X[i]

    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
            for k in range(M):
                if j + 1 == C[k]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + Y[k])

    print(max(dp[N]))

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for _ in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)
    
    #dp[i][j] i番目までのコインでj回表が出た時の最大金額
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(N+1):
            if j == 0:
                dp[i+1][j] = max(dp[i][j],dp[i+1][j])
            else:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j-1]+X[i])
            for k in range(M):
                if C[k] == j:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][0]+Y[k])
    print(max(dp[N]))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    # print(n, m)
    # print(x)
    # print(c)
    # print(y)
    ans = 0
    for i in range(n):
        ans += x[i]
        for j in range(m):
            if i+1 == c[j]:
                ans += y[j]
    print(ans)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = []
    C = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    #print(N, M, X, Y, C)

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            #print(i, j, dp[i][j])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            for k in range(M):
                if i + C[k] > N:
                    continue
                dp[i + C[k]][j + 1] = max(dp[i + C[k]][j + 1], dp[i][j] + Y[k])
    #print(dp)
    print(max(dp[N]))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_i, y_i = map(int, input().split())
        c.append(c_i)
        y.append(y_i)
    dp = [[-float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 <= n:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            if j in c:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + y[c.index(j)])
    print(max(dp[n]))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)

    dp = [[-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            #表が出た場合
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+x[i])
            #裏が出た場合
            dp[i+1][0] = max(dp[i+1][0],dp[i][j])
            #ボーナスの処理
            for k in range(m):
                if j+1 == c[k]:
                    dp[i+1][0] = max(dp[i+1][0],dp[i][j]+y[k])

    ans = 0
    for i in range(n+1):
        ans = max(ans,dp[n][i])
    print(ans)

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]

    # dp[i] := i回目のコイントスまでの最大の金額
    dp = [0] * (N + 1)
    # dp[i] = max(dp[i], dp[i - 1] + X[i - 1])
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + X[i - 1]
    # dp[i] = max(dp[i], dp[i - C] + Y)
    for C, Y in CY:
        for i in range(C, N + 1):
            dp[i] = max(dp[i], dp[i - C] + Y)

    return dp[N]

print(solve())

=======
Suggestion 10

def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    dp = [[-1]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+X[i])
            for k in range(M):
                if j+1 == XY[k][0]:
                    dp[i+1][0] = max(dp[i+1][0],dp[i][j]+XY[k][1])
    ans = 0
    for i in range(N+1):
        ans = max(ans,dp[N][i])
    print(ans)
