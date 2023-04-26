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
    dp = [[0 for _ in range(X + Y + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, X + Y + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if j >= A[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + B[i - 1])
            if j >= B[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - B[i - 1]] + A[i - 1])
    for i in range(X, X + Y + 1):
        if dp[N][i] >= X:
            print(i - X)
            return
    print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[float("inf")] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - A[i]] + 1)
            if j - B[i] >= 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - B[i]] + 1)
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    if dp[N][X] == float("inf") or dp[N][Y] == float("inf"):
        print(-1)
    else:
        print(min(dp[N][X], dp[N][Y]))

=======
Suggestion 3

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j][k] = i 番目までの弁当を見て、たこ焼きが j 個、たい焼きが k 個あるときの、
    # 買う弁当の最小個数
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                nj = j + A[i]
                nk = k + B[i]
                if nj <= X and nk <= Y:
                    dp[i + 1][nj][nk] = min(dp[i + 1][nj][nk], dp[i][j][k] + 1)
    ans = dp[N][X][Y]
    if ans == float('inf'):
        ans = -1
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

    # dp[i][j][k] = たこ焼きがj個、たい焼きがk個の時の最小個数
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
Suggestion 5

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
Suggestion 6

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []

    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[[float("inf")] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + B[i] <= Y and k + A[i] <= X:
                    dp[i + 1][j + B[i]][k + A[i]] = min(dp[i + 1][j + B[i]][k + A[i]], dp[i][j][k] + 1)

    if dp[N][Y][X] == float("inf"):
        print(-1)
    else:
        print(dp[N][Y][X])

=======
Suggestion 7

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)

    dp = [[[0 for k in range(Y + 1)] for j in range(X + 1)] for i in range(N + 1)]
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
Suggestion 8

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(0, N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0 for i in range(0, Y + 1)] for j in range(0, X + 1)] for k in range(0, N + 1)]
    for n in range(1, N + 1):
        for x in range(0, X + 1):
            for y in range(0, Y + 1):
                dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x][y])
                if x >= A[n - 1]:
                    dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x - A[n - 1]][y] + 1)
                if y >= B[n - 1]:
                    dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x][y - B[n - 1]] + 1)
    if dp[N][X][Y] == 10 ** 10:
        print(-1)
    else:
        print(dp[N][X][Y])

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[float("inf")] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            if j < AB[i][0] + AB[i][1]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - AB[i][0] - AB[i][1]] + 1)

    if dp[N][X + Y] == float("inf"):
        print(-1)
    else:
        print(dp[N][X + Y])

=======
Suggestion 10

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j - AB[i][1] >= 0 and k - AB[i][0] >= 0:
                    dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j - AB[i][1]][k - AB[i][0]] + 1)
    ans = dp[N][Y][X]
    if ans == float('inf'):
        ans = -1
    print(ans)
