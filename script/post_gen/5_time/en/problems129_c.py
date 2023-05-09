Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    broken = set([int(input()) for _ in range(M)])
    dp = [0] * (N + 1)
    dp[0] = 1
    if 1 not in broken:
        dp[1] = 1
    for i in range(2, N + 1):
        if i not in broken:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    broken = set()
    for _ in range(M):
        broken.add(int(input()))
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i not in broken:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= 10 ** 9 + 7
    print(dp[-1])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    broken_steps = set()
    for i in range(M):
        broken_steps.add(int(input()))

    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken_steps:
            continue
        if i - 1 not in broken_steps:
            dp[i] += dp[i - 1]
        if i - 2 not in broken_steps:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000007
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    broken = set()
    for i in range(M):
        broken.add(int(input()))
    mod = 1000000007
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
    print(dp[N])

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    broken = {int(input()) for _ in range(M)}
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= mod
    print(dp[N])

solve()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N+1)
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in a:
            continue
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])
main()

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = [int(input()) for i in range(m)]
    a.append(n+1)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(m+1):
            if i < a[j]:
                break
            dp[i] += dp[i-a[j]]
            dp[i] %= 10**9+7
    print(dp[n])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    b = []
    for i in range(M+1):
        if i == 0:
            b.append(a[i]-1)
        else:
            b.append(a[i]-a[i-1]-1)
    c = []
    for i in range(M+1):
        if b[i] == 0:
            c.append(1)
        elif b[i] == 1:
            c.append(1)
        else:
            c.append(0)
    for i in range(M+1):
        if i == 0:
            pass
        elif i == 1:
            c[i] = c[i-1]
        else:
            c[i] = (c[i-1] + c[i-2]) % 1000000007
    print(c[M])

=======
Suggestion 9

def climbStairs(n, m, a):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            if i in a:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
print(climbStairs(n, m, a) % (10**9+7))

=======
Suggestion 10

def main():
    # Get input here
    n, m = map(int, input().strip().split())
    a = [int(input()) for _ in range(m)]

    # Calculate the answer from input here
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i not in a:
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
            dp[i] %= mod

    # Print the answer here
    print(dp[n])
