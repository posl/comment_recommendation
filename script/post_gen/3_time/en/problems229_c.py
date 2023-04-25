Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0] * (W + 1) for i in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - B[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - B[i]] + A[i])
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
    print(dp[N][W])

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][j] = i番目までの品物の中から、重さがj以下となるように選んだときの、価値の総和の最大値
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(N):
        for j in range(W+1):
            if j >= A[i]:
                dp[i+1][j] = max(dp[i][j-A[i]] + B[i], dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[N][W])

main()

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j - B[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - B[i]] + A[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    ans = ans // W
    print(ans)

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(N, W)
    #print(A)
    #print(B)

    #dp = [[0] * (W+1)] * (N+1)
    dp = [[0] * (W+1) for i in range(N+1)]
    #print(dp)

    for i in range(N):
        for j in range(W+1):
            if j - B[i] >= 0:
                dp[i+1][j] = max(dp[i][j-B[i]] + A[i], dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print(dp[N][W])

=======
Suggestion 6

def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, 0, -1):
            if j - B[i] >= 0:
                dp[j] = max(dp[j], dp[j - B[i]] + A[i])
    print(dp[W])

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # dp[i][j] = (i番目までのチーズを使って, 重さjのときの価値の最大値)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - A[i]] + B[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 8

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    c = []
    for i in range(n):
        c.append(a[i] / b[i])

    c = [x for _, x in sorted(zip(c, b), reverse=True)]

    ans = 0
    for i in range(n):
        if w >= c[i]:
            ans += c[i] * a[i]
            w -= c[i]
        else:
            ans += w * a[i]
            break

    print(int(ans))

=======
Suggestion 9

def solve():
    n, w = map(int, input().split())
    a, b = [], []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(w + 1):
            if j - b[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - b[i - 1]] + a[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][w])

=======
Suggestion 10

def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    sum = 0
    for i in range(n):
        a[i], b[i] = map(int, input().split())
        sum += a[i] * b[i]
    dp = [0] * (sum+1)
    for i in range(n):
        for j in range(sum, a[i]-1, -1):
            dp[j] = max(dp[j], dp[j-a[i]] + b[i])
    print(min(sum, w, max(dp[:w+1])))
