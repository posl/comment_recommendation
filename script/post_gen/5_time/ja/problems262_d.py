Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(n):
        ans += a[i]
    ans %= mod
    ans *= pow(2, n-1, mod)
    ans %= mod
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = pow(2, n, mod) - pow(2, n - 1, mod)
    print(ans % mod)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353

    dp = [0] * (sum(a) + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(len(dp) - 1, -1, -1):
            if j - a[i] >= 0:
                dp[j] += dp[j - a[i]]
                dp[j] %= mod
    #print(dp)
    ans = 0
    for i in range(1, len(dp)):
        if dp[i] != 0 and dp[i] % 2 == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A.append(0)
    ans = 1
    cnt = 1
    for i in range(0, N):
        if A[i] != A[i+1]:
            ans *= (pow(2, cnt, 998244353) - 1)
            ans %= 998244353
            cnt = 1
        else:
            cnt += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = 0
    for i in range(1<<n):
        sum = 0
        for j in range(n):
            if (i>>j)&1:
                sum += a[j]
        if sum % n == 0:
            ans += 1
    print(ans % mod)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    mod = 998244353
    ans = 0
    for a in A:
        ans += pow(2, N-1, mod) * a
        ans %= mod
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353

    # dp[i][j] = i番目までの要素からj個選んで平均値が整数になる場合の数
    dp = [[0 for _ in range(10000)] for _ in range(101)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10000):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            dp[i+1][j+a[i]] += dp[i][j]
            dp[i+1][j+a[i]] %= mod

    ans = 0
    for i in range(1, n+1):
        ans += dp[i][i*sum(a)//n]
        ans %= mod
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    MOD = 998244353

    # dp[i][j] := i番目までの数でj個の数を選んだときの総和
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] += dp[i][j] * A[i]
            dp[i + 1][j + 1] %= MOD
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD

    ans = 0
    for i in range(1, N + 1):
        ans += dp[N][i]
        ans %= MOD
    print(ans)
