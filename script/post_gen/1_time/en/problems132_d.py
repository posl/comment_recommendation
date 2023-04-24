Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, k):
    mod = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] * j) % mod
    ans = [0] * (k + 1)
    for i in range(1, k + 1):
        ans[i] = dp[n][i] * dp[n - 1][k - i] % mod
    return ans

n, k = map(int, input().split())
print('

'.join(map(str, solve(n, k))))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
    for i in range(1, K + 1):
        print(dp[N - K + 1][i] * dp[K - 1][i - 1] % MOD)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][0] = 1
        for j in range(1, K+1):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
    for i in range(1, K+1):
        print((dp[N-K][i] * dp[K-1][i-1]) % MOD)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7
    dp = [[0]*(N+1) for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % MOD
    for i in range(1, K+1):
        print((dp[i][N] - dp[i-1][N]) % MOD)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
    for i in range(1, K + 1):
        ans = dp[i][N] * dp[K - i][N] % MOD
        print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for i in range(K):
        for j in range(N):
            dp[i + 1][j + 1] = (dp[i + 1][j] + dp[i][j]) % MOD
    ans = [0] * (K + 1)
    for i in range(K + 1):
        ans[i] = dp[i][N] * dp[K - i][N] % MOD
    for i in range(1, K + 1):
        ans[i] = (ans[i] - ans[i - 1]) % MOD
    print('

'.join(map(str, ans[1:])))

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (N+1) for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % MOD
    ans = [0] * (K+1)
    for i in range(1, K+1):
        ans[i] = (dp[i][N] - dp[i][N-i]) % MOD
    for i in range(1, K+1):
        print(ans[i])

solve()

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    fac = [1]
    for i in range(1, N+1):
        fac.append(fac[-1]*i%MOD)
    finv = [pow(fac[-1], MOD-2, MOD)]
    for i in range(N, 0, -1):
        finv.append(finv[-1]*i%MOD)
    finv.reverse()
    def comb(n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return fac[n]*finv[r]*finv[n-r]%MOD
    for i in range(1, K+1):
        print(comb(N-K+1, i)*comb(K-1, i-1)%MOD)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
    for i in range(1, K+1):
        ans = dp[N-K+1][i] * dp[K-1][i-1]
        print(ans%mod)

=======
Suggestion 10

def main():
    # input
    N, K = map(int, input().split())

    # compute
    mod = 10**9 + 7
    dp = [[0]*(K+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            dp[i][j] %= mod

    # output
    for i in range(1, K+1):
        print(dp[N-K+1][i]*dp[K-1][i-1]%mod)
