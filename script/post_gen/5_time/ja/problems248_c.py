Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    print(N, M, K)

=======
Suggestion 2

def main():
    n,m,k = map(int,input().split())
    mod = 998244353
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1:
                if j <= k:
                    dp[i][j][j] = 1
            else:
                for l in range(1,k+1):
                    dp[i][j][l] = dp[i][j-1][l]
                    if l-j >= 0:
                        dp[i][j][l] += dp[i-1][j][l-j]
                    dp[i][j][l] %= mod
    print(dp[n][m][k])

=======
Suggestion 3

def main():
    n,m,k = map(int,input().split())
    mod = 998244353
    dp = [[[0 for i in range(k+1)] for j in range(m+1)] for l in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                if dp[i][j][l] == 0:
                    continue
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= mod
                if l+j <= k:
                    dp[i+1][j][l+j] += dp[i][j][l]
                    dp[i+1][j][l+j] %= mod
                if j+1 <= m:
                    dp[i+1][j+1][l] += dp[i][j][l]
                    dp[i+1][j+1][l] %= mod
    print(dp[n][m][k])

=======
Suggestion 4

def main():
    n, m, k = map(int, input().split())
    dp = [[[0] * (k+1) for _ in range(m+1)] for _ in range(n+1)]
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
Suggestion 5

def main():
    n,m,k = map(int, input().split())
    mod = 998244353
    dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= mod
                if j < m and l+i+1 <= k:
                    dp[i+1][j+1][l+i+1] += dp[i][j][l]
                    dp[i+1][j+1][l+i+1] %= mod
    print(dp[n][m][k])

=======
Suggestion 6

def main():
    n,m,k=map(int,input().split())
    mod=998244353
    dp=[[[0 for i in range(k+1)] for j in range(m+1)] for k in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l]+=dp[i][j][l]*(m-j)
                dp[i+1][j][l]%=mod
                if l+j+1<=k:
                    dp[i+1][j+1][l+j+1]+=dp[i][j][l]
                    dp[i+1][j+1][l+j+1]%=mod
    print(dp[n][m][k])

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    mod = 998244353

    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= mod
                if k + j + 1 <= K:
                    dp[i+1][j+1][k+j+1] += dp[i][j][k]
                    dp[i+1][j+1][k+j+1] %= mod

    print(dp[N][M][K])

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    print(N, M, K)
    print("Hello World!")

=======
Suggestion 10

def main():
    N, M, K = map(int, input().split())
    #dp[i][j][k] := i番目までの数列でj個の数を使って和がkになる場合の数
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                if j+1 <= M and k+i+1 <= K:
                    dp[i+1][j+1][k+i+1] += dp[i][j][k]
                    dp[i+1][j+1][k+i+1] %= 998244353
                if k+i+1 <= K:
                    dp[i+1][j][k+i+1] += dp[i][j][k]*(j+1)
                    dp[i+1][j][k+i+1] %= 998244353
    print(dp[N][M][K])
