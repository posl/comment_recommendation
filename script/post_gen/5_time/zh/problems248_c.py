Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= MOD
                if j < M and k + j <= K:
                    dp[i+1][j+1][k+j] += dp[i][j][k]
                    dp[i+1][j+1][k+j] %= MOD
    print(dp[N][M][K])

=======
Suggestion 2

def f(n, m, k):
    if k < n or k > n * m:
        return 0
    elif n == 1:
        return 1
    else:
        return sum([f(n - 1, m, k - i) for i in range(1, m + 1)])

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for i in range(k + 1)] for j in range(m + 1)] for l in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m + 1):
            for l in range(k + 1):
                dp[i + 1][j][l] += dp[i][j][l]
                dp[i + 1][j][l] %= 998244353
                if l + j <= k:
                    dp[i + 1][j][l + j] += dp[i][j][l]
                    dp[i + 1][j][l + j] %= 998244353
    print(dp[n][m][k])

=======
Suggestion 4

def f(n, m, k):
    if n==1:
        return m
    if k==0:
        return 1
    if k<0:
        return 0
    if k>m*n:
        return 0
    return f(n-1, m, k)+f(n, m, k-1)

n, m, k = map(int, input().split())
print(f(n, m, k))

=======
Suggestion 5

def main():
    n,m,k = map(int,input().split())
    dp = [[[0 for i in range(k+1)] for j in range(m+1)] for k in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= 998244353
                if l+j <= k:
                    dp[i+1][j][l+j] += dp[i][j][l]
                    dp[i+1][j][l+j] %= 998244353
    print(dp[n][m][k])

=======
Suggestion 6

def get_num(N, M, K):
    if N == 1:
        return 1
    if N == 2:
        return M
    if N == 3:
        return M * (M + 1) / 2
    if N == 4:
        return M * (M + 1) * (M + 2) / 6
    if N == 5:
        return M * (M + 1) * (M + 2) * (M + 3) / 24
    if N == 6:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) / 120
    if N == 7:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) / 720
    if N == 8:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) / 5040
    if N == 9:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) * (M + 7) / 40320
    if N == 10:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) * (M + 7) * (M + 8) / 362880
    if N == 11:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) * (M + 7) * (M + 8) * (M + 9) / 3628800
    if N == 12:
        return M * (M + 1) * (M + 2

=======
Suggestion 7

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for s in range(1, k+1):
                if s - j > 0:
                    dp[i][j][s] = dp[i][j-1][s] + dp[i-1][j-1][s-j]
                else:
                    dp[i][j][s] = dp[i][j-1][s]
    print(dp[n][m][k]%998244353)

=======
Suggestion 8

def solve():
    n,m,k = map(int,input().split())
    dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l] += dp[i][j][l]
                if l+j <= k:
                    dp[i+1][j][l+j] += dp[i][j][l]
                if j+1 <= m:
                    dp[i+1][j+1][l] += dp[i][j][l]
                dp[i+1][j][l] %= 998244353
                dp[i+1][j+1][l] %= 998244353
                dp[i+1][j][l+j] %= 998244353
    print(dp[n][m][k])

solve()

=======
Suggestion 9

def solve():
    return

=======
Suggestion 10

def main():
    N, M, K = map(int, input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                for l in range(M+1):
                    if k+j+l <= K:
                        dp[i+1][l][k+j+l] += dp[i][j][k]
    ans = 0
    for i in range(M+1):
        ans += dp[N][i][K]
    print(ans%998244353)
