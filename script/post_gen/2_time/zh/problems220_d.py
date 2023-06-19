Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(n):
            ndp = [0] * 10
            for k in range(10):
                ndp[(k + a[j]) % 10] += dp[k]
                ndp[(k + a[j]) % 10] %= mod
                ndp[(k * a[j]) % 10] += dp[k]
                ndp[(k * a[j]) % 10] %= mod
            dp = ndp
        ans[i] = dp[0]
    print(*ans, sep='\n')

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0]*10
    for i in range(10):
        dp = [0]*10
        dp[i] = 1
        for a in A:
            ndp = [0]*10
            for j in range(10):
                ndp[(j+a)%10] += dp[j]
                ndp[(j+a)%10] %= mod
                ndp[(j*a)%10] += dp[j]
                ndp[(j*a)%10] %= mod
            dp = ndp
        ans[i] = dp[0]
    for a in ans:
        print(a)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        x = 0
        y = 0
        for a in A:
            if a + x + y == i:
                x += 1
            elif (a * x + y) % 10 == i:
                y += 1
        ans[i] = x * y % MOD
    print(*ans, sep='\n')

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            dp = [0] * 10
            dp[(i + j) % 10] += 1
            for a in A:
                ndp = [0] * 10
                for k in range(10):
                    ndp[(k * a + (i + j)) % 10] += dp[k]
                    ndp[(k * a + (i * j)) % 10] += dp[k]
                dp = ndp
            for k in range(10):
                ans[k] += dp[k]
    for a in ans:
        print(a % MOD)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            dp = [[0] * 10 for _ in range(N + 1)]
            dp[0][i] = 1
            for k in range(N):
                dp[k + 1][(dp[k][j] + A[k]) % 10] += dp[k][j]
                dp[k + 1][(dp[k][j] * A[k]) % 10] += dp[k][j]
                dp[k + 1][(dp[k][j] + A[k]) % 10] %= mod
                dp[k + 1][(dp[k][j] * A[k]) % 10] %= mod
            ans[j] += dp[N][j]
            ans[j] %= mod
    for i in ans:
        print(i)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353

    # 统计0~9出现的次数
    cnt = [0] * 10
    for a in A:
        cnt[a] += 1

    # 逆元
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(mod // i) * inv[mod % i]) % mod

    # 计算阶乘
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod

    # 计算组合数
    def comb(n, k):
        if n < k:
            return 0
        return fact[n] * inv[k] * inv[n - k] % mod

    # 计算答案
    ans = [0] * 10
    for K in range(10):
        for i in range(0, N + 1, 2):
            j = N - i
            if i > j:
                break
            if i == j:
                ans[K] += comb(cnt[K], i // 2)
            else:
                ans[K] += comb(cnt[K], i) * comb(N - cnt[K], j)
            ans[K] %= mod

    for i in range(10):
        print(ans[i])

solve()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)
    for i in range(1, n):
        tmp = [0] * 10
        for j in range(10):
            for k in range(10):
                tmp[(j + k) % 10] += ans[j] * a[k]
                tmp[(j * k) % 10] += ans[j] * a[k]
        ans = tmp
    for i in range(10):
        print(ans[i] % 998244353)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    # print(A)

    def calc(K):
        # print("K:", K)
        if N == 1:
            return 1 if A[0] == K else 0
        if N == 2:
            return 1 if ((A[0] + A[1]) % 10 == K) else 0
        if N == 3:
            return 1 if (((A[0] + A[1]) % 10) * A[2]) % 10 == K else 0
        if N == 4:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10)) % 10 == K else 0
        if N == 5:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * A[4]) % 10 == K else 0
        if N == 6:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4] + A[5]) % 10)) % 10 == K else 0
        if N == 7:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4] + A[5]) % 10) * A[6]) % 10 == K else 0
        if N == 8:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4] + A[5]) % 10) * ((A[6] + A[7]) % 10)) % 10 == K else 0
        if N == 9:
            return 1 if (((A[0] + A[1]) % 10) * ((A[2] + A[3]) % 10) * ((A[4

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        if a[0] == i:
            ans[i] += 1
    for i in range(n - 1):
        tmp = [0] * 10
        for j in range(10):
            if ans[j] == 0:
                continue
            if a[i + 1] == j:
                tmp[j] += ans[j]
            else:
                tmp[(j + a[i + 1]) % 10] += ans[j]
                tmp[(j * a[i + 1]) % 10] += ans[j]
        ans = tmp
    for i in range(10):
        print(ans[i] % 998244353)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(n + 1)]
        dp[0][0] = 1
        for j in range(n):
            for k in range(10):
                dp[j + 1][(k + a[j]) % 10] += dp[j][k]
                dp[j + 1][(k + a[j]) % 10] %= mod
                dp[j + 1][(k * a[j]) % 10] += dp[j][k]
                dp[j + 1][(k * a[j]) % 10] %= mod
        ans[i] = dp[-1][i]
    print(*ans, sep='\n')
