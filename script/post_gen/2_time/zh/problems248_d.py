Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve(n,m,k):
    MOD = 998244353
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,m+1):
        dp[1][i][i] = 1
    for i in range(1,n):
        for j in range(1,m+1):
            for l in range(1,k+1):
                if l+j <= k:
                    dp[i+1][j][l+j] = (dp[i+1][j][l+j] + dp[i][j][l]) % MOD
                dp[i+1][j][l] = (dp[i+1][j][l] + dp[i][j][l]) % MOD
                if j < m and l+j <= k:
                    dp[i+1][j+1][l+j] = (dp[i+1][j+1][l+j] + dp[i][j][l]) % MOD
    ans = 0
    for i in range(1,m+1):
        ans = (ans + dp[n][i][k]) % MOD
    return ans

=======
Suggestion 3

def main():
    n,m,k=map(int,input().split())
    mod=998244353
    dp=[[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        for j in range(m+1):
            for s in range(k+1):
                dp[i+1][j][s]+=dp[i][j][s]
                dp[i+1][j][s]%=mod
                if s+j<=k:
                    dp[i+1][j][s+j]+=dp[i][j][s]
                    dp[i+1][j][s+j]%=mod
    print(dp[n][m][k])

=======
Suggestion 4

def solve(n, m, k):
    dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m + 1):
            for l in range(k + 1):
                dp[i + 1][j][l] += dp[i][j][l]
                dp[i + 1][j][l] %= 998244353
                if j + 1 <= m and l + j + 1 <= k:
                    dp[i + 1][j + 1][l + j + 1] += dp[i][j][l]
                    dp[i + 1][j + 1][l + j + 1] %= 998244353
    return dp[n][m][k]

n, m, k = map(int, input().split())
print(solve(n, m, k))

=======
Suggestion 5

def input():
    return list(map(int, input().split()))

N, M, K = input()

dp = [[[0 for i in range(K+1)] for j in range(M+1)] for k in range(N+1)]
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
Suggestion 6

def main():
    n,m,k = map(int,input().split())
    MOD = 998244353
    dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= MOD
                if j+1 <= m and l+j+1 <= k:
                    dp[i+1][j+1][l+j+1] += dp[i][j][l]
                    dp[i+1][j+1][l+j+1] %= MOD
    print(dp[n][m][k])

=======
Suggestion 7

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            for s in range(1, k+1):
                dp[i][j][s] += dp[i-1][j][s]
                if s - j >= 1:
                    dp[i][j][s] += dp[i-1][j][s-j]
                dp[i][j][s] %= 998244353
    ans = 0
    for j in range(1, m+1):
        ans += dp[n][j][k]
        ans %= 998244353
    print(ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    dp = [[[0 for i in range(K+1)] for j in range(M+1)] for k in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= 998244353
                if j < M and k + j <= K:
                    dp[i+1][j+1][k+j] += dp[i][j][k]
                    dp[i+1][j+1][k+j] %= 998244353
    print(dp[N][M][K])

=======
Suggestion 9

def main():
    n,m,k = map(int,input().split())
    dp = [[[0 for i in range(k+1)] for j in range(m+1)] for l in range(n+1)]
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
