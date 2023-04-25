Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K+1):
            if j > 0:
                dp[i+1][j] += dp[i][j-1]
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
    ans = [0]*K
    for i in range(1, K+1):
        ans[i-1] = dp[N][i] * dp[N-K][K-i]
        ans[i-1] %= mod
    print('

'.join(map(str, ans)))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
    for i in range(1, K+1):
        print((dp[N-K+1][i] * dp[K-1][i-1]) % mod)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        dp[i][0] = 1
        for j in range(1, N + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
    for i in range(1, K + 1):
        print((dp[N - K + 1][i] * dp[K - 1][i - 1]) % MOD)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for i in range(1, K + 1):
        for j in range(i, N + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
    for i in range(1, K + 1):
        print((dp[i][N] - dp[i - 1][N]) % MOD)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0]*(N+1) for _ in range(K+1)]
    dp[0][0] = 1
    for k in range(K):
        for n in range(N):
            dp[k+1][n+1] = (dp[k+1][n] + dp[k][n])%MOD
    for k in range(1, K+1):
        ans = 0
        for n in range(N, N-K+k-1, -1):
            ans = (ans + dp[k][n])%MOD
        print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    for i in range(K + 1):
        for j in range(N + 1):
            if i == 0:
                dp[i][j] = 0
            elif i == 1:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % mod
    for i in range(1, K + 1):
        print((dp[i][N] * dp[K - i + 1][N]) % mod)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    dp = [[0]*(N+1) for _ in range(K+1)]
    for i in range(K+1):
        dp[i][i] = 1
    for i in range(1, K+1):
        for j in range(i+1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % MOD
    for i in range(1, K+1):
        print((dp[i][N] - dp[i-1][N]) % MOD)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    # dp[i][j]: i個のボールからj個の青いボールを選ぶ方法の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(min(i, K) + 1):
            dp[i][j] = dp[i - 1][j] * j + dp[i - 1][j - 1] * (i - j)
            dp[i][j] %= MOD

    # ans[i]: i回の操作で青いボールを全て取る方法の数
    ans = [0] * (K + 1)
    for i in range(1, K + 1):
        ans[i] = dp[N][i] * i % MOD

    print('

'.join(map(str, ans[1:])))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7

    # dp[i][j]: i個のボールからj個のボールを選ぶ場合の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod

    for i in range(1, K + 1):
        ans = dp[N - K + 1][i] * dp[K - 1][i - 1]
        print(ans % mod)

=======
Suggestion 10

def main():
    # write your code
    n, k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod
            if j > 0:
                dp[i + 1][j] += dp[i][j - 1]
                dp[i + 1][j] %= mod
    print(dp[n][k])
