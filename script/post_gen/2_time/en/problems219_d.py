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
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0][0] = 0
    for i in range(1, N + 1):
        for j in range(1, Y + 1):
            for k in range(1, X + 1):
                if j - B[i - 1] < 0 or k - A[i - 1] < 0:
                    dp[i][j][k] = dp[i - 1][j][k]
                else:
                    dp[i][j][k] = min(dp[i - 1][j][k], dp[i - 1][j - B[i - 1]][k - A[i - 1]] + 1)
    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])

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
    dp = [[[10**9] * 301 for i in range(301)] for j in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][min(j+A[i], X)][min(k+B[i], Y)] = min(dp[i+1][min(j+A[i], X)][min(k+B[i], Y)], dp[i][j][k]+1)
    if dp[N][X][Y] == 10**9:
        print(-1)
    else:
        print(dp[N][X][Y])

=======
Suggestion 3

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j] = i番目のお弁当までを使って、j個のたこ焼き、k個のたい焼きを作るのに必要な最小枚数
    dp = [[float("inf")] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j - A[i] >= 0 and k - B[i] >= 0:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - A[i]] + dp[i][k - B[i]] + 1)
                else:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    if dp[N][X] == float("inf"):
        print(-1)
    else:
        print(dp[N][X])

=======
Suggestion 4

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(X + 1):
            if j - A[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + B[i - 1])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
    for i in range(N + 1):
        if dp[i][X] >= Y:
            print(i)
            return
    print(-1)

=======
Suggestion 5

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    dp = [[-1] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(x + 1):
            if dp[i][j] == -1:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + a[i] <= x:
                dp[i + 1][j + a[i]] = max(dp[i + 1][j + a[i]], dp[i][j] + b[i])

    ans = -1
    for i in range(x + 1):
        if dp[n][i] >= y:
            ans = i
            break
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
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

=======
Suggestion 7

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    dp = [[[0] * (x + 1) for _ in range(y + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(y + 1):
            for k in range(x + 1):
                if j - b[i] >= 0 and k - a[i] >= 0:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - b[i]][k - a[i]] + 1)
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
    if dp[n][y][x] == 0:
        print(-1)
    else:
        print(dp[n][y][x])

=======
Suggestion 8

def main():
    #input
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    #calc
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j - B[i] >= 0 and k - A[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - B[i]][k - A[i]] + 1)
                elif j - B[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - B[i]][k] + 1)
                elif k - A[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k - A[i]] + 1)

    #output
    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + AB[i][1] <= Y and k + AB[i][0] <= X:
                    dp[i + 1][j + AB[i][1]][k + AB[i][0]] = min(dp[i + 1][j + AB[i][1]][k + AB[i][0]], dp[i][j][k] + 1)
    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])

=======
Suggestion 10

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    for n in range(1, N + 1):
        for y in range(Y + 1):
            for x in range(X + 1):
                a, b = AB[n - 1]
                dp[n][y][x] = dp[n - 1][y][x]
                if y >= b:
                    dp[n][y][x] = max(dp[n][y][x], dp[n - 1][y - b][x] + 1)
                if x >= a:
                    dp[n][y][x] = max(dp[n][y][x], dp[n - 1][y][x - a] + 1)
    print(dp[N][Y][X] if dp[N][Y][X] else -1)
