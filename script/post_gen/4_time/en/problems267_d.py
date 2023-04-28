Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (i + 1) * A[i])
            if i + 2 <= N:
                dp[i + 2][j + 1] = max(dp[i + 2][j + 1], dp[i][j] + (i + 1) * A[i + 1])
    print(dp[N][M])

=======
Suggestion 2

def solve(n, m, a):
    a.sort(reverse=True)
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j] != -float('inf'):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                if j + 1 <= m:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
    return dp[n][m]

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            s += a[i] + a[j]
            if j-i+1 == m:
                break
    print(s)

=======
Suggestion 4

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    dp = [[-1]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(1,M+1):
        for j in range(i,N+1):
            dp[i][j] = max(dp[i-1][j-1]+A[j-1], dp[i][j-1])
    ans = 0
    for i in range(1,M+1):
        ans = max(ans, dp[i][N] + i * S[N-i])
    print(ans)
    return 0

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    b[0] = a[0]
    for i in range(1,n):
        b[i] = b[i-1] + a[i]
    ans = 0
    for i in range(1,n+1):
        ans = max(ans, b[i-1] + (m-i)*a[i-1])
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [[-float('inf')]*(n+1) for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(1,m+1):
        for j in range(n+1):
            if j > 0:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+a[j-1]*i)
            dp[i][j] = max(dp[i][j],dp[i][j-1])
    print(dp[-1][-1])

=======
Suggestion 7

def solve(N, M, A):
    A.sort(reverse=True)
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + (i+1)*A[i])
    return dp[N][M]


N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))

=======
Suggestion 8

def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+a[i]*(j+1))
            if i+2 <= n:
                dp[i+2][j+1] = max(dp[i+2][j+1], dp[i][j]+a[i]*(j+1)+a[i+1]*(j+1))
    print(dp[-1][-1])

solve()

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()

    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(m + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + a[i]
            else:
                dp[i + 1][j] = max(dp[i][j] + a[i], dp[i][j - 1])

    print(dp[n][m])

=======
Suggestion 10

def calc_sum(a, m):
    max_sum = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i + j >= len(a):
                break
            else:
                sum = 0
                for k in range(i, i + j + 1):
                    sum += a[k]
                if sum > max_sum and j + 1 == m:
                    max_sum = sum
    return max_sum

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(calc_sum(a, m))
