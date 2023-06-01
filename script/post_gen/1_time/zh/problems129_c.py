Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]

    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    for i in range(N+1):
        for j in range(1,3):
            if i-j >= 0 and not(i-j in a):
                dp[i] += dp[i-j]
                dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 2

def get_input():
    n,m = map(int,input().split())
    a = [0] * m
    for i in range(m):
        a[i] = int(input())
    return n,m,a

=======
Suggestion 3

def climb(n, m, a):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in a:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1000000007

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)

    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(n+1):
        for j in range(m+1):
            if a[j] == i:
                dp[i] = 0
                break
            if a[j] > i:
                break
            dp[i] += dp[i-a[j]]
            dp[i] %= 1000000007
    print(dp[n])

=======
Suggestion 6

def climb_stairs(N, M, broken):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N] % 1000000007

=======
Suggestion 7

def climb_stairs(n, m, a):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        if i in a:
            dp[i] = 0
        else:
            if i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]

n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
print(climb_stairs(n, m, a))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    A.append(N)
    A.append(N+1)
    A.sort()
    dp = [0] * (N + 2)
    dp[0] = 1
    for i in range(1, N + 2):
        if i in A:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N + 1] % 1000000007)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        if dp[i] == 0:
            continue
        for j in range(M + 1):
            if i + a[j] > N:
                break
            dp[i + a[j]] = (dp[i + a[j]] + dp[i]) % 1000000007
    print(dp[N])
