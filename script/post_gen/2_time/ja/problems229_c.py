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
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j - B[i] >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-B[i]] + A[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
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
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])

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
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j - A[i] >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-A[i]] + B[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
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
    # print(A)
    # print(B)
    # dp[i][j] = i番目までのチーズで重さj以下のときの最大のおいしさ
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    # print(dp)
    for i in range(N):
        for j in range(W + 1):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]
    # print(dp)
    print(dp[N][W])

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    MAX = 10 ** 5 + 1
    dp = [[0] * MAX for _ in range(N + 1)]
    for i in range(N):
        for j in range(MAX):
            if j >= B[i]:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]

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

    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(N):
        for j in range(W + 1):
            if j - B[i] >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - B[i]] + A[i])
            else:
                dp[i + 1][j] = dp[i][j]

    print(dp[N][W])

=======
Suggestion 7

def main():
    n, w = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    print(solve(n, w, a, b))

=======
Suggestion 8

def main():
    N,W = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i][j],dp[i+1][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[N][W])

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] := i番目までのチーズで重さjの時の最大のおいしさ
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i]] + B[i])
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= AB[i][0]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-AB[i][0]] + AB[i][1])
            else:
                dp[i+1][j] = dp[i][j]

    print(dp[N][W])

=======
Suggestion 10

def solve():
    N, W = map(int, input().split())
    max_A = 10**9
    max_B = 1000

    # dp[i][j] := i番目までのチーズを使って重さjを作るときのチーズのおいしさの最大値
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        a, b = map(int, input().split())
        for j in range(W+1):
            if j - b >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-b] + a)
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][W])
