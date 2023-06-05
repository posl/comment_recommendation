Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M,K = map(int,input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1,M+1):
        dp[1][i][i] = 1
    for i in range(2,N+1):
        for j in range(1,M+1):
            for k in range(1,K+1):
                if k-j>=0:
                    dp[i][j][k] = dp[i][j][k-j] + dp[i-1][j-1][k-j]
    print(dp[N][M][K] % 998244353)

=======
Suggestion 2

def main():
    N,M,K = map(int,input().split())
    dp = [[[0 for k in range(K+1)] for j in range(M+1)] for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            for k in range(1,K+1):
                if i == 1 and j <= k:
                    dp[i][j][k] = 1
                elif j <= k:
                    dp[i][j][k] = (dp[i-1][j][k] * j + dp[i][j-1][k] * (k+1-j)) % 998244353
    print(dp[N][M][K])

=======
Suggestion 3

def solve(n, m, k):
    dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        for j in range(m + 1):
            for s in range(k + 1):
                dp[i][j][s] += dp[i - 1][j][s]
                if j > 0 and s >= i:
                    dp[i][j][s] += dp[i - 1][j - 1][s - i]
                dp[i][j][s] %= 998244353
    return dp[n][m][k]

n, m, k = map(int, input().split())
print(solve(n, m, k))

=======
Suggestion 4

def solve():
    N, M, K = map(int, input().split())
    dp = [[[0 for k in range(K+1)] for j in range(M+1)] for i in range(N+1)]
    dp[0][0][0] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            for k in range(K+1):
                dp[i][j][k] += dp[i][j-1][k]
                if k >= j:
                    dp[i][j][k] += dp[i-1][j][k-j]
                dp[i][j][k] %= 998244353
    print(dp[N][M][K])

=======
Suggestion 5

def f(n,m,k):
    if n == 1:
        return k
    if n == 2:
        return k*(k+1)//2
    if n == 3:
        return k*(k+1)*(k+2)//6
    if n == 4:
        return k*(k+1)*(k+2)*(k+3)//24
    if n == 5:
        return k*(k+1)*(k+2)*(k+3)*(k+4)//120
    if n == 6:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)//720
    if n == 7:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)//5040
    if n == 8:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)*(k+7)//40320
    if n == 9:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)*(k+7)*(k+8)//362880
    if n == 10:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)*(k+7)*(k+8)*(k+9)//3628800
    if n == 11:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)*(k+7)*(k+8)*(k+9)*(k+10)//39916800
    if n == 12:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)*(k+7)*(k+8)*(k+9)*(k+10)*(k+11)//479001600
    if n == 13:
        return k*(k+1)*(k+2)*(k+3)*(k+4)*(k+5)*(k+6)*(k+7)*(k+8)*(k+9)*(k+10)*(k+11)*(k+12)//6227020800
    if n ==

=======
Suggestion 6

def count_seq(n, m, k):
    if n == 1:
        return k
    if n == 2:
        return k * (k + 1) // 2
    if n == 3:
        return k * (k + 1) * (k + 2) // 6
    if n == 4:
        return k * (k + 1) * (k + 2) * (k + 3) // 24
    if n == 5:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) // 120
    if n == 6:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) // 720
    if n == 7:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) // 5040
    if n == 8:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) * (k + 7) // 40320
    if n == 9:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) * (k + 7) * (k + 8) // 362880
    if n == 10:
        return k * (k + 1) * (k + 2) * (k + 3) * (k + 4) * (k + 5) * (k + 6) * (k + 7) * (k + 8) * (k + 9) // 3628800
    if n == 11:
        return k * (k + 1) * (k + 2) * (k + 3) * (k +

=======
Suggestion 7

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for l in range(1, k+1):
                if l - j >= 0:
                    dp[i][j][l] = (dp[i][j-1][l] + dp[i-1][j][l-j]) % 998244353
                else:
                    dp[i][j][l] = dp[i][j-1][l]
    print(dp[n][m][k])

=======
Suggestion 8

def main():
    n,m,k = map(int,input().split())
    dp = [[[0]*(k+1) for i in range(m+1)] for j in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l] += dp[i][j][l]
                dp[i+1][j][l] %= 998244353
                if l+j <= k:
                    dp[i+1][j][l+j] += dp[i][j][l]
                    dp[i+1][j][l+j] %= 998244353
                if j+1 <= m:
                    dp[i+1][j+1][l] += dp[i][j][l]
                    dp[i+1][j+1][l] %= 998244353
    print(dp[n][m][k])

=======
Suggestion 9

def dfs(n, m, k):
    if n == 0:
        return 1 if k == 0 else 0
    if dp[n][k] != -1:
        return dp[n][k]
    res = 0
    for i in range(1, m+1):
        if k-i >= 0:
            res += dfs(n-1, m, k-i)
    dp[n][k] = res
    return res

n, m, k = map(int, input().split())
dp = [[-1 for i in range(k+1)] for j in range(n+1)]
print(dfs(n, m, k))

=======
Suggestion 10

def f(n,m,k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]
    res = 0
    for i in range(m+1):
        if k-i >= 0:
            res += f(n-1,m,k-i)
    dp[n][k] = res % 998244353
    return dp[n][k]

N,M,K = map(int,input().split())
dp = [[-1 for i in range(K+1)] for j in range(N+1)]
print(f(N,M,K))
