Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i - a[j] >= 0 and dp[i - a[j]] >= 0:
                dp[i] = max(dp[i], dp[i - a[j]] + 1)
    ans = []
    while n > 0:
        for i in range(m):
            if n - a[i] >= 0 and dp[n - a[i]] == dp[n] - 1:
                ans.append(a[i])
                n -= a[i]
                break
    print(''.join(map(str, ans)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for a in A:
            if i - a >= 0:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[N])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0 and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] + 1)
    ans = []
    i = N
    while i > 0:
        for a in A:
            if i - a >= 0 and dp[i - a] == dp[i] - 1:
                ans.append(a)
                i -= a
                break
    print(''.join(map(str, ans)))

=======
Suggestion 4

def solve(n, m, a):
    dp = [-float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i - a[j][1] >= 0:
                dp[i] = max(dp[i], dp[i - a[j][1]] + a[j][0])
    return dp[-1]

n, m = map(int, input().split())
a = []
for i, v in enumerate(map(int, input().split())):
    a.append((v, i + 1))
a.sort(reverse=True)
print(solve(n, m, a))

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    dp = [-1]*(N+1)
    dp[0] = 0
    for i in range(1,N+1):
        for j in range(M):
            if i-A[j] >= 0:
                dp[i] = max(dp[i],dp[i-A[j]]+1)
    s = ''
    i = N
    while i > 0:
        for j in range(M):
            if i-A[j] >= 0 and dp[i-A[j]] == dp[i]-1:
                s += str(A[j])
                i -= A[j]
                break
    print(s)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i], dp[i-a[j]]*10 + a[j])

    print(dp[n])

=======
Suggestion 7

def solve(N, M, A):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for a in A:
            if i >= a:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    return dp[N]

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))

=======
Suggestion 8

def solve(n, m, a):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        if dp[i] < 0:
            continue
        for j in a:
            dp[i + j] = max(dp[i] * 10 + j, dp[i + j])
    return dp[n]

=======
Suggestion 9

def largest_integer(n,m,a):
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i >= a[j] and dp[i-a[j]] >= 0:
                dp[i] = max(dp[i], dp[i-a[j]]*10+j+1)
    return dp[n]

=======
Suggestion 10

def solve(N, M, A):
    # dp[i] := ちょうどi本のマッチを使って作れる最大の整数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0 and dp[i - a] != -1:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    return dp[N]
