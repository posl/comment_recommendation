Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i][j] + a[i] * (j + 1), dp[i][j + 1])

    print(dp[n][m])

=======
Suggestion 2

def max_sum(n, m, a):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, min(i+1, m+1)):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + i*a[i-1])
    return dp[n][m]

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(max_sum(n, m, a))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] + (i + 1) * A[i])
    print(dp[N][M])

=======
Suggestion 4

def max_sum():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
            if i + 1 < n:
                dp[i + 2][j + 1] = max(dp[i + 2][j + 1], dp[i][j] + a[i] * (j + 1) + a[i + 1] * (j + 1))
    print(dp[n][m])

max_sum()

=======
Suggestion 5

def get_max_sum(a, m):
    if m == 0:
        return 0
    if m == 1:
        return max(a)
    if m == 2:
        return max(a[0] + 2 * a[1], 2 * a[0] + a[1])
    if m == 3:
        return max(a[0] + 2 * a[1] + 3 * a[2], a[0] + 2 * a[1] + a[2] + a[3], 2 * a[0] + a[1] + a[2] + a[3])
    if m == 4:
        return max(a[0] + 2 * a[1] + 3 * a[2] + 4 * a[3], a[0] + 2 * a[1] + 3 * a[2] + a[3] + a[4], a[0] + 2 * a[1] + a[2] + a[3] + a[4] + a[5], 2 * a[0] + a[1] + a[2] + a[3] + a[4] + a[5])
    if m == 5:
        return max(a[0] + 2 * a[1] + 3 * a[2] + 4 * a[3] + 5 * a[4], a[0] + 2 * a[1] + 3 * a[2] + 4 * a[3] + a[4] + a[5], a[0] + 2 * a[1] + 3 * a[2] + a[3] + a[4] + a[5] + a[6], a[0] + 2 * a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7], 2 * a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7])
    if m == 6:
        return max(a[0] + 2 * a[1

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j > i:
                continue
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+i*a[i-1])
    print(dp[n][m])

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+a[i]*(j+1))
            if i+1+j+1<=m:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j+1])
    print(dp[n][m])

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,n+1):
        dp[1][i] = dp[1][i-1] + a[i-1]
    for i in range(2,m+1):
        for j in range(i,n+1):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+i*a[j-1])
    print(dp[m][n])

=======
Suggestion 9

def get_max_sum(n, m, a):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, min(i, m) + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + a[i - 1] * j, dp[i - 1][j])
    return dp[n][m]

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    # print(n,m,a)
    # print(type(n),type(m),type(a))
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])
    # print(a[4])
    # print(a[5])
    # print(a[6])
    # print(a[7])
    # print(a[8])
    # print(a[9])
    # print(a[0]+a[1])
    # print(a[0]+a[2])
    # print(a[0]+a[3])
    # print(a[0]+a[4])
    # print(a[0]+a[5])
    # print(a[0]+a[6])
    # print(a[0]+a[7])
    # print(a[0]+a[8])
    # print(a[0]+a[9])
    # print(a[1]+a[2])
    # print(a[1]+a[3])
    # print(a[1]+a[4])
    # print(a[1]+a[5])
    # print(a[1]+a[6])
    # print(a[1]+a[7])
    # print(a[1]+a[8])
    # print(a[1]+a[9])
    # print(a[2]+a[3])
    # print(a[2]+a[4])
    # print(a[2]+a[5])
    # print(a[2]+a[6])
    # print(a[2]+a[7])
    # print(a[2]+a[8])
    # print(a[2]+a[9])
    # print(a[3]+a[4])
    # print(a[3]+a[5])
    # print(a[3]+a[6])
    # print(a[3]+a[7])
    # print(a[3]+a[8])
    # print(a[3]+a[9])
    # print(a[4]+a[5])
    # print(a[4]+a[6])
    # print(a[4]+a[7])
    # print(a[4]+a[8])
    # print(a[4]+a[9])
    # print(a
