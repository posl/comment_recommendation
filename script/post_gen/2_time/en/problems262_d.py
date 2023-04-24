Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, i, MOD) * pow(2, N - i - 1, MOD) * A[i]
        ans %= MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, N-i-1, MOD) * A[i] * pow(N, MOD-2, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, 1 << N):
        cnt = 0
        s = 0
        for j in range(N):
            if i >> j & 1:
                cnt += 1
                s += A[j]
        if s % cnt == 0:
            ans += 1
    ans = ans * pow(2, MOD - 2, MOD)
    ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1, n+1):
        ans += pow(2, i-1, mod) * pow(2, n-i, mod) * a[i-1]
    print(ans%mod)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += A[j]
        if s % bin(i).count("1") == 0:
            ans += 1
    print(ans % mod)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # 2^N-1
    ways = pow(2, N, MOD) - 1

    # 2^N-1 - (2^N-1) / gcd(a_1, a_2, ..., a_N)
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
    ways -= pow(2, N, MOD) * pow(gcd, MOD-2, MOD) % MOD
    print(ways % MOD)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 998244353

    # dp[i][j] = the number of ways to choose j terms from the first i terms
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N + 1):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] %= MOD
            dp[i + 1][j + 1] %= MOD

    ans = 0
    for i in range(1, N + 1):
        ans += (dp[N][i] * A[i - 1]) % MOD
        ans %= MOD

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # dp[i][j]: i番目までの整数の和をjとする選び方の数
    dp = [[0] * (N * 10 ** 9 + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N * 10 ** 9 + 1):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j] %= MOD
            if j - A[i] >= 0:
                dp[i + 1][j] += dp[i][j - A[i]]
                dp[i + 1][j] %= MOD

    ans = 0
    for i in range(1, N + 1):
        ans += dp[i][i * sum(A) // N]
        ans %= MOD

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    
    # dp[i][j] = (i個の整数の和がjとなるような選び方の数)
    dp = [[0] * (N*10**9+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N*10**9+1):
            dp[i+1][j] = dp[i][j]
            if j - A[i] >= 0:
                dp[i+1][j] += dp[i][j-A[i]]
            dp[i+1][j] %= MOD
    
    ans = 0
    for i in range(1, N+1):
        for j in range(N*10**9+1):
            if dp[i][j] > 0 and j % i == 0:
                ans += 1
                ans %= MOD
    
    print(ans)

=======
Suggestion 10

def solve(n, a):
    return 0
