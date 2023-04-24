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
    #print(A, B)

    # dp[i][j] = i 番目までの弁当を買って、たこ焼きを j 個以上食べられるかどうか
    dp = [[False] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X + Y + 1):
            # i 番目の弁当を買わない場合
            if dp[i][j]:
                dp[i + 1][j] = True

            # i 番目の弁当を買う場合
            if j >= A[i] and dp[i][j - A[i]]:
                dp[i + 1][j] = True
            if j >= B[i] and dp[i][j - B[i]]:
                dp[i + 1][j] = True

    #print(dp)
    for i in range(X, X + Y + 1):
        if dp[N][i]:
            print(i - X)
            exit()
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

    # dp[i][j] := i番目までの弁当を選んだとき、たこ焼きがj個以上になる場合の最小個数
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i]] + 1) ただし、j >= A[i]
    # dp[i][j] = dp[i-1][j] ただし、j < A[i]
    # dp[0][j] = INF ただし、j >= 1
    # dp[0][0] = 0
    dp = [[float('inf')] * (X+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(X+1):
            if j >= A[i-1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]

    # dp[i][j] := i番目までの弁当を選んだとき、たい焼きがj個以上になる場合の最小個数
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-B[i]] + 1) ただし、j >= B[i]
    # dp[i][j] = dp[i-1][j] ただし、j < B[i]
    # dp[0][j] = INF ただし、j >= 1
    # dp[0][0] = 0
    dp2 = [[float('inf')] * (Y+1) for _ in range(N+1)]
    dp2[0][0] = 0
    for i in range(1, N+1):
        for j in range(Y

=======
Suggestion 3

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 300 * 300 + 1
    for i in range(1, 2 ** N):
        a = 0
        b = 0
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                a += A[j]
                b += B[j]
                cnt += 1
        if a >= X and b >= Y:
            ans = min(ans, cnt)
    if ans > 300 * 300:
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
    dp = [[[0] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                if j >= B[i] and k >= A[i]:
                    dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - B[i]][k - A[i]] + 1)
                else:
                    dp[i + 1][j][k] = dp[i][j][k]
    if dp[N][Y][X] == 0:
        print(-1)
    else:
        print(N - dp[N][Y][X])

=======
Suggestion 5

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (X + Y + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(X + Y + 1):
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - A[i]] + B[i], dp[i + 1][j])
            if j - B[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - B[i]] + A[i], dp[i + 1][j])
    ans = -1
    for i in range(X + Y + 1):
        if X <= dp[N][i] and Y <= i - dp[N][i]:
            ans = i
            break
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[float('inf')] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + Y + 1):
            if j < A[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - A[i]] + 1)
            if j < B[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - B[i]] + 1)
    if dp[N][X] == float('inf') and dp[N][Y] == float('inf'):
        print(-1)
    else:
        print(min(dp[N][X], dp[N][Y]))

=======
Suggestion 7

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[float('inf')] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(X + Y + 1):
            if j - A[i] >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-A[i]] + 1)
            if j - B[i] >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-B[i]] + 1)
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

    if dp[N][X] < float('inf') and dp[N][Y] < float('inf'):
        print(min(dp[N][X], dp[N][Y]))
    else:
        print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[0] * (X + 1) for _ in range(Y + 1)]
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if j >= A[i] and k >= B[i]:
                    dp[k][j] = max(dp[k][j], dp[k - B[i]][j - A[i]] + 1)
    if dp[Y][X] == 0:
        print(-1)
    else:
        print(N - dp[Y][X])

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                if j - B[i] >= 0 and k - A[i] >= 0:
                    dp[i + 1][j][k] = min(dp[i][j][k], dp[i][j - B[i]][k - A[i]] + 1)
                else:
                    dp[i + 1][j][k] = min(dp[i][j][k], dp[i][j - B[i]][k - A[i]])

    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])

=======
Suggestion 10

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    dp = [[float('inf')]*(X+Y+1) for i in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X+Y+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j >= A[i][0]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-A[i][0]]+1)
            if j >= A[i][1]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-A[i][1]]+1)
    ans = float('inf')
    for i in range(X, X+Y+1):
        ans = min(ans, dp[N][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
