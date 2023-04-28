Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - A[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - A[i]] + B[i])
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

    print(dp[N][W])

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - A[i]] + B[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j] := i番目までのチーズから重さがjを超えないように選んだときのチーズの価値の最大値
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + B[i])
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j >= A[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - A[i]] + B[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 4

def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    # dp[i][j]: i 番目までのチーズを使って、重さが j 以下になるように選んだときの、チーズのおいしさの総和の最大値
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(w + 1):
            if j >= a[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - a[i]] + b[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[n][w])

=======
Suggestion 5

def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)
    # dp[i][j] := i 番目までの品物の中から、重さが j 以下となるように選んだときの、価値の総和の最大値
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + b[i - 1])
    # i 番目の品物を選ぶ場合、選ばない場合のどちらか
    # i 番目の品物を選ばない場合、dp[i - 1][j] と同じ
    # i 番目の品物を選ぶ場合、dp[i - 1][j - a[i - 1]] + b[i - 1]
    # i 番目の品物を選ぶ場合の価値は、i 番目の品物を選ぶ前の価値に i 番目の品物の価値を足す
    # i 番目の品物を選ぶ場合の重さは、i 番目の品物を選ぶ前の重さから i 番目の品物の重さを引く
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - a[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + b[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][w])

=======
Suggestion 6

def main():
    n, w = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(n):
        a, b = ab[i]
        ans += a * min(b, w)
        w -= min(b, w)
        if w == 0:
            print(ans)
            exit()

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    #dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        a, b = map(int, input().split())
        for w in range(W+1):
            if w-a >= 0:
                dp[i+1][w] = max(dp[i][w-a]+b, dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

=======
Suggestion 8

def main():
    import sys
    readline = sys.stdin.readline

    #N, W = map(int, input().split())
    N, W = map(int, readline().split())
    #AB = [list(map(int, input().split())) for _ in range(N)]
    AB = [list(map(int, readline().split())) for _ in range(N)]
    #dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for w in range(W+1):
            if w >= AB[i][1]:
                dp[i+1][w] = max(dp[i][w-AB[i][1]]+AB[i][0], dp[i][w])
            else:
                dp[i+1][w] = dp[i][w]
    print(dp[N][W])

=======
Suggestion 9

def solve():
    # ナップサック問題
    # dp[i][w] := i 番目までの品物から重さが w を超えないように選んだときの、価値の総和の最大値
    # dp[i+1][w] = max(dp[i][w], dp[i][w-weight[i]] + value[i])

    n, w = map(int, input().split())
    dp = [[0]*(w+1) for _ in range(n+1)]

    for i in range(n):
        weight, value = map(int, input().split())
        for j in range(w+1):
            if j >= weight:
                dp[i+1][j] = max(dp[i][j], dp[i][j-weight] + value)
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])

solve()

=======
Suggestion 10

def solve():
    N, W = map(int, input().split())
    # dp[i][j] := i番目までのチーズで重さがjになるようにしたときのおいしさの最大値
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        a, b = map(int, input().split())
        for j in range(W+1):
            if j - a >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-a] + b)
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])
