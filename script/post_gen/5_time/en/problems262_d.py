Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, N+1):
        for j in range(N-i+1):
            ans += sum(A[j:j+i])%i == 0
    print(ans%MOD)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    ans = 0
    for i in range(N):
        ans = (ans + A[i])%mod
    ans = ans * pow(2,N-1,mod)
    ans = ans % mod
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353

    dp = [[0 for _ in range(5000)] for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(5000):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            dp[i+1][j+A[i]] += dp[i][j]
            dp[i+1][j+A[i]] %= mod

    ans = 0
    for i in range(5000):
        if i % 2 == 0:
            ans += dp[N][i]
            ans %= mod

    print(ans)

=======
Suggestion 4

def solve(n, a):
    return 0

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 5

def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += a[i] == a[j]
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 6

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

=======
Suggestion 7

def count_average(n, a):
    count = 0
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j) != 0:
                sum += a[j]
        if sum % len(bin(i)[2:]) == 0:
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
print(count_average(n, a))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # dp[i][j] = i番目までの数字を使ってjを作る組み合わせの総数
    dp = [[0] * (sum(A)+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sum(A)+1):
            dp[i+1][j] += dp[i][j]
            if j + A[i] < sum(A)+1:
                dp[i+1][j+A[i]] += dp[i][j]
            dp[i+1][j] %= MOD
            dp[i+1][j+A[i]] %= MOD

    ans = 0
    for i in range(1, sum(A)+1):
        if i % N == 0:
            ans += dp[N][i]
    print(ans % MOD)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # sum(A) * (2 ** (N - 1)) % MOD
    ans = 0
    for a in A:
        ans += a
        ans %= MOD

    ans *= pow(2, N - 1, MOD)
    ans %= MOD

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353

    # 0～N-1までの整数の2^N-1通りの部分集合のうち、整数平均をとったものが整数になるものの個数を求める
    # 0～N-1までの整数の2^N-1通りの部分集合のうち、整数平均をとったものが整数になるものの個数を求める
    # dp[i][j] = i番目までの要素の部分集合のうち、整数平均をとったものがjになるものの個数
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-A[i-1]]  (j-A[i-1] >= 0)
    dp = [[0 for _ in range(sum(A)+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(sum(A)+1):
            dp[i][j] = dp[i-1][j]
            if j-A[i-1] >= 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-A[i-1]]) % MOD
    ans = 0
    for i in range(1, sum(A)+1):
        if i * N in A:
            ans = (ans + dp[N][i]) % MOD
    print(ans)
