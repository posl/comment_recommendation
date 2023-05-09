Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m=list(map(int,input().split()))
    x=list(map(int,input().split()))
    cy=[]
    for _ in range(m):
        c,y=list(map(int,input().split()))
        cy.append((c,y))
    return n,m,x,cy

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)

    ans = 0
    for i in range(1, N+1):
        for j in range(M):
            if i >= C[j]:
                ans = max(ans, X[i-1]+Y[j]*(i//C[j]))

    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    #print(n,m,x,c,y)
    dp = [[0]*(n+1) for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                dp[i][j] = -1
    #print(dp)
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            if i == j:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                dp[i+1][i+1] = max(dp[i+1][i+1],dp[i][j]+x[i])
            else:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                dp[i+1][i+1] = max(dp[i+1][i+1],dp[i][j]+x[i])
                if dp[i][j] >= c[j]:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j]+y[j])
    #print(dp)
    ans = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            ans = max(ans,dp[i][j])
    print(ans)

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        c_, y_ = map(int, input().split())
        c.append(c_)
        y.append(y_)
    c_y = sorted(zip(c, y), key=lambda x: x[0])
    c = [x[0] for x in c_y]
    y = [x[1] for x in c_y]
    dp = [[-float("inf") for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+x[i])
            if j+1 in c:
                dp[i+1][1] = max(dp[i+1][1], dp[i][j]+y[c.index(j+1)])
    print(max(dp[n]))

=======
Suggestion 5

def get_input():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    return n, m, x, c, y

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = [list(map(int, input().split())) for _ in range(m)]
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = dp[i][0] + x[i]
    for i in range(n):
        for j in range(1, i+2):
            dp[i+1][j] = max(dp[i][j-1] + x[i], dp[i][j])
    ans = 0
    for i in range(m):
        for j in range(n+1):
            ans = max(ans, dp[j][j-y[i][0]] + y[i][1])
    print(ans)

=======
Suggestion 7

def solve(n, m, x, c, y):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
            dp[i+1][min(j+c[i], n)] = max(dp[i+1][min(j+c[i], n)], dp[i][j+1] + y[i])
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + x[i])
    return max(dp[n])

n, m = map(int, input().split())
x = list(map(int, input().split()))
c = []
y = []
for _ in range(m):
    c_, y_ = map(int, input().split())
    c.append(c_)
    y.append(y_)
print(solve(n, m, x, c, y))

=======
Suggestion 8

def solve(N, M, X, C, Y):
    result = 0
    for i in range(0, N):
        if X[i] == 1:
            result += Y[0]
        elif X[i] == 2:
            result += Y[1]
        elif X[i] == 3:
            result += Y[2]
        else:
            result += Y[3]
    return result

=======
Suggestion 9

def resolve():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    #s = input().rstrip().decode()
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = [list(map(int, input().split())) for i in range(m)]
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    #c = list(map(int, input().split()))

    dp = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(n):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j + 1])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j])

            for k in range(m):
                if i + 1 == y[k][0]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + y[k][1])

            if i + 1 + j + 1 <= n:
                dp[i + 1 + j + 1][0] = max(dp[i + 1 + j + 1][0], dp[i][j] + sum(x[i + 1:i + 1 + j + 1]))

    print(max(dp[n]))

=======
Suggestion 10

def get_max_coin(N, M, X, C, Y):
    max_coin = 0
    for i in range(N):
        coin = X[i]
        for j in range(M):
            if i + 1 == C[j]:
                coin += Y[j]
        if max_coin < coin:
            max_coin = coin
    return max_coin
