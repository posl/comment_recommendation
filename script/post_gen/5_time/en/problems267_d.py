Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(1, N):
        A[i] += A[i-1]
    ans = 0
    for i in range(N):
        if i+M > N:
            break
        if i == 0:
            ans = max(ans, A[i+M-1])
        else:
            ans = max(ans, A[i+M-1]-A[i-1])
    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M):
        for j in range(N):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j] + (i + 1) * A[j])
    print(dp[M][N])

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = [0] * n
    for i in range(n):
        b[i] = a[i] + b[i-1]
    ans = 0
    for i in range(1, m+1):
        ans = max(ans, b[i-1] + i * b[n-1] - b[n-i-1])
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[-float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i - 1] * j)
    return dp[N][M]

print(solve())

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[-float('inf')]*(M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M+1):
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + A[i]*(i-j+1))
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(dp[N][M])

=======
Suggestion 6

def solve(N, M, A):
    A.sort(reverse=True)
    dp = [[-float('inf') for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M+1):
            if j > i+1:
                break
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + A[i] * j)
    return dp[N][M]

N, M = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, M, A))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(M):
        ans += A[i] * (i + 1)
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    dp = [[-float('inf') for i in range(m+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][j]+a[i]*(i-j))
    print(dp[n][m])

=======
Suggestion 9

def problem():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # print(a)

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + a[i] * (j+1))

    # for i in range(n+1):
    #     print(dp[i])

    print(dp[n][m])

=======
Suggestion 10

def max_sum():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()

    #print(A)

    count = 0
    for i in range(M):
        count += A[i]

    for i in range(M, N):
        if A[i] < 0:
            break
        count += A[i]

    return count

print(max_sum())
