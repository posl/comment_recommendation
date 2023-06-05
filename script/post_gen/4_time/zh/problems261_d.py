Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    cy = [list(map(int, input().split())) for _ in range(m)]
    c = [i[0] for i in cy]
    y = [i[1] for i in cy]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 in c:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][j] + y[c.index(j + 1)])
    print(max(dp[n]))

=======
Suggestion 2

def coin(n,m,X,C,Y):
    #n次抛硬币，m种连胜奖金
    #X为n次抛硬币的结果
    #C为连胜奖金的条件
    #Y为连胜奖金的金额
    #X=[2,7,1,8,2,8]
    #C=[2,3,5]
    #Y=[10,1,5]
    #n=6
    #m=3
    #print(X)
    #print(C)
    #print(Y)
    #print(n,m)
    X=[int(i) for i in X]
    C=[int(i) for i in C]
    Y=[int(i) for i in Y]
    #print(X)
    #print(C)
    #print(Y)
    #print(n,m)
    #print(X[0])
    #print(C[0])
    #print(Y[0])
    #print(X[1])
    #print(C[1])
    #print(Y[1])
    #print(X[2])
    #print(C[2])
    #print(Y[2])
    #print(n,m)
    #print(X)
    #print(C)
    #print(Y)
    #print(n,m)
    #print(X[0])
    #print(C[0])
    #print(Y[0])
    #print(X[1])
    #print(C[1])
    #print(Y[1])
    #print(X[2])
    #print(C[2])
    #print(Y[2])
    #print(n,m)
    #print(X)
    #print(C)
    #print(Y)
    #print(n,m)
    #print(X[0])
    #print(C[0])
    #print(Y[0])
    #print(X[1])
    #print(C[1])
    #print(Y[1])
    #print(X[2])
    #print(C[2])
    #print(Y[2])
    #print(n,m)
    #print(X)
    #print(C)
    #print(Y)
    #print(n,m)
    #print(X[0])
    #print(C[0])
    #print(Y[0])
    #print(X[1])
    #print(C[1])
    #print(Y

=======
Suggestion 3

def main():
    n,m = list(map(int,input().split()))
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_i, y_i = list(map(int,input().split()))
        c.append(c_i)
        y.append(y_i)
    #print(n,m,x,c,y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,n+1):
        dp[0][i] = dp[0][i-1] + x[i-1]
    #print(dp)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if j < c[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-c[i-1]]+y[i-1])
    #print(dp)
    print(dp[-1][-1])

=======
Suggestion 4

def solve():
    N,M=map(int,input().split())
    X=list(map(int,input().split()))
    YC=[list(map(int,input().split())) for _ in range(M)]
    YC.sort(key=lambda x:x[0])
    YC.sort(key=lambda x:x[1],reverse=True)
    dp=[0]*(N+1)
    for i in range(N):
        dp[i+1]=max(dp[i+1],dp[i])
        for j in range(M):
            if i+YC[j][0]<=N:
                dp[i+YC[j][0]]=max(dp[i+YC[j][0]],dp[i]+X[i])
    print(max(dp))

solve()

=======
Suggestion 5

def main():
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    c,y=[],[]
    for i in range(m):
        c_,y_=map(int,input().split())
        c.append(c_)
        y.append(y_)
    # print(n,m,x,c,y)
    # print(len(x),len(c),len(y))
    # print(x)
    # print(c)
    # print(y)
    # print(len(x))
    # print(len(c))
    # print(len(y))
    # print(len(x))
    # print(len(c))
    # print(len(y))
    # print(x[0:3])
    # print(x[3:6])
    # print(x[0:2])
    # print(x[2:3])
    # print(x[3:5])
    # print(x[5:6])
    # print(x[0:1])
    # print(x[1:1])
    # print(x[2:2])
    # print(x[3:3])
    # print(x[4:4])
    # print(x[5:5])
    # print(x[6:6])
    # print(x[0:0])
    # print(x[1:0])
    # print(x[2:0])
    # print(x[3:0])
    # print(x[4:0])
    # print(x[5:0])
    # print(x[6:0])
    # print(x[0:1])
    # print(x[1:2])
    # print(x[2:3])
    # print(x[3:4])
    # print(x[4:5])
    # print(x[5:6])
    # print(x[6:7])
    # print(x[0:2])
    # print(x[2:3])
    # print(x[3:5])
    # print(x[5:6])
    # print(x[0:3])
    # print(x[3:6])
    # print(x[0:1])
    # print(x[1:1])
    # print(x[2:2])
    # print(x[3:3])
    # print(x[4:4])
    # print(x[5:5])
    # print(x[6:6])
    # print(x[0:0])
    # print(x

=======
Suggestion 6

def solve():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for _ in range(m):
        a,b = map(int,input().split())
        c.append(a)
        y.append(b)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i][i] = x[i]
    for i in range(n):
        for j in range(i+1,n):
            dp[i][j] = dp[i][j-1] + x[j]
    dp2 = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp2[i][i] = x[i]
    for i in range(n):
        for j in range(i+1,n):
            dp2[i][j] = max(dp2[i][j-1],dp[i][j])
    ans = 0
    for i in range(1,n+1):
        for j in range(m):
            if i < c[j]:
                continue
            ans = max(ans,dp2[i-c[j]][i-1]+y[j])
    print(ans)
solve()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for _ in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = dp[i][0] + x[i]
    for i in range(n):
        for j in range(1, n + 1):
            if j <= i + 1:
                dp[i + 1][j] = max(dp[i][j - 1] + y[j - 1], dp[i][j] + x[i])
            else:
                dp[i + 1][j] = dp[i][j] + x[i]
    ans = 0
    for i in range(n + 1):
        ans = max(ans, dp[n][i])
    print(ans)

=======
Suggestion 8

def getmaxmoney(N,M,X,C,Y):
    maxmoney = 0
    for i in range(N):
        if X[i] == 1:
            money = Y[0]
        else:
            money = 0
        if i == 0:
            maxmoney = money
            continue
        if i == N-1:
            if X[i] == 1:
                if C[i] == 1:
                    money = money + Y[C[i]-1]
                else:
                    money = money + Y[C[i]-1] + Y[C[i]-2]
            else:
                if C[i] == 1:
                    money = 0
                else:
                    money = money + Y[C[i]-2]
            maxmoney = max(maxmoney,money)
            continue
        if X[i] == 1:
            if C[i] == 1:
                money = money + Y[C[i]-1]
            else:
                money = money + Y[C[i]-1] + Y[C[i]-2]
        else:
            if C[i] == 1:
                money = 0
            else:
                money = money + Y[C[i]-2]
        maxmoney = max(maxmoney,money)
    return maxmoney

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    C = []
    Y = []
    for i in range(M):
        c,y = map(int,input().split())
        C.append(c)
        Y.append(y)
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,i+1):
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+X[i-1])
            for k in range(M):
                if j == C[k]:
                    dp[i][j] = max(dp[i][j],dp[i-C[k]][j-C[k]]+Y[k])
    print(max(dp[N]))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    x = [int(x) for x in input().split()]
    c = []
    y = []
    for i in range(m):
        c_y = [int(x) for x in input().split()]
        c.append(c_y[0])
        y.append(c_y[1])
    #print(n, m)
    #print(x)
    #print(c)
    #print(y)
    #print(x[0])
    #print(c[0])
    #print(y[0])
    #print(x[1])
    #print(c[1])
    #print(y[1])
    #print(x[2])
    #print(c[2])
    #print(y[2])
    #print(x[3])
    #print(c[3])
    #print(y[3])
    #print(x[4])
    #print(c[4])
    #print(y[4])
    #print(x[5])
    #print(c[5])
    #print(y[5])
    #print(x[6])
    #print(c[6])
    #print(y[6])
    #print(x[7])
    #print(c[7])
    #print(y[7])
    #print(x[8])
    #print(c[8])
    #print(y[8])
    #print(x[9])
    #print(c[9])
    #print(y[9])
    #print(x[10])
    #print(c[10])
    #print(y[10])
    #print(x[11])
    #print(c[11])
    #print(y[11])
    #print(x[12])
    #print(c[12])
    #print(y[12])
    #print(x[13])
    #print(c[13])
    #print(y[13])
    #print(x[14])
    #print(c[14])
    #print(y[14])
    #print(x[15])
    #print(c[15])
    #print(y[15])
    #print(x[16])
    #print(c[16])
    #print(y[16])
    #print(x[17])
    #print(c[17])
    #print(y[17])
    #print(x[18])
    #print(c[18])
    #print(y[18])
    #print(x[
