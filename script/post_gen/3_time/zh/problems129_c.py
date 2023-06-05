Synthesizing 10/10 solutions

=======
Suggestion 1

def climb_stairs(N, M, a):
    # 建立一个数组，用来存放有多少种方法可以爬上去
    # 数组的长度为N+1，因为有0级台阶
    # 0级台阶，只有一种方法，就是不爬
    # 1级台阶，只有一种方法，就是爬上去
    # 2级台阶，只有两种方法，一次爬一级，或者一次爬两级
    # 3级台阶，有三种方法，一次爬一级，一次爬两级，一次爬一级再爬一级
    # 4级台阶，有五种方法，一次爬一级，一次爬两级，一次爬一级再爬两级，一次爬两级再爬一级，一次爬两级再爬两级
    # 5级台阶，有八种方法，一次爬一级，一次爬两级，一次爬一级再爬两级，一次爬两级再爬一级，一次爬两级再爬两级，一次爬一级再爬一级再爬一级，一次爬一级再爬两级再爬一级，一次爬两级再爬一级再爬一级
    # 6级台阶，有十三种方法，一次爬一级，一次爬两级，一次爬一级再爬两级，一次爬两级再爬一级，一次爬两级再爬两级，一次爬一级再爬一级再爬一级，一次爬一级再爬两级再爬一级，一次爬两级再爬一级再爬一级，一次爬一级再爬一级再爬两级，一次爬一级再爬一级再爬一级再爬一

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = [0]
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%1000000007)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(m):
        a[int(input())] = 1
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n + 1):
        if a[i] == 1:
            continue
        b[i] = (b[i - 1] + b[i - 2]) % 1000000007
    print(b[n])

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
        if i in a:
            dp[i] = 0
    print(dp[n])

=======
Suggestion 5

def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    A = []
    for i in range(M):
        A.append(int(input()))
    A.sort()
    A.append(N)
    A.insert(0, 0)
    ans = 1
    for i in range(M+1):
        ans *= pow(2, A[i+1]-A[i]-1, 1000000007)
        ans %= 1000000007
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(N)
    dp = [0] * (N + 1)
    dp[0] = 1
    MOD = 10 ** 9 + 7
    for i in range(1, N + 1):
        if i in A:
            continue
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        dp[i] %= MOD
    print(dp[N])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    mod = 1000000007

    # 一次性将所有台阶的情况列出来
    # dp[i] 代表到达第i个台阶的方法数
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod

    # 将不能踩的台阶置为0
    for i in range(M):
        dp[A[i]] = 0

    print(dp[N])

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N)
    a.sort()
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if i in a:
            dp[i] = 0
        else:
            if i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]+dp[i-2]
    print(dp[N]%1000000007)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N)
    MOD = 10**9+7
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in a:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= MOD
    print(dp[N])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in a:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[N])
