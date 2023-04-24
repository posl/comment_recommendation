Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                ans += (A[i]+A[j]+A[k])%998244353
    print(ans%998244353)

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    mod = 998244353
    sumA = sum(A)
    dp = [0] * (sumA + 1)
    dp[0] = 1
    for a in A:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == 0:
                continue
            dp[i + a] += dp[i]
            dp[i + a] %= mod

    ans = 0
    for i in range(len(dp)):
        if dp[i] == 0:
            continue
        if i % N != 0:
            continue
        ans += dp[i]
        ans %= mod
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = ans * pow(2,N-1,MOD)
    ans %= MOD
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    total = sum(A)
    ans = pow(2, N-1, MOD)
    ans *= total
    ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353

    # dp[i][j] = i番目までの要素からj個選んだ時の総和
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j] %= mod
            dp[i + 1][j + 1] += dp[i][j] * A[i]
            dp[i + 1][j + 1] %= mod

    ans = 0
    for i in range(N):
        ans += dp[N][i + 1] * A[i]
        ans %= mod
    print(ans)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

A.sort()
A.reverse()

ans = 0
for i in range(1, N):
    for j in range(i + 1, N + 1):
        ans += gcd(A[i - 1], A[j - 1]) * (2 ** (N - j))
        ans %= 998244353

for i in range(1, N + 1):
    ans += A[i - 1] * (2 ** (N - i))
    ans %= 998244353

print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353

    #dp[i][j] := i番目までの数でj個選んだ時の平均値の合計
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            dp[i+1][j] += dp[i][j]*(j+1)
            dp[i+1][j] %= mod
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
    ans = 0
    for i in range(n):
        ans += dp[n][i]*a[i]
        ans %= mod
    print(ans)
solve()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] は i 個目までの要素で、合計が j のものの個数
    dp = [[0] * (sum(A) + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sum(A) + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j - A[i]] * 2
            else:
                dp[i + 1][j] = dp[i][j]
            dp[i + 1][j] %= MOD
    ans = 0
    for i in range(1, N + 1):
        ans += dp[i][sum(A) // 2] * pow(2, N - i, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 10

def get_integer():
    return int(input())
