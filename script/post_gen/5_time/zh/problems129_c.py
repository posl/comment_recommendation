Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems129_c():
    return

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    broken = [0] * (n+1)
    for i in range(m):
        broken[int(input())] = 1
    mod = 1000000007
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        if broken[i] == 1:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= mod
    print(dp[n])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [int(input()) for i in range(M)]
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i not in A:
            if i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
                dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 4

def climb_stairs(n, m, a):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(m):
        dp[a[i]] = -1
    for i in range(2, n + 1):
        if dp[i] != -1:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a=[]
    for i in range(m):
        a.append(int(input()))
    a.sort()
    a.append(n)
    b=[0]*(n+1)
    b[0]=1
    for i in range(1,n+1):
        if i in a:
            continue
        elif i-1 in a and i-2 in a:
            b[i]=0
        elif i-1 in a:
            b[i]=b[i-2]
        elif i-2 in a:
            b[i]=b[i-1]
        else:
            b[i]=b[i-1]+b[i-2]
    print(b[n]%1000000007)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = [0 for i in range(n)]
    for i in range(m):
        a[int(input())] = 1
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1,n):
        if a[i] == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[n-1])

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    a = [0]*M
    for i in range(M):
        a[i] = int(input())

    # dp[i] = iにたどり着くまでの方法
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1]+dp[i-2])%1000000007
    print(dp[N])

=======
Suggestion 8

def count_steps(n, m, a):
    steps = [0] * (n + 1)
    steps[0] = 1
    steps[1] = 1
    for i in range(2, n + 1):
        if i in a:
            steps[i] = 0
        else:
            steps[i] = (steps[i - 1] + steps[i - 2]) % 1000000007
    return steps[n]

=======
Suggestion 9

def main():
    pass
