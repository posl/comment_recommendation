Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    dp[i + 1][j + k] += dp[i][j]
                    dp[i + 1][j + k] %= MOD
    print(dp[N][K])

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= MOD
    print(dp[N][K])

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (M-1) % MOD
            if j >= i:
                dp[i][j] = (dp[i][j] - dp[i-1][j-i] * (M-2)) % MOD
    print(dp[N][K])

=======
Suggestion 4

def solve(n, m, k):
    mod = 998244353
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            if j + m < k + 1:
                dp[i + 1][j + m] = (dp[i + 1][j + m] + dp[i][j]) % mod
            else:
                dp[i + 1][k] = (dp[i + 1][k] + dp[i][j]) % mod
    return dp[n][k]

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 6

def main():
    # 入力
    N, M, K = map(int, input().split())
    # 処理
    ans = 0
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    # dp[i][j][k] := i番目までの整数からなる数列のうち、条件を満たすものの個数
    # j: 1~Mの整数
    # k: 1~Kの整数
    dp = [[[0] * (K+1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M):
            for k in range(K+1):
                # i番目までの整数からなる数列のうち、条件を満たすものの個数
                # に、i番目にj+1を追加したものを加える
                dp[i+1][j+1][k+j+1] += dp[i][j+1][k]
                dp[i+1][j+1][k+j+1] %= 998244353
                # i番目までの整数からなる数列のうち、条件を満たすものの個数
                # に、i番目にj+1を追加しなかったものを加える
                dp[i+1][j+1][k] += dp[i][j+1][k]
                dp[i+1][j+1][k] %= 998244353
    ans = 0
    for i in range(M+1):
        ans += dp[N][i][K]
        ans %= 998244353
    print(ans)

=======
Suggestion 8

def main():
    N, M, K = map(int, input().split())
    # dp[i][j] := i 個の整数からなる数列で、その総和が j となるような数列の個数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k > K:
                    break
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= 998244353
    print(dp[N][K])

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    # dp[i][j]: i人までで合計jの場合の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(M + 1):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= MOD
    print(dp[N][K])

=======
Suggestion 10

def main():
    #入力
    N, M, K = map(int, input().split())
    #N ≦ K ≦ NM
    #dp[i][j] = i個の数列で、sum _{i=1}^N A_i ≦ j となる数列の個数
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            if j - M - 1 >= 0:
                dp[i][j] -= dp[i-1][j-M-1]
            dp[i][j] %= 998244353
    print(dp[N][K])
