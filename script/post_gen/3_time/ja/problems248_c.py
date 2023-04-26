Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    mod = 998244353

    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    dp[i + 1][j + k] += dp[i][j]
                    dp[i + 1][j + k] %= mod

    print(dp[N][K])

=======
Suggestion 3

def solve(n, m, k):
    MOD = 998244353
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            for l in range(min(j, m) + 1):
                dp[i][j] += dp[i - 1][j - l]
                dp[i][j] %= MOD
    return dp[n][k]

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for k in range(K + 1):
        for n in range(N + 1):
            for m in range(1, M + 1):
                if k + m > K or n + 1 > N:
                    continue
                dp[k + m][n + 1] += dp[k][n]
                dp[k + m][n + 1] %= MOD
    print(dp[K][N])

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= mod
    ans = 0
    for i in range(1, N+1):
        ans += dp[i-1][M] * dp[N-i][K-i*M] * M
        ans %= mod
    print(ans)

=======
Suggestion 6

def main():
    N,M,K=map(int,input().split())
    mod=998244353
    dp=[[0 for i in range(K+1)] for j in range(N+1)]
    dp[0][0]=1
    for i in range(1,N+1):
        for j in range(K+1):
            for k in range(1,M+1):
                if j-k>=0:
                    dp[i][j]+=dp[i-1][j-k]
                    dp[i][j]%=mod
    print(dp[-1][-1])

=======
Suggestion 7

def solve():
    N, M, K = [int(x) for x in input().split()]
    mod = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            for k in range(M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 8

def main():
    #入力
    N, M, K = map(int, input().split())

    #初期化
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    mod = 998244353

    #初期条件
    dp[0][0][0] = 1

    #DP
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                #i番目の整数をjにする場合
                if k+j <= K:
                    dp[i+1][j][k+j] += dp[i][j][k]
                    dp[i+1][j][k+j] %= mod
                #i番目の整数をj以外にする場合
                dp[i+1][j][k] += dp[i][j][k] * j
                dp[i+1][j][k] %= mod

    #出力
    print(sum(dp[N][i][K] for i in range(1, M+1)) % mod)

=======
Suggestion 9

def solve(N, M, K):
    if N * M < K:
        return 0
    if N > K:
        return 0
    if N == K:
        return 1
    if N == 1:
        return 1
    if M == 1:
        return 1
    if N == 2:
        return M
    if M == 2:
        return N
    return 0

=======
Suggestion 10

def main():
    N,M,K = map(int, input().split())
    MOD = 998244353
    ans = 0

    # i個目までの数列の総和をjとする
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    dp[0][0] = 1

    for i in range(1,N+1):
        for j in range(K+1):
            for k in range(1,M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD

    print(dp[N][K])
