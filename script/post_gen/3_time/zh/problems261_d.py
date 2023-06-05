Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    # 读入数据
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for i in range(M)]
    # print(N, M)
    # print(X)
    # print(CY)

    # dp[i][j]表示第i次抛硬币，连续抛出j次正面时，可以得到的最大金额
    # dp[i][j] = max(dp[i-1][j-1]+X[i], dp[i-1][j])
    dp = [[0 for j in range(N+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = max(dp[i-1][j-1]+X[i-1], dp[i-1][j])

    # print(dp)

    # 计算最大金额
    ans = 0
    for i in range(1, M+1):
        C, Y = CY[i-1]
        for j in range(1, N+1):
            ans = max(ans, dp[j][C]+Y)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]
    CY.sort(key=lambda x: x[1], reverse=True)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 == CY[0][0]:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + CY[0][1])
            elif j + 1 > CY[0][0]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + CY[0][1])
    print(max(max(dp)))

=======
Suggestion 3

def main():
    # 读入数据
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    # print(N, M)
    # print(X)
    # print(C)
    # print(Y)

    # 初始化
    dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0

    # 动态规划
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            # 投掷硬币为正面，计数器加1
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i])
            # 投掷硬币为反面，计数器清零
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
    # print(dp)

    # 计算连胜奖金
    for i in range(N+1):
        for j in range(N+1):
            if dp[i][j] == -1:
                continue
            for k in range(M):
                if i+C[k] <= N:
                    dp[i+C[k]][j] = max(dp[i+C[k]][j], dp[i][j]+Y[k])
    # print(dp)

    # 计算最大金额
    ans = 0
    for i in range(N+1):
        for j in range(N+1):
            ans = max(ans, dp[i][j])
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_temp, y_temp = map(int, input().split())
        c.append(c_temp)
        y.append(y_temp)
    dp = [[-float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            for k in range(m):
                if j + 1 == c[k]:
                    dp[i + 1][0] = max(dp[i + 1][0], dp[i + 1][j + 1] + y[k])
    print(max(dp[n]))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_i, y_i = map(int, input().split())
        c.append(c_i)
        y.append(y_i)

    dp = [[0] * (n + 1) for _ in range(n + 1)] # dp[i][j]表示第i次投掷硬币后，连续j次正面朝上时的最大金额
    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1] + x[i])
            if j + 1 in c:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][j + 1] + y[c.index(j + 1)])
    print(max(dp[-1]))

=======
Suggestion 6

def solve():
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    c=[]
    y=[]
    for i in range(m):
        c_,y_=map(int,input().split())
        c.append(c_)
        y.append(y_)

    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m):
        for j in range(n+1):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])
            if j+c[i]<=n:
                dp[i+1][j+c[i]]=max(dp[i+1][j+c[i]],dp[i][j]+y[i])
    ans=0
    for i in range(n+1):
        ans=max(ans,dp[m][i]+x[i-1])
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c1,y1 = map(int,input().split())
        c.append(c1)
        y.append(y1)
    dp = [[-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] >= 0:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                if j+1 <= n:
                    dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + x[i])
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if dp[i][j] >= 0:
                for k in range(m):
                    if j >= c[k]:
                        dp[i][j-c[k]] = max(dp[i][j-c[k]],dp[i][j] + y[k])
                    ans = max(ans,dp[i][j])
    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)

    # 初始化
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    # 递推
    for i in range(1,n+1):
        dp[0][i] = dp[0][i-1] + x[i-1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if j >= c[i-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-c[i-1]]+y[i-1])

    # 输出
    print(dp[m][n])

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        c_i, y_i = map(int, input().split())
        c.append(c_i)
        y.append(y_i)

    dp = [[-float('inf')]*(n+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + x[i])
        for j in range(n):
            dp[i+1][0] = max(dp[i+1][0], dp[i][j] + y[j])
    print(max(dp[n]))

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    cy = []
    for i in range(m):
        c,y = map(int,input().split())
        cy.append([c,y])
    cy.sort()
    cy.reverse()
    ans = 0
    for i in range(n):
        ans += x[i]
        for j in range(m):
            if cy[j][0] <= i+1:
                ans = max(ans,ans+cy[j][1])
    print(ans)
