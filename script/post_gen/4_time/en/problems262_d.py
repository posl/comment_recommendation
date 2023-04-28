Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

M = 998244353

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    mod = 998244353
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]+A[j])%2 == 0:
                ans += 2**(N-2)
                ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    mod = 998244353
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            if j + a[i] <= s:
                dp[i+1][j+a[i]] += dp[i][j]
                dp[i+1][j+a[i]] %= mod
    ans = 0
    for i in range(1,s+1):
        if i * n % s == 0:
            ans += dp[n][i]
            ans %= mod
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans = (ans + (A[i] * pow(2, i, MOD)) % MOD) % MOD
    print(ans)

=======
Suggestion 5

def solve(N, A):
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += A[i]
    ans *= pow(2, N-1, mod)
    ans %= mod
    return ans

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # dp[i][j] = i番目までの要素からj個選んだ時の総和
    dp = [[0 for j in range(N+1)] for i in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(i+1):
            dp[i][j] += dp[i-1][j] * 2
            dp[i][j] %= MOD
            if j-1 >= 0:
                dp[i][j] += dp[i-1][j-1] * A[i-1]
                dp[i][j] %= MOD

    ans = 0
    for j in range(1, N+1):
        ans += dp[N][j]
        ans %= MOD
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    A.reverse()
    mod = 998244353
    ans = 0
    for i in range(1,N+1):
        ans = (ans + (A[i-1] * (2**(i-1)) * (2**(N-i))))%mod
    print(ans)
solve()

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # dp[i][j] := i個の要素からなる部分集合のうち、和がjになるものの個数
    dp = [[0] * (sum(A) + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(sum(A) + 1):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j] %= MOD
            if j + A[i] <= sum(A):
                dp[i + 1][j + A[i]] += dp[i][j]
                dp[i + 1][j + A[i]] %= MOD

    ans = 0
    for i in range(1, sum(A) + 1):
        if i % N == 0:
            ans += dp[N][i]
            ans %= MOD
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353

    # 累積和
    # 累積和を作る
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    # 累積和の差の累積和
    T = [0] * (N+1)
    for i in range(N):
        T[i+1] = T[i] + S[i+1]
    # 累積和の差の累積和の差
    U = [0] * (N+1)
    for i in range(N):
        U[i+1] = U[i] + T[i+1]

    # dp[i][j] := i番目までの数を使ってj個選ぶときの場合の数
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(i+1):
            dp[i][j] += dp[i-1][j] * 2
            dp[i][j] %= mod
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] %= mod

    ans = 0
    for i in range(1,N+1):
        ans += dp[N][i] * U[i]
        ans %= mod
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # dp[i] = (i個の要素の和, i個の要素の数)の組み合わせの数
    dp = [0] * (n + 1)
    dp[0] = (0, 1)

    for i in range(n):
        for j in range(i, -1, -1):
            x, y = dp[j]
            dp[j + 1] = (x + a[i] * y, y)

    ans = 0
    for i in range(1, n + 1):
        x, y = dp[i]
        if x % y == 0:
            ans += pow(2, n - i, 998244353) * y
            ans %= 998244353
    print(ans)
