Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    for i in range(m, n + 1):
        ans = max(ans, s[i] - s[i - m])
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [0] * (n + 1)
    for i in range(n):
        t[i + 1] = min(t[i], s[i + 1])
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, s[i] - t[i])
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    max_val = -10**18
    for i in range(M, N+1):
        max_val = max(max_val, A[i] - A[i-M])
    print(max_val)

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*(n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    c = [0]*(n+1)
    for i in range(n):
        if i >= m:
            c[i+1] = max(c[i], b[i+1]-b[i+1-m])
        else:
            c[i+1] = max(c[i], b[i+1])
    ans = 0
    for i in range(n+1):
        if i >= m:
            ans = max(ans, c[i]+b[i]-b[i-m])
        else:
            ans = max(ans, c[i]+b[i])
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    max_sum = 0
    for i in range(n - m + 1):
        sum = 0
        for j in range(m):
            sum += (j + 1) * a[i + j]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if a[i] < 0:
            c += 1
    if m > c:
        a = sorted(a, reverse=True)
        print(sum(a[:m]))
    else:
        a = sorted(a)
        s = 0
        for i in range(m):
            if a[i] < 0:
                s = i
        print(sum(a[s:]))

=======
Suggestion 7

def problem():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i] > 0:
            b.append(a[i])
    b.sort()
    b.reverse()
    ans = 0
    for i in range(m):
        ans += b[i] * (i + 1)
    print(ans)

problem()

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    maxSum = 0
    for i in range(1, N+1):
        maxSum += i * A[i-1]
    print(maxSum)
    return 0

=======
Suggestion 9

def max_subarray(A, M):
    max_val = 0
    for i in range(0,len(A)-M+1):
        max_val = max(max_val, sum([A[i+j]*(j+1) for j in range(0,M)]))
    return max_val

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(max_subarray(A, M))

=======
Suggestion 10

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # dp[i] := Aのi番目までの要素を使って、連続する要素の和の最大値
    dp = [0] * (N + 1)
    for i in range(N):
        dp[i + 1] = max(dp[i] + A[i], A[i])

    # dp[i] := Aのi番目までの要素を使って、連続する要素の和の最大値
    dp2 = [0] * (N + 1)
    for i in range(N):
        dp2[i + 1] = max(dp2[i], dp[i + 1])

    ans = 0
    for i in range(1, N + 1):
        if i - M >= 0:
            ans = max(ans, dp[i] + dp2[i - M])
        else:
            ans = max(ans, dp[i])
    print(ans)
