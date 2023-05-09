Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
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
Suggestion 2

def solve(N, M, K):
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                for l in range(j, M+1):
                    if k + l <= K:
                        dp[i+1][l][k+l] += dp[i][j][k]
                        dp[i+1][l][k+l] %= 998244353
    return sum(dp[N][j][K] for j in range(M+1)) % 998244353

N, M, K = map(int, input().split())
print(solve(N, M, K))

=======
Suggestion 3

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, M+1):
        dp[1][i][i] = 1
    for i in range(2, N+1):
        for j in range(1, M+1):
            for k in range(1, K+1):
                dp[i][j][k] = dp[i][j-1][k]
                if k >= j:
                    dp[i][j][k] += dp[i-1][j-1][k-j]
                dp[i][j][k] %= mod
    print(dp[N][M][K])

=======
Suggestion 4

def problem248_c():
    N, M, K = map(int, input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                if dp[i][j][k] == 0:
                    continue
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= 998244353
                if k+j <= K:
                    dp[i+1][j+1][k+j] += dp[i][j][k]
                    dp[i+1][j+1][k+j] %= 998244353
    print(dp[N][M][K])

=======
Suggestion 5

def main():
    n,m,k = map(int,input().split())
    dp = [[[0]*(k+1) for i in range(m+1)] for j in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m):
            for l in range(k+1):
                dp[i][j][l] %= 998244353
                dp[i+1][j][l] += dp[i][j][l]
                if l+j+1 <= k:
                    dp[i+1][j+1][l+j+1] += dp[i][j][l]
    ans = 0
    for i in range(m+1):
        ans += dp[n][i][k]
    print(ans%998244353)

=======
Suggestion 6

def solve(N,M,K):
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(M):
            for k in range(K+1):
                dp[i+1][j+1][k] += dp[i][j][k]
                dp[i+1][j+1][k] %= 998244353
                if k+j+1 <= K:
                    dp[i+1][j+1][k+j+1] += dp[i][j][k]
                    dp[i+1][j+1][k+j+1] %= 998244353

    return dp[N][M][K]

N,M,K = map(int, input().split())
print(solve(N,M,K))

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        ndp = [0] * (K + 1)
        for j in range(1, M + 1):
            for k in range(K - j, -1, -1):
                ndp[k + j] += dp[k]
                ndp[k + j] %= MOD
        dp = ndp
    print(dp[K])

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    from operator import mul
    from functools import reduce
    from itertools import combinations_with_replacement

    MOD = 998244353

    def ncr(n, r):
        if r > n:
            return 0
        r = min(r, n-r)
        numer = reduce(mul, range(n, n-r, -1), 1)
        denom = reduce(mul, range(1, r+1), 1)
        return (numer // denom) % MOD

    def ncr2(n, r):
        return fact[n] * factinv[r] * factinv[n-r] % MOD

    def ncr3(n, r):
        return fact[n] * inv(r) * inv(n-r) % MOD

    def inv(n):
        return pow(n, MOD-2, MOD)

    N, M, K = map(int, sys.stdin.readline().split())

    fact = [1] * (N+1)
    factinv = [1] * (N+1)
    for i in range(1, N+1):
        fact[i] = fact[i-1] * i % MOD
        factinv[i] = inv(fact[i])

    ans = 0
    for i in range(N+1):
        tmp = ncr3(N-1, i)
        tmp *= pow(M-1, N-i-1, MOD)
        tmp *= M
        tmp %= MOD
        ans += tmp
        ans %= MOD
    print(ans)

=======
Suggestion 9

def find_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

=======
Suggestion 10

def count_sequences(N, M, K):
    #print("N=", N, " M=", M, " K=", K)
    if N == 1:
        return M
    else:
        count = 0
        for i in range(1, M+1):
            count += count_sequences(N-1, M, K-i)
        return count

N, M, K = map(int, input().split())
print(count_sequences(N, M, K) % 998244353)
