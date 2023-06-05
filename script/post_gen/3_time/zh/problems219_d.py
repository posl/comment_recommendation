Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    return n, x, y, ab

=======
Suggestion 2

def main():
    print('start')
    n = 3
    x = 8
    y = 8
    a = [3, 2, 2]
    b = [4, 3, 1]
    print(n)
    print(x, y)
    print(a, b)

    ans = -1
    for i in range(n):
        for j in range(n):
            if a[i] + b[j] >= x + y:
                if ans == -1:
                    ans = i + j
                else:
                    ans = min(ans, i + j)
    print(ans)

=======
Suggestion 3

def solve():
    n=int(input())
    x,y=map(int,input().split())
    a=[]
    b=[]
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append(ai)
        b.append(bi)
    dp=[[[False for i in range(301)]for j in range(301)]for k in range(n+1)]
    dp[0][0][0]=True
    for i in range(n):
        for j in range(n+1):
            for k in range(n+1):
                if dp[i][j][k]:
                    dp[i+1][j][k]=True
                    if j+a[i]<=n:
                        dp[i+1][j+a[i]][k]=True
                    if k+b[i]<=n:
                        dp[i+1][j][k+b[i]]=True
                    if j+a[i]<=n and k+b[i]<=n:
                        dp[i+1][j+a[i]][k+b[i]]=True
    ans=-1
    for i in range(n+1):
        for j in range(n+1):
            if dp[n][i][j] and i>=x and j>=y:
                ans=i+j
                break
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    #print(n, x, y)
    #print(a)
    #print(b)

    #dp[i][j][k]表示前i种便当中选j个章鱼烧和k个鱼形蛋糕的最小便当数量
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if j >= a[i] and k >= b[i]:
                    dp[i+1][j][k] = min(dp[i][j][k], dp[i][j-a[i]][k-b[i]]+1)
                else:
                    dp[i+1][j][k] = dp[i][j][k]

    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])

=======
Suggestion 5

def main():
    # 读入数据
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # 递推
    dp = [[False for j in range(y + 1)] for i in range(x + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j - a[i] >= 0 and k - b[i] >= 0:
                    dp[j][k] |= dp[j - a[i]][k - b[i]]

    # 输出结果
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)

=======
Suggestion 6

def solve(n, x, y, a, b):
    #dp[i][j][k]表示前i种便当中选出j个章鱼烧和k个鱼形蛋糕的最小便当数
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                dp[i+1][min(x, j+a[i])][min(y, k+b[i])] = min(dp[i+1][min(x, j+a[i])][min(y, k+b[i])], dp[i][j][k] + 1)
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
    return dp[n][x][y] if dp[n][x][y] != float('inf') else -1

=======
Suggestion 7

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(301)] for j in range(301)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(300, -1, -1):
            for k in range(300, -1, -1):
                if dp[j][k] == 1:
                    dp[j + A[i]][k + B[i]] = 1
    ans = -1
    for i in range(X, 301):
        for j in range(Y, 301):
            if dp[i][j] == 1:
                ans = i + j
                break
        if ans != -1:
            break
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for _ in range(y + 1)] for _ in range(x + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k]:
                    dp[min(x, j + a[i])][min(y, k + b[i])] = True
    ans = 10 ** 18
    for i in range(x, y + 1):
        for j in range(y, y + 1):
            if dp[i][j]:
                ans = min(ans, i + j)
    print(ans if ans != 10 ** 18 else -1)
solve()

=======
Suggestion 9

def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)

    dp = [[[0 for _ in range(300 * 300 + 1)] for _ in range(300 + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, 300 + 1):
            for k in range(300 * 300 + 1):
                if k - a[i - 1] >= 0 and j - 1 >= 0:
                    dp[i][j][k] |= dp[i - 1][j - 1][k - a[i - 1]]
                if k - b[i - 1] >= 0:
                    dp[i][j][k] |= dp[i - 1][j][k - b[i - 1]]

    ans = -1
    for i in range(1, n + 1):
        for j in range(1, 300 * 300 + 1):
            if dp[i][x][j] and dp[i][y][j]:
                ans = max(ans, j)
    print(ans)


solve()

=======
Suggestion 10

def get_input():
    n = int(input())
    x, y = map(int, input().split())
    lunch = []
    for i in range(n):
        lunch.append(tuple(map(int, input().split())))
    return n, x, y, lunch
