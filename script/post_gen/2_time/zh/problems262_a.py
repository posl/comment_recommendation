Synthesizing 10/10 solutions (Duplicates hidden)

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

    #dp[i][j] 表示第i次投掷后，连续投掷j次且获得奖励的最大金额
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    #初始化
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0] + X[i-1]

    #状态转移
    for i in range(1, N+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1] + X[i-1], dp[i-1][j])
            if j in C:
                dp[i][0] = max(dp[i][0], dp[i][j] + Y[C.index(j)])

    print(max(dp[N]))

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    cy = []
    for i in range(m):
        cy.append(list(map(int,input().split())))
    cy.sort(key=lambda x:x[1],reverse=True)
    #print(cy)
    #print(x)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
            if x[i] == cy[0][0]:
                for k in range(m):
                    if j+1 == cy[k][0]:
                        dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j+1-cy[k][0]]+cy[k][1])
    print(dp[n][n])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C, Y = [], []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    ans = 0
    for i in range(N):
        ans += X[i]
        if i + 1 in C:
            ans += max(Y)
    print(ans)

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    CY = [list(map(int,input().split())) for _ in range(M)]
    CY.sort(key=lambda x:x[1],reverse=True)
    dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            for k in range(M):
                if j + CY[k][0] > N:
                    continue
                dp[i+CY[k][0]][j+CY[k][0]] = max(dp[i+CY[k][0]][j+CY[k][0]],dp[i][j]+CY[k][1])
    ans = 0
    for i in range(N+1):
        ans = max(ans,dp[N][i])
    print(ans)

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
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + x[i]
            else:
                dp[i + 1][j] = max(dp[i][j] + x[i], dp[i][j - 1])
    ans = 0
    for i in range(m):
        for j in range(n + 1):
            ans = max(ans, dp[c[i]][j] + y[i])
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]

    #dp[n][m]表示第n次投掷后，连续投掷m次的最大金额
    dp = [[0]*(M+1) for _ in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, M+1):
            c, y = CY[m-1]
            if n < c: dp[n][m] = dp[n][m-1]
            else:
                dp[n][m] = max(dp[n][m-1], dp[n-c][m-1] + y)
    #print(dp)
    ans = 0
    for n in range(N+1):
        ans = max(ans, dp[n][M] + sum(X[:n]))
    print(ans)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def problems261_d():
    pass

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_, y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    #print(n,m,x,c,y)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][j]+x[i])
    #print(dp)
    ans = 0
    for i in range(m):
        for j in range(n+1):
            ans = max(ans,dp[j][j-c[i]]+y[i])
    print(ans)
