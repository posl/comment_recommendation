Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = a[i]
    for j in range(1, m):
        for i in range(j, n):
            dp[i][j] = max(dp[k][j - 1] + a[i] * (i - k) for k in range(j - 1, i))
    print(max(dp[i][m - 1] for i in range(m - 1, n)))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if j > 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + (j * a[i]))
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[n][m])

=======
Suggestion 3

def solve(n,m,a):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+i*a[i-1])
    return dp[n][m]

=======
Suggestion 4

def solve(n,m,a):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i<j:
                dp[i][j] = -100000000
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+a[i-1]*j)
    return dp[n][m]

=======
Suggestion 5

def max_sum_subsequence(N, M, A):
    # dp[i][j]表示前i个数中取j个数的最大值
    dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if j > i:
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1] * j)
    return dp[N][M]

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [[-float("inf")]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+a[i]*(j+1))
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
    print(dp[n][m])

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+a[i-1])
    print(dp[n][m])

=======
Suggestion 9

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[-float("inf")]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+i*a[i-1])
    print(max(dp[-1]))

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[-float("inf")]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j == 0:
                dp[i+1][j] = 0
            else:
                dp[i+1][j] = max(dp[i][j],dp[i][j-1]+j*a[i])
    print(max(dp[n]))
