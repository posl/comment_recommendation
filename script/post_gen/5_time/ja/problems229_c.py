Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # dp[i][j] i番目までのチーズで重さがjになるときの最大のおいしさ
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(w+1):
            if j-b[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-b[i]]+a[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

=======
Suggestion 2

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_b = max(B)
    if max_a > 1000:
        max_a = 1000
    if max_b > 1000:
        max_b = 1000
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= B[i]:
                dp[i+1][w] = max(dp[i][w], dp[i][w-B[i]]+A[i])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

=======
Suggestion 3

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # dp[i][j] i番目までのチーズで重さがjの時の最大のおいしさ
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i] + v_i)
    # dp[0][j] = 0
    # dp[i][0] = 0
    dp = [[0 for j in range(w+1)] for i in range(n+1)]

    for i in range(n):
        for j in range(w+1):
            if j < b[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-b[i]] + a[i])

    print(dp[n][w])

=======
Suggestion 4

def main():
    n, w = map(int, input().split())
    a, b = [], []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)

    # dp[i][j]: i番目までのチーズで重さj以下になるときの最大のおいしさ
    dp = [[0]*(w+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(w+1):
            if j >= b[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-b[i]] + a[i])
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[n][w])

=======
Suggestion 5

def solve():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j >= b[i]:
                dp[i+1][j] = max(dp[i][j-b[i]]+a[i], dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

=======
Suggestion 6

def main():
    n, w = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(n):
        if w >= cheese[i][1]:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0]/cheese[i][1]*w
            break
    print(int(ans))

=======
Suggestion 7

def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    dp = [[0] * (w+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j - a[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-a[i]] + b[i])
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[n][w])

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j - B[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]] + A[i])
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[N][W])

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # dp[i][j] := i 番目までのチーズで重さが j 以下になるように選んだときのおいしさの総和の最大値
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= A[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - A[i]] + B[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 10

def main():
    # データ入力
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # DP テーブル定義
    dp = [[0]*(W+1) for i in range(N+1)]

    # DP ループ
    for i in range(N):
        for w in range(W+1):
            if w >= A[i]:
                dp[i+1][w] = max(dp[i][w-A[i]] + B[i], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]

    # 最適値の出力
    print(dp[N][W])
