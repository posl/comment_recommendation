Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for n in range(N):
        for m in range(M+1):
            for k in range(K+1):
                dp[n+1][m][k] += dp[n][m][k] * (m+1)
                dp[n+1][m][k] %= 998244353
                if k + m + 1 <= K:
                    dp[n+1][m+1][k+m+1] += dp[n][m][k]
                    dp[n+1][m+1][k+m+1] %= 998244353
    print(dp[N][M][K])

=======
Suggestion 2

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                for a in range(j, m+1):
                    if l + a <= k:
                        dp[i+1][a][l+a] += dp[i][j][l]
                        dp[i+1][a][l+a] %= 998244353
    print(sum(dp[n][j][k] for j in range(m+1)) % 998244353)

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            for l in range(1, k+1):
                if i == 1 and j <= l:
                    dp[i][j][l] = 1
                elif i >= 2 and j <= l:
                    dp[i][j][l] = dp[i-1][j][l] + dp[i][j][l-j]
    print(dp[n][m][k] % 998244353)

=======
Suggestion 4

def solve(n,m,k):
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m):
            for l in range(k):
                dp[i+1][j+1][l+1] += dp[i][j][l]
                dp[i+1][j+1][l+1] %= 998244353
                dp[i+1][j][l+1] += dp[i][j][l] * (m-j)
                dp[i+1][j][l+1] %= 998244353
    return dp[n][m][k]

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M):
            for k in range(K):
                dp[i][j][k + 1] += dp[i][j][k]
                dp[i][j + 1][k + 1] += dp[i][j][k]
                dp[i + 1][j + 1][k + 1] += dp[i][j][k]
                dp[i][j][k + 1] %= MOD
                dp[i][j + 1][k + 1] %= MOD
                dp[i + 1][j + 1][k + 1] %= MOD
    print(dp[N][M][K])

=======
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            for l in range(1, m+1):
                if j-l >= 0:
                    dp[i][j] += dp[i-1][j-l]
                    dp[i][j] %= mod
                else:
                    break
    print(dp[n][k])

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    dp = [[[0] * (K+1) for _ in range(M+1)] for __ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= 998244353
                if j+1 <= M and k+i+1 <= K:
                    dp[i+1][j+1][k+i+1] += dp[i][j][k]
                    dp[i+1][j+1][k+i+1] %= 998244353
    print(dp[N][M][K])

=======
Suggestion 8

def main():
    N,M,K = map(int,input().split())
    mod = 998244353

    dp = [[[0 for i in range(K+1)] for j in range(M+1)] for k in range(N+1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= mod
                if k+j <= K:
                    dp[i+1][j][k+j] += dp[i][j][k]
                    dp[i+1][j][k+j] %= mod
                if j+1 <= M:
                    dp[i+1][j+1][k] += dp[i][j][k]
                    dp[i+1][j+1][k] %= mod
    print(dp[N][M][K])

=======
Suggestion 9

def comb(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    if n == 0 or r == 0 or n == r:
        return 1
    if n - r < r:
        r = n - r
    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)
    return c

n, m, k = map(int, input().split())
mod = 998244353
ans = 0
for i in range(n):
    ans += comb(n - 1, i) * m * pow(m - 1, n - i - 1, mod)
    ans %= mod
print(ans)

=======
Suggestion 10

def main():
    N, M, K = map(int, input().split())
    A = [1] * N
    for i in range(1, N):
        A[i] = A[i-1] * (M-1)
    for i in range(N-1, 0, -1):
        A[i] -= A[i-1] * (M-1)
    print(sum(A) % 998244353)
