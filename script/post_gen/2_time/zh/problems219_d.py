Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_num = 300
    for i in range(n):
        if a[i] >= x and b[i] >= y:
            if a[i] + b[i] < min_num:
                min_num = a[i] + b[i]
    if min_num == 300:
        print(-1)
    else:
        print(min_num)

=======
Suggestion 2

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][min(j + A[i], X)][min(k + B[i], Y)] |= dp[i][j][k]
                dp[i + 1][j][k] |= dp[i][j][k]
    ans = -1
    for i in range(1, N + 1):
        if dp[i][X][Y]:
            ans = i
            break
    print(ans)

=======
Suggestion 3

def get_input():
    n = int(input())
    x,y = input().split()
    x = int(x)
    y = int(y)
    a = []
    b = []
    for i in range(n):
        ai,bi = input().split()
        a.append(int(ai))
        b.append(int(bi))
    return n,x,y,a,b

=======
Suggestion 4

def solve():
    n = int(input())
    x, y = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[float('inf')] * (y+1) for _ in range(x+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(x,-1,-1):
            for k in range(y,-1,-1):
                if dp[j][k] != float('inf'):
                    dp[min(x,j+A[i])][min(y,k+B[i])] = min(dp[min(x,j+A[i])][min(y,k+B[i])],dp[j][k]+1)
    if dp[x][y] == float('inf'):
        print(-1)
    else:
        print(dp[x][y])

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # print(N, X, Y, A, B)
    # N = 3
    # X, Y = 5, 6
    # A = [2, 3, 2]
    # B = [1, 4, 3]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A = [3, 2, 2]
    # B = [4, 3, 1]
    # N = 3
    # X, Y = 8, 8
    # A

=======
Suggestion 6

def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                a, b = ab[i]
                dp[i+1][min(j+a, x)][min(k+b, y)] = min(dp[i+1][min(j+a, x)][min(k+b, y)], dp[i][j][k]+1)
    print(dp[n][x][y] if dp[n][x][y] != float('inf') else -1)

=======
Suggestion 7

def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    dp = [[[False for _ in range(301)] for _ in range(301)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j + a[i] <= x and k + b[i] <= y:
                        dp[i+1][j+a[i]][k+b[i]] = True
    ans = -1
    for i in range(1, n+1):
        if dp[i][x][y]:
            ans = i
            break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[False for i in range(y+1)] for j in range(x+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j >= a[i] and k >= b[i]:
                    dp[j][k] = dp[j][k] or dp[j-a[i]][k-b[i]]
    if dp[x][y]:
        print(0)
        return
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if j >= a[i] and k >= b[i]:
                    dp[j][k] = dp[j][k] or dp[j-a[i]][k-b[i]]
    if dp[x][y]:
        print(1)
        return
    print(-1)

=======
Suggestion 9

def solve():
    N = int(input())
    X,Y = map(int,input().split())
    AB = []
    for i in range(N):
        A,B = map(int,input().split())
        AB.append((A,B))
    dp = [[False]*(Y+1) for _ in range(X+1)]
    dp[0][0] = True
    for A,B in AB:
        for x in range(X,-1,-1):
            for y in range(Y,-1,-1):
                if x-A >= 0 and y-B >= 0:
                    dp[x][y] = dp[x][y] or dp[x-A][y-B]
    ans = float('inf')
    for x in range(X+1):
        for y in range(Y+1):
            if dp[x][y]:
                ans = min(ans,x+y)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
solve()

=======
Suggestion 10

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    #dp[i][j][k]表示前i种便当中选出j个章鱼烧和k个鱼形蛋糕的最小数量
    dp = [[[float('inf') for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(X+1):
            for k in range(Y+1):
                if j >= a and k >= b:
                    dp[i+1][j][k] = min(dp[i][j][k], dp[i][j-a][k-b]+1)
                else:
                    dp[i+1][j][k] = dp[i][j][k]
    if dp[N][X][Y] == float('inf'):
        print(-1)
    else:
        print(dp[N][X][Y])
