Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i], dp[i - a[j]] * 10 + a[j])
    print(dp[n])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(m):
            dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    print(dp[n])

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for a in A:
            if i - a >= 0:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    print(dp[N])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for a in A:
            if i - a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a]*10+a)
    print(dp[N])

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(n+1):
        if dp[i] != -1:
            for j in a:
                dp[i+j] = max(dp[i+j],dp[i]*10+j)
    print(dp[n])

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        if dp[i] == -1:
            continue
        for j in range(m):
            if i+a[j] <= n:
                dp[i+a[j]] = max(dp[i+a[j]],dp[i]*10+j+1)
    print(dp[n])

=======
Suggestion 7

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    match = [2,5,5,4,5,6,3,7,6]
    a.sort(reverse=True)
    dp = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(m):
            if i-match[a[j]-1] >= 0:
                dp[i] = max(dp[i-match[a[j]-1]]*10+a[j],dp[i])
    print(dp[n])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    A = sorted(A, reverse=True)
    #print(A)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in range(M):
            if i - match[A[j]-1] >= 0:
                dp[i] = max(dp[i], dp[i-match[A[j]-1]]*10+A[j])
    #print(dp)
    print(dp[N])

=======
Suggestion 9

def answer(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] < 0:
            continue
        for j in a:
            dp[i + j] = max(dp[i + j], dp[i] * 10 + j)
    return dp[n]

=======
Suggestion 10

def make_num(n, a):
    dp = [0]*(n+1)
    for i in range(n+1):
        for j in a:
            if i+j <= n:
                dp[i+j] = max(dp[i]+1, dp[i+j])
    return dp[n]
