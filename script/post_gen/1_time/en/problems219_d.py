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

    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                if j - A[i] >= 0 and k - B[i] >= 0:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - A[i]][k - B[i]] + 1)
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])

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
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + B[i] <= Y and k + A[i] <= X:
                    dp[i + 1][j + B[i]][k + A[i]] = min(dp[i + 1][j + B[i]][k + A[i]], dp[i][j][k] + 1)
    ans = dp[N][Y][X]
    if ans == float('inf'):
        ans = -1
    print(ans)

main()

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
    dp = [[[0] * 301 for i in range(301)] for i in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i + 1][j + A[i]][k + B[i]] = max(dp[i + 1][j + A[i]][k + B[i]], dp[i][j][k] + 1)
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])

=======
Suggestion 4

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                dp[i + 1][min(j + A[i], X)][min(k + B[i], Y)] = min(dp[i + 1][min(j + A[i], X)][min(k + B[i], Y)], dp[i][j][k] + 1)
    if dp[N][X][Y] == float('inf'):
        print(-1)
    else:
        print(dp[N][X][Y])

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i + 1][j + A[i]][k + B[i]] = min(dp[i + 1][j + A[i]][k + B[i]], dp[i][j][k] + 1)
    if dp[N][X][Y] == float('inf'):
        print(-1)
    else:
        print(dp[N][X][Y])

=======
Suggestion 6

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j < X:
                    dp[i + 1][min(j + A[i], X)][k] = min(dp[i + 1][min(j + A[i], X)][k], dp[i][j][k] + 1)
                if k < Y:
                    dp[i + 1][j][min(k + B[i], Y)] = min(dp[i + 1][j][min(k + B[i], Y)], dp[i][j][k] + 1)
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
    
    ans = dp[N][X][Y]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[[float('inf')] * (x + y + 1) for _ in range(y + 1)] for _ in range(x + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x + 1):
            for k in range(y + 1):
                dp[j][k][a[i]] = min(dp[j][k][a[i]], dp[j][k][0] + 1)
                dp[j][k][b[i]] = min(dp[j][k][b[i]], dp[j][k][0] + 1)
                if j >= a[i]:
                    dp[j][k][j + b[i]] = min(dp[j][k][j + b[i]], dp[j][k][j] + 1)
                if k >= b[i]:
                    dp[j][k][j + a[i]] = min(dp[j][k][j + a[i]], dp[j][k][k] + 1)
    ans = float('inf')
    for i in range(x, x + y + 1):
        ans = min(ans, dp[x][y][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[[float('inf')] * (x+1) for _ in range(y+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(y+1):
            for k in range(x+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                if j+b[i] <= y:
                    dp[i+1][j+b[i]][k] = min(dp[i+1][j+b[i]][k], dp[i][j][k]+1)
                if k+a[i] <= x:
                    dp[i+1][j][k+a[i]] = min(dp[i+1][j][k+a[i]], dp[i][j][k]+1)
    ans = min(dp[n][y][x], dp[n][x][y])
    if ans == float('inf'):
        ans = -1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[float("inf")] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + AB[i][0] <= X and k + AB[i][1] <= Y:
                    dp[i + 1][j + AB[i][0]][k + AB[i][1]] = min(dp[i + 1][j + AB[i][0]][k + AB[i][1]], dp[i][j][k] + 1)
    print(-1 if dp[N][X][Y] == float("inf") else dp[N][X][Y])

=======
Suggestion 10

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[float('inf')] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 0

    for i in range(N):
        a, b = AB[i]
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if j + a <= X and k + b <= Y:
                    dp[j + a][k + b] = min(dp[j + a][k + b], dp[j][k] + 1)

    ans = dp[X][Y]
    if ans == float('inf'):
        ans = -1
    print(ans)
