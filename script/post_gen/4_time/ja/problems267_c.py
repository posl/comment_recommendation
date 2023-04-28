Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = -10 ** 18
    for i in range(1, n - m + 2):
        ans = max(ans, s[i + m - 1] - s[i - 1] + sum(range(m)))
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    ans = -10**18
    for i in range(n-m+1):
        ans = max(ans, s[i+m]-s[i])
    for i in range(n-m+1):
        ans = max(ans, s[i+m]-s[i]-i)
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    ans = -float('inf')
    for i in range(N - M + 1):
        ans = max(ans, B[i + M] - B[i])
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    c = [0] * (n+1)
    d = 0
    for i in range(n):
        d = max(d, b[i+1])
        c[i+1] = d
    e = [0] * (n+1)
    f = 0
    for i in range(n+1):
        f = max(f, b[i])
        e[i] = f

    ans = 0
    for i in range(1, n+1):
        if i >= m:
            ans = max(ans, c[i-m] + e[i])
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    C = [0] * (N + 1)
    for i in range(N + 1):
        C[i] = B[i] - i
    from collections import deque
    Q = deque()
    ans = -float("inf")
    for i in range(N + 1):
        while Q and Q[0][0] < i - M:
            Q.popleft()
        while Q and Q[-1][1] >= C[i]:
            Q.pop()
        Q.append((i, C[i]))
        ans = max(ans, C[i] - Q[0][1])
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    c = [0] * (n+1)
    for i in range(n+1):
        c[i] = b[i] - i
    from collections import deque
    q = deque()
    ans = 0
    for i in range(n+1):
        while q and c[q[-1]] >= c[i]:
            q.pop()
        q.append(i)
        if q[0] == i - m:
            q.popleft()
        ans = max(ans, c[i] - c[q[0]])
    print(ans)
main()

=======
Suggestion 7

def solve(n, m, a):
    a = [0] + a
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i + 1]
    ans = -10 ** 18
    for i in range(n - m + 1):
        ans = max(ans, s[i + m] - s[i] + sum(a[i + 1:i + m + 1]) + m * (m + 1) // 2)
    return ans

=======
Suggestion 8

def solve(n, m, a):
    a.sort()
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    l = 0
    r = 2 * 10 ** 5 + 1
    while r - l > 1:
        x = (l + r) // 2
        cnt = 0
        for i in range(n):
            cnt += n - bisect.bisect_left(a, x - a[i])
        if cnt >= m:
            l = x
        else:
            r = x
    ans = 0
    cnt = 0
    for i in range(n):
        idx = bisect.bisect_left(a, l - a[i])
        cnt += n - idx
        ans += b[n] - b[idx] + a[i] * (n - idx)
    ans += (m - cnt) * l
    return ans

import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [0] + a
    #print(n,m)
    #print(a)
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i+1]
    #print(s)
    ans = -10 ** 9
    for i in range(n-m+1):
        ans = max(ans,s[i+m] - s[i])
    print(ans)

=======
Suggestion 10

def max_sum(n, m, a):
    sums = [0] * (n+1)
    for i in range(n):
        sums[i+1] = sums[i] + a[i]

    maxs = 0
    for i in range(n-m+1):
        maxs = max(maxs, sums[i+m] - sums[i] + (m*(m+1)//2))

    return maxs
