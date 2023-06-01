Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def func(n, a, b):
    result = 1
    for i in range(n):
        result *= (b[i] - a[i] + 1)
    return result % 998244353

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    # 用dp[i][j]表示长度为i，第i个数为j的方案数
    dp = [[0] * 3001 for i in range(n + 1)]
    for i in range(a[0], b[0] + 1):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(a[i - 1], b[i - 1] + 1):
            for k in range(j, b[i - 2] + 1):
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= mod
    print(sum(dp[n]) % mod)

solve()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    MOD = 998244353

    # dp[i][j] = C[i][j] * dp[i-1][j]
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(3001):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
            if j >= a[i]:
                dp[i+1][j] += dp[i][j-a[i]]
                dp[i+1][j] %= MOD
            if j >= b[i]:
                dp[i+1][j] -= dp[i][j-b[i]-1]
                dp[i+1][j] %= MOD

    print(dp[n][3000])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mod = 998244353

    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= mod

    print(ans)

=======
Suggestion 5

def func(n,a,b):
    result = 1
    for i in range(n):
        result *= (b[i]-a[i]+1)
    print(result%998244353)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    MOD = 998244353

    dp = [[0] * 3001 for _ in range(N + 1)]

    dp[0][0] = 1

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] = dp[i][j]
        for j in range(1, 3001):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i + 1][j - 1]) % MOD

    print(dp[N][3000])

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    ans = 1
    for i in range(N):
        ans *= max(0, B[i] - A[i] + 1)
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353

    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(a[i - 1], b[i - 1] + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod

    print(dp[n][b[n - 1]])

=======
Suggestion 9

def get_num(n, a, b):
    #print(n, a, b)
    if n == 1:
        return b[0] - a[0] + 1
    else:
        return get_num(n-1, a[:-1], b[:-1]) + b[-1] - a[-1] + 1

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(get_num(n, a, b) % 998244353)
