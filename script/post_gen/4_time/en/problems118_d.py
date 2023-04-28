Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] < 0:
            continue
        for j in a:
            dp[i + j] = max(dp[i + j], dp[i] * 10 + j)
    print(dp[n])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i - A[j] >= 0:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)
    ans = [0] * dp[N]
    for i in range(dp[N]):
        for j in range(M):
            if N - A[j] >= 0 and dp[N - A[j]] == dp[N] - i - 1:
                ans[i] = str(A[j])
                N -= A[j]
                break
    print(''.join(ans))

=======
Suggestion 3

def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i - a[j] >= 0 and dp[i - a[j]] != -1:
                dp[i] = max(dp[i], dp[i - a[j]] + 1)
    ans = []
    while n > 0:
        for j in range(m):
            if n - a[j] >= 0 and dp[n - a[j]] == dp[n] - 1:
                ans.append(a[j])
                n -= a[j]
                break
    return ''.join(map(str, ans))

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in a:
            if i - j >= 0 and dp[i - j] != -1:
                dp[i] = max(dp[i], dp[i - j] * 10 + j)
    print(dp[n])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N):
        for a in A:
            if i + a <= N:
                dp[i+a] = max(dp[i+a], dp[i] * 10 + a)
    print(dp[N])

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(m):
            if i - a[j] >= 0 and dp[i-a[j]] != -1:
                dp[i] = max(dp[i], dp[i-a[j]]*10 + a[j])
    print(dp[n])

solve()

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + a > N:
                continue
            dp[i+a] = max(dp[i+a],dp[i]+1)
    ans = ''
    for i in range(dp[N]):
        for a in A:
            if N - a < 0:
                continue
            if dp[N-a] == dp[N] - i - 1:
                ans += str(a)
                N -= a
                break
    print(ans)

=======
Suggestion 8

def solve(n, m, a):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in a:
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] * 10 + j)
    return dp[n]

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [0] * (N+1)
    for i in range(N+1):
        if i == 0:
            dp[i] = 0
        else:
            for j in range(M):
                if i - A[j] < 0:
                    continue
                dp[i] = max(dp[i], dp[i-A[j]]*10 + A[j])
    print(dp[N])

=======
Suggestion 10

def main():
    # Get input here
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    # Calculate result here
    # Print output here
    print(n, m, a)
