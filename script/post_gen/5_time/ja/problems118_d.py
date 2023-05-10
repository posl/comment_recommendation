Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-float('inf')] * (n+1)
    dp[0] = 0
    for i in range(n+1):
        for j in range(m):
            if i - match[a[j]] >= 0:
                dp[i] = max(dp[i], dp[i-match[a[j]]]*10 + a[j])
    print(dp[n])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in a:
            if i - j >= 0 and dp[i - j] >= 0:
                dp[i] = max(dp[i], dp[i - j] * 10 + j)
    print(dp[n])

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(n):
        for j in a:
            if i+j <= n:
                dp[i+j] = max(dp[i+j],dp[i]*10+j)
    print(dp[n])

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    match = [2,5,5,4,5,6,3,7,6]
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        for j in range(M):
            if i + match[A[j]-1] <= N:
                dp[i+match[A[j]-1]] = max(dp[i+match[A[j]-1]], dp[i]*10 + A[j])
    print(dp[N])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in range(M):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i-A[j]] * 10 + A[j])
    print(dp[N])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        for j in range(M):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i-A[j]]*10 + A[j])
    print(dp[N])

=======
Suggestion 7

def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(m):
            dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    return dp[n]

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if dp[i] == -1:
            continue
        for j in a:
            if i + j > n:
                continue
            dp[i + j] = max(dp[i + j], dp[i] * 10 + j)
    print(dp[n])

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + a <= N:
                dp[i + a] = max(dp[i + a], dp[i] * 10 + a)
    print(dp[N])

solve()
