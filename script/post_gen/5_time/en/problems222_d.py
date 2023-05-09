Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 1
    for i in range(N):
        ans *= max(0, B[i] - A[i] + 1)
        ans %= 998244353
    print(ans)
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [[0 for _ in range(3001)] for _ in range(N)]
    for i in range(A[0], B[0] + 1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(A[i], B[i] + 1):
            dp[i][j] = sum(dp[i - 1][A[i - 1]:j + 1]) % MOD
    print(sum(dp[N - 1]) % MOD)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(N)]
    for i in range(A[0], B[0]+1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    print(sum(dp[N-1]) % MOD)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[0] * 3001 for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = dp[i + 1][j - 1] + dp[i][j]
            dp[i + 1][j] %= 998244353

    print(dp[n][b[n - 1]])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for j in range(3001)] for i in range(n)]
    for i in range(a[0], b[0]+1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(a[i], b[i]+1):
            dp[i][j] = sum(dp[i-1][a[i-1]:j+1]) % mod
    print(sum(dp[n-1]) % mod)
    return

=======
Suggestion 6

def solve(n, a, b):
    dp = [[0 for i in range(3001)] for j in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3001):
            dp[i+1][j] = dp[i][j]
            if j >= a[i] and j <= b[i]:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= 998244353
    return dp[n][3000]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))

=======
Suggestion 7

def solve(N, A, B):
    dp = [[0 for _ in range(3001)] for _ in range(N)]
    for i in range(A[0], B[0]+1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(A[i], B[i]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % 998244353
    return sum(dp[N-1]) % 998244353

=======
Suggestion 8

def solve(n,a,b):
    mod = 998244353
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n+1):
            dp[i+1][j] = dp[i][j]
            if a[i] <= j <= b[i]:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod
    return sum(dp[-1]) % mod

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(n,a,b))

=======
Suggestion 9

def solve(N, A, B):
    MOD = 998244353
    dp = [[0]*(3001) for _ in range(3001)]
    for i in range(A[0], B[0]+1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(3001):
            dp[i][j] = dp[i-1][j]
            if j >= A[i]:
                dp[i][j] += dp[i][j-1]
            if j > B[i]:
                dp[i][j] -= dp[i-1][j-1]
            dp[i][j] %= MOD
    return dp[N-1][3000]

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    p = [0]*(N+1)
    for i in range(N):
        p[i+1] = min(B[i], p[i]+1)
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N+1):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
            if A[i] <= j <= p[i+1]:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
    print(dp[N][N])
