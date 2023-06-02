Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 10
    for i in a:
        b[i] += 1
    ans = [0] * 10
    ans[0] = b[0] * (b[0] - 1) // 2 % 998244353
    for i in range(1, 10):
        ans[i] = b[0] * b[i] % 998244353
    for i in range(1, 5):
        ans[i * 2] += b[i] * (b[i] - 1) // 2 % 998244353
        ans[i * 2] %= 998244353
        for j in range(i + 1, 5):
            ans[i + j] += b[i] * b[j] * 2 % 998244353
            ans[i + j] %= 998244353
    for i in range(10):
        print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * 10
    for k in range(10):
        for i in range(n):
            if a[i] == k:
                if i % 2 == 0:
                    ans[k] += 1
                else:
                    ans[k] += 998244353 - 1

    for k in range(10):
        print(ans[k] % 998244353)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(n, a)

    # 10个数，每个数的个数
    cnt = [0] * 10
    for i in a:
        cnt[i] += 1
    # print(cnt)

    # 逆向思维，最后的结果是K，那么最开始的数是几，就有几种可能
    # 从大到小，一共10种可能
    for k in range(10):
        ans = 0
        # 前面的数，从大到小
        for i in range(10):
            # 后面的数，从大到小
            for j in range(10):
                # i 和 j 的可能性
                # i + j = k
                # 9 + 1 = 10
                # 8 + 2 = 10
                # 7 + 3 = 10
                # 6 + 4 = 10
                # 5 + 5 = 10
                # 4 + 6 = 10
                # 3 + 7 = 10
                # 2 + 8 = 10
                # 1 + 9 = 10
                # 0 + 0 = 0
                # i * j = k
                # 9 * 1 = 9
                # 8 * 2 = 16
                # 7 * 3 = 21
                # 6 * 4 = 24
                # 5 * 5 = 25
                # 4 * 6 = 24
                # 3 * 7 = 21
                # 2 * 8 = 16
                # 1 * 9 = 9
                # 0 * 0 = 0
                # 9 + 1 = 10
                # 8 + 2 = 10
                # 7 + 3 = 10
                # 6 + 4 = 10
                # 5 + 5 = 10
                # 4 + 6 = 10
                # 3 + 7 = 10
                #

=======
Suggestion 5

def solve(n, a):
    # print(n, a)
    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)
    # print(ans)
    for i in range(n - 1):
        tmp = [0] * 10
        for j in range(10):
            tmp[(j + a[i]) % 10] += ans[j]
            tmp[(j * a[i]) % 10] += ans[j]
        ans = tmp
        # print(ans)
    return ans

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0]*10
    for i in range(10):
        ans[i] = 0
    ans[a[-1]] = 1
    for i in range(n-1):
        tmp = [0]*10
        for j in range(10):
            tmp[(j+a[n-2-i])%10] += ans[j]
            tmp[(j*a[n-2-i])%10] += ans[j]
        ans = tmp
    for i in range(10):
        print(ans[i]%998244353)

=======
Suggestion 7

def f(a,b):
    return (a+b)%10

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))

    mod = 998244353

    dp = [0] * 10
    dp[a[0]] = 1

    for i in range(n - 1):
        new_dp = [0] * 10
        for j in range(10):
            new_dp[(j + a[i + 1]) % 10] += dp[j]
            new_dp[(j + a[i + 1]) % 10] %= mod
            new_dp[(j * a[i + 1]) % 10] += dp[j]
            new_dp[(j * a[i + 1]) % 10] %= mod
        dp = new_dp

    for i in range(10):
        print(dp[i])

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(10)]
        for a in range(10):
            for b in range(10):
                dp[(a + b) % 10][b] += 1
                dp[a][(a * b) % 10] += 1
        for a in range(10):
            for b in range(10):
                dp[a][b] %= mod
        for a in range(N - 1):
            for b in range(10):
                dp[(A[a] + b) % 10][b] += dp[A[a]][b]
                dp[A[a]][(A[a] * b) % 10] += dp[A[a]][b]
                dp[(A[a] + b) % 10][b] %= mod
                dp[A[a]][(A[a] * b) % 10] %= mod
        ans[i] = dp[A[-1]][i]
    print(*ans, sep='\n')

solve()

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10

    for i in range(10):
        dp = [0] * 10
        dp[i] = 1

        for j in range(n - 1):
            nxt = [0] * 10
            for k in range(10):
                nxt[(k + a[j]) % 10] = (nxt[(k + a[j]) % 10] + dp[k]) % mod
                nxt[(k * a[j]) % 10] = (nxt[(k * a[j]) % 10] + dp[k]) % mod
            dp = nxt

        for j in range(10):
            ans[j] = (ans[j] + dp[j]) % mod

    for i in range(10):
        print(ans[i])
