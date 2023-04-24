Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in a:
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] * 10 + j)
    print(dp[n])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1 for _ in range(N+1)]
    dp[0] = 0
    for i in range(1, N+1):
        for a in A:
            if i - a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a] + 1)
    ans = []
    n = N
    while n > 0:
        for a in A:
            if n - a >= 0 and dp[n-a] == dp[n] - 1:
                ans.append(a)
                n -= a
                break
    print(''.join(map(str, ans)))

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
            if i-a >= 0 and dp[i-a] >= 0:
                dp[i] = max(dp[i], dp[i-a]+1)
    ans = ""
    while N > 0:
        for a in A:
            if N-a >= 0 and dp[N-a] == dp[N]-1:
                ans += str(a)
                N -= a
                break
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(n+1):
        if dp[i] == -1:
            continue
        for j in a:
            if i+j > n:
                continue
            dp[i+j] = max(dp[i+j], dp[i]+1)
    ans = ''
    i = n
    while i > 0:
        for j in a:
            if i-j < 0:
                continue
            if dp[i-j] == dp[i]-1:
                ans += str(j)
                i -= j
                break
    print(ans)

=======
Suggestion 6

def solve(n, m, a):
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i], dp[i-a[j]] * 10 + a[j])
    return dp[-1]

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    matchsticks = [2,5,5,4,5,6,3,7,6]
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + matchsticks[a - 1] > N:
                continue
            dp[i + matchsticks[a - 1]] = max(dp[i + matchsticks[a - 1]], dp[i] * 10 + a)
    print(dp[N])

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i], dp[i - a[j]] * 10 + a[j])
    print(dp[n])

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = dict()
    for i in range(m):
        d[a[i]] = i + 1
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in a:
            if i - d[j] >= 0 and dp[i - d[j]] != -1:
                dp[i] = max(dp[i], dp[i - d[j]] * 10 + j)
    print(dp[n])

=======
Suggestion 10

def get_max_digit(a, m):
    for i in range(m-1, -1, -1):
        if a[i] <= n:
            return a[i]

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.reverse()
