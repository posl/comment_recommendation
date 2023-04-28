Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for i in range(Y+1)] for j in range(X+1)] for k in range(N+1)]
    dp[0][0][0] = True
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                if not dp[i][j][k]:
                    continue
                dp[i+1][j][k] = True
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i+1][j+A[i]][k+B[i]] = True
    for i in range(X, X+1):
        for j in range(Y, Y+1):
            if dp[N][i][j]:
                print(i + j)
                return
    print(-1)

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
    #print(N, X, Y)
    #print(A)
    #print(B)
    ans = -1
    for i in range(N):
        for j in range(N):
            if A[i] + B[j] >= X and A[i] + B[j] >= Y:
                if ans == -1:
                    ans = A[i] + B[j]
                else:
                    ans = min(ans, A[i] + B[j])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[False for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = True
    for i in range(1, N+1):
        for x in range(X+1):
            for y in range(Y+1):
                if dp[i-1][x][y]:
                    dp[i][x][y] = True
                    if x+A[i-1] <= X and y+B[i-1] <= Y:
                        dp[i][x+A[i-1]][y+B[i-1]] = True
    ans = -1
    for i in range(1, N+1):
        if dp[i][X][Y]:
            ans = i
            break
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[False for _ in range(Y + 1)] for _ in range(X + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if dp[j][k]:
                    dp[min(X, j + A[i])][min(Y, k + B[i])] = True

    if dp[X][Y]:
        print(0)
        return

    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if dp[j][k]:
                    dp[min(X, j + A[i])][min(Y, k + B[i])] = True

    if dp[X][Y]:
        print(1)
        return

    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if dp[j][k]:
                    dp[min(X, j + A[i])][min(Y, k + B[i])] = True

    if dp[X][Y]:
        print(2)
        return

    print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    dp[min(x + A[i], X)][min(y + B[i], Y)] = True

    for i in range(X, -1, -1):
        for j in range(Y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)

=======
Suggestion 6

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[[False for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    dp[i+1][min(j+a[i], x)][min(k+b[i], y)] = True
    for i in range(x, x+1):
        for j in range(y, y+1):
            if dp[n][i][j]:
                print(n)
                return
    print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # dp[i][j][k] = (i番目までの弁当で、j個以上のたこ焼きを、k個以上のたい焼きを作るための弁当の最小個数)
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0

    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][min(x, j+a[i])][min(y, k+b[i])] = min(dp[i+1][min(x, j+a[i])][min(y, k+b[i])], dp[i][j][k] + 1)

    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])

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
    dp = [[False] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k]:
                    dp[min(x, j + a[i])][min(y, k + b[i])] = True
    for i in range(x, -1, -1):
        for j in range(y, -1, -1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)

=======
Suggestion 9

def get_input():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    return n, x, y, a, b

=======
Suggestion 10

def main():
    N = int(input())

    X, Y = map(int, input().split())

    A = [0] * N
    B = [0] * N

    for i in range(N):
        A[i], B[i] = map(int, input().split())

    dp = [[False for _ in range(Y + 1)] for _ in range(X + 1)]

    dp[0][0] = True

    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    if x + A[i] <= X and y + B[i] <= Y:
                        dp[x + A[i]][y + B[i]] = True

    ans = float('inf')

    for x in range(X, X + 301):
        for y in range(Y, Y + 301):
            if dp[x][y]:
                ans = min(ans, x + y)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
