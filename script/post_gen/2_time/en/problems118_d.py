Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0 and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[N])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in A:
            if i - j >= 0 and dp[i-j] != -1:
                dp[i] = max(dp[i], dp[i-j] * 10 + j)
    print(dp[-1])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    matchsticks = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N):
        for j in A:
            if i + matchsticks[j-1] <= N:
                dp[i+matchsticks[j-1]] = max(dp[i+matchsticks[j-1]], dp[i]*10+j)
    print(dp[N])

=======
Suggestion 4

def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(m):
            if i + a[j] <= n:
                dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    return dp[n]

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a = [2, 5, 5, 4, 5, 6, 3, 7, 6]
n = 20
m = 9
print(solve(n, m, a))

=======
Suggestion 5

def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if dp[i] == -1:
            continue
        for j in range(m):
            if i + a[j] <= n:
                dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    return dp[n]

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a = [2, 5, 5, 4, 5, 6, 3, 7, 6]
print(solve(n, m, a))

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    dp = [-1]*(N+1)
    dp[0] = 0
    for i in range(N+1):
        if dp[i] == -1:
            continue
        for a in A:
            if i+a <= N:
                dp[i+a] = max(dp[i+a],dp[i]*10+a)
    print(dp[N])

=======
Suggestion 7

def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i >= a[j][1] and dp[i - a[j][1]] != -1:
                dp[i] = max(dp[i], dp[i - a[j][1]] * 10 + a[j][0])
    return dp[n]

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A.append(0)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N):
        if dp[i] == -1:
            continue
        for j in range(M):
            if i + A[j] <= N:
                dp[i + A[j]] = max(dp[i + A[j]], dp[i] * 10 + A[j])
    print(dp[N])

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = [0] * (n + 1)
    ans[0] = 1
    for i in range(n + 1):
        if ans[i] == 0:
            continue
        for j in range(m):
            if i + a[j] <= n:
                ans[i + a[j]] = max(ans[i + a[j]], ans[i] * 10 + a[j])
    print(ans[n])

=======
Suggestion 10

def matchstick(N, M, A):
    #dp[i] = matchstick i can be made by the largest integer
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + match[a] <= N:
                dp[i + match[a]] = max(dp[i + match[a]], dp[i] * 10 + a)
    return dp[N]
