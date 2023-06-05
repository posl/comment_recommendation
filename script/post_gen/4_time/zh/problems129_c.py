Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    N, M = map(int, input().split())
    a = [0] * (M + 2)
    a[0] = 0
    a[M + 1] = N
    for i in range(1, M + 1):
        a[i] = int(input())
    return N, M, a

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def climb_stairs(n, m, a):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    broken = [False for i in range(n + 1)]
    for i in a:
        broken[i] = True
    for i in range(1, n + 1):
        if not broken[i]:
            if i == 1:
                dp[i] = dp[i - 1]
            else:
                dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]

=======
Suggestion 4

def climb_stairs(n, m, a):
    # 0到n的台阶，m个破损台阶，a为破损台阶的位置
    # 状态转移方程：dp[i] = dp[i-1] + dp[i-2]
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i not in a:
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1000000007

=======
Suggestion 5

def climb_stairs(n, a):
    stairs = [0] * (n + 1)
    stairs[0] = 1
    for i in range(1, n + 1):
        for j in range(len(a)):
            if i - a[j] >= 0:
                stairs[i] += stairs[i - a[j]]
                stairs[i] %= 1000000007
    return stairs[n]

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    broken = [int(input()) for _ in range(m)]

    # 1. 一次爬1阶或2阶，爬到第i阶的方法数记为dp[i]
    # 2. 如果第i阶是坏的，则dp[i] = 0
    # 3. 如果第i阶不是坏的，则dp[i] = dp[i-1] + dp[i-2]
    # 4. 边界条件：dp[0] = 1, dp[1] = 1, dp[2] = 2

    # 1. 一次爬1阶或2阶，爬到第i阶的方法数记为dp[i]
    dp = [0] * (n + 1)

    # 2. 如果第i阶是坏的，则dp[i] = 0
    for b in broken:
        dp[b] = -1

    # 4. 边界条件：dp[0] = 1, dp[1] = 1, dp[2] = 2
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    # 3. 如果第i阶不是坏的，则dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        if dp[i] != -1:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    print(dp[n])

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = [0] * (n+1)
    for i in range(m):
        a[int(input())] = -1
    a[0] = 1
    for i in range(1,n+1):
        if a[i] != -1:
            if a[i-1] != -1:
                a[i] += a[i-1]
            if a[i-2] != -1:
                a[i] += a[i-2]
            a[i] %= 1000000007
    print(a[n])

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = [int(input()) for _ in range(m)]
    a.append(n+1)
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(m+1):
            if i+1 == a[j]:
                dp[i] = 0
            elif i+1 > a[j]:
                dp[i] = (dp[i] + dp[i-a[j]-1]) % mod
    print(dp[n])

=======
Suggestion 9

def climb(N,M,a):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        dp = [0 for i in range(N+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,N+1):
            if i in a:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

N,M = map(int,input().split())
a = []
for i in range(M):
    a.append(int(input()))

print(climb(N,M,a)%1000000007)
