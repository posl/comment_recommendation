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
    dp = [[[float("inf") for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i+1][j+A[i]][k+B[i]] = min(dp[i+1][j+A[i]][k+B[i]], dp[i][j][k]+1)
    ans = dp[N][X][Y]
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j >= A[i] and k >= B[i]:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - A[i]][k - B[i]] + 1)
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
    ans = dp[N][X][Y]
    if ans == 0:
        ans = -1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(1, N + 1):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                if j - B[i - 1] >= 0 and k - A[i - 1] >= 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - B[i - 1]][k - A[i - 1]] + 1)
    ans = min(dp[N][Y][X], dp[N][Y - 1][X], dp[N][Y][X - 1])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    dp = [[[float("inf")] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                if j - B[i] >= 0 and k - A[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i][j][k], dp[i][j - B[i]][k - A[i]] + 1)
                else:
                    dp[i + 1][j][k] = min(dp[i][j][k], dp[i][j][k])

    if dp[N][Y][X] == float("inf"):
        print(-1)
    else:
        print(dp[N][Y][X])

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # dp[i][j] = i種類の食べ物をj個買うときの最小個数
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i]] + 1) if j >= A[i]
    # dp[i][j] = dp[i-1][j] if j < A[i]
    # dp[i][j] = min(dp[i][j], dp[i-1][j-B[i]] + 1) if j >= B[i]
    # dp[i][j] = dp[i][j] if j < B[i]
    dp = [[float('inf')] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(X + Y + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= A[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - A[i - 1]] + 1)
            if j >= B[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - B[i - 1]] + 1)

    ans = float('inf')
    for i in range(X, X + Y + 1):
        ans = min(ans, dp[N][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if dp[i][j][k] == 0:
                    continue
                if j + A[i] <= X:
                    dp[i + 1][j + A[i]][k] = 1
                if k + B[i] <= Y:
                    dp[i + 1][j][k + B[i]] = 1
    for i in range(1, N + 1):
        if dp[i][X][Y] == 1:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 7

def main():
    N = int(input())
    X,Y = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    dp = [[[0 for i in range(Y+1)] for j in range(X+1)] for k in range(N+1)]
    for k in range(N):
        for i in range(X+1):
            for j in range(Y+1):
                if i-A[k]>=0 and j-B[k]>=0:
                    dp[k+1][i][j] = max(dp[k][i-A[k]][j-B[k]]+1,dp[k][i][j])
                dp[k+1][i][j] = max(dp[k+1][i-A[k]][j],dp[k+1][i][j-B[k]],dp[k+1][i][j])
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])

=======
Suggestion 8

def main():
    N = int(input())
    X, Y = map(int, input().split())
    takoyaki = [0]
    taiyaki = [0]
    for _ in range(N):
        a, b = map(int, input().split())
        takoyaki.append(a)
        taiyaki.append(b)
    dp = [[[float("inf")] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + takoyaki[i + 1] <= X and k + taiyaki[i + 1] <= Y:
                    dp[i + 1][j + takoyaki[i + 1]][k + taiyaki[i + 1]] = min(dp[i + 1][j + takoyaki[i + 1]][k + taiyaki[i + 1]], dp[i][j][k] + 1)
    print(dp[N][X][Y] if dp[N][X][Y] != float("inf") else -1)

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            if j + AB[i][0] <= X + Y:
                dp[i + 1][j + AB[i][0]] = min(dp[i + 1][j + AB[i][0]], dp[i][j] + AB[i][1])
            if j + AB[i][1] <= X + Y:
                dp[i + 1][j + AB[i][1]] = min(dp[i + 1][j + AB[i][1]], dp[i][j] + AB[i][0])
    ans = float('inf')
    for i in range(X, X + Y + 1):
        ans = min(ans, dp[N][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[[float("inf")] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0

    for i in range(N):
        a, b = AB[i]
        for j in range(X+1):
            for k in range(Y+1):
                if j >= a and k >= b:
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-a][k-b]+1)
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])

    if dp[N][X][Y] == float("inf"):
        print(-1)
    else:
        print(dp[N][X][Y])
