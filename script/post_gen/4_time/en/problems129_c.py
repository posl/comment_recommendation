Synthesizing 10/10 solutions

=======
Suggestion 1

def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    broken = [False] * (n + 1)
    for _ in range(m):
        broken[int(input())] = True

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if broken[i + 1]:
            continue
        dp[i + 1] += dp[i]
        dp[i + 1] %= 1000000007
        if i + 2 <= n:
            dp[i + 2] += dp[i]
            dp[i + 2] %= 1000000007
    print(dp[n])

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * (m + 2)
    a[0] = 0
    a[m + 1] = n + 1
    for i in range(1, m + 1):
        a[i] = int(input())
    a.sort()
    d = [0] * (m + 2)
    d[0] = 1
    d[1] = 1
    for i in range(2, m + 2):
        d[i] = d[i - 1] + d[i - 2]
    ans = 1
    for i in range(1, m + 2):
        ans *= d[a[i] - a[i - 1] - 1]
        ans %= 1000000007
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    broken = [0] * (N + 1)
    for _ in range(M):
        broken[int(input())] = 1
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if broken[i] == 1:
            continue
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        dp[i] %= 10 ** 9 + 7
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    mod = 10**9 + 7

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N + 1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= mod

    print(dp[N])

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = [0]*m
    for i in range(m):
        a[i] = int(input())
    a.append(n+1)
    a.append(0)
    a.sort()
    dp = [0]*(n+1)
    dp[0] = 1
    mod = 10**9+7
    for i in range(m+1):
        for j in range(a[i+1]-a[i]):
            dp[a[i]+j] = (dp[a[i]+j-1]+dp[a[i]+j-2])%mod
    print(dp[n])

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    a = [0]*N
    for i in range(M):
        a[int(input())-1] = 1
    dp = [0]*N
    dp[0] = 1
    for i in range(1,N):
        if a[i] == 1:
            dp[i] = 0
        else:
            if i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
    print(dp[N-1]%(10**9+7))

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    a.append(0)
    a.sort()
    b = []
    for i in range(m+2):
        b.append(a[i+1]-a[i]-1)
    b.sort()
    ans = 0
    if b[0] == 0:
        ans = 1
    else:
        ans = 1
        for i in range(m+2):
            if b[i] != 0:
                ans *= fib(b[i])
                ans %= 1000000007
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N+1)
    a.append(0)
    a.sort()
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(M+1):
        if a[i+1] - a[i] > 1:
            for j in range(a[i+1]-a[i]-1):
                dp[a[i]+j+1] = (dp[a[i]+j] + dp[a[i]+j-1]) % 1000000007
    print(dp[N])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    broken_steps = [int(input()) for _ in range(M)]
    broken_steps.append(N+1)
    broken_steps.sort()
    #print(broken_steps)
    
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i in broken_steps:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])
