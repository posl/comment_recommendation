Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(0, n - 1):
            ndp = [0] * 10
            for k in range(10):
                ndp[(k + a[j]) % 10] += dp[k]
                ndp[(k * a[j]) % 10] += dp[k]
            dp = ndp
        ans[i] = dp[0]
    for i in range(10):
        print(ans[i])

=======
Suggestion 2

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
        ans[i] = dp[n][i]
    print(*ans, sep="\n")

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * n
        for j in range(n):
            if i == a[j]:
                dp[j] = 1
        for _ in range(n - 1):
            dp2 = [0] * (len(dp) - 1)
            for j in range(len(dp) - 1):
                dp2[j] = (dp[j + 1] + dp[j]) % mod
            dp = dp2
        ans[i] = dp[0]
    print(*ans, sep="\n")

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #print(N)
    #print(A)

    #dp[i][j] 表示前i个数，最后一个数为j的方案数
    dp = [[0 for i in range(10)] for j in range(N+1)]

    #初始化
    dp[0][A[0]] = 1

    #状态转移
    for i in range(1, N):
        for j in range(10):
            #F
            #print(i, j, A[i])
            dp[i][(j+A[i])%10] += dp[i-1][j]
            dp[i][(j+A[i])%10] %= 998244353

            #G
            dp[i][(j*A[i])%10] += dp[i-1][j]
            dp[i][(j*A[i])%10] %= 998244353

    #print(dp)

    #输出结果
    for i in range(10):
        print(dp[N-1][i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        dp[i] = 1
        for j in range(N-1):
            nxt = [0] * 10
            for k in range(10):
                nxt[(k + A[j]) % 10] += dp[k]
                nxt[(k * A[j]) % 10] += dp[k]
            dp = nxt
        ans[i] = dp[0]
    for i in range(10):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        for j in range(10):
            dp = [[0] * 10 for _ in range(N)]
            dp[0][(i + j) % 10] = 1
            dp[0][(i * j) % 10] += 1
            for k in range(N - 1):
                for l in range(10):
                    dp[k + 1][(l + A[k + 1]) % 10] += dp[k][l]
                    dp[k + 1][(l + A[k + 1]) % 10] %= MOD
                    dp[k + 1][(l * A[k + 1]) % 10] += dp[k][l]
                    dp[k + 1][(l * A[k + 1]) % 10] %= MOD
            ans[i] += dp[N - 1][j]
            ans[i] %= MOD
    for i in range(10):
        print(ans[i])

=======
Suggestion 7

def cal(a,b):
    return (a+b)%10

=======
Suggestion 8

def problems220_d():
    return None

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [0] * 10
        for j in range(10):
            dp[(i + j) % 10] += 1
        for k in range(n - 1):
            tmp = [0] * 10
            for j in range(10):
                tmp[(j * a[k + 1]) % 10] += dp[j]
                tmp[(j + a[k + 1]) % 10] += dp[j]
            dp = tmp
        for j in range(10):
            ans[j] = (ans[j] + dp[j]) % mod
    for i in range(10):
        print(ans[i])

=======
Suggestion 10

def main():
    n = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10

    for i in range(10):
        ans[i] = 1

    for i in range(n):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j + A[i]) % 10] += ans[j]
            ans2[(j + A[i]) % 10] %= mod
            ans2[(j * A[i]) % 10] += ans[j]
            ans2[(j * A[i]) % 10] %= mod
        ans = ans2
    for i in range(10):
        print(ans[i])
