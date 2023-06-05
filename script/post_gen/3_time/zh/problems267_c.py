Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[:m])
    ans = s
    for i in range(n - m):
        s += a[i + m] - a[i]
        ans = max(ans, s)
    for i in range(m):
        s += a[i + n - m] - a[i]
        ans = max(ans, s)
    print(ans)

=======
Suggestion 2

def solve(n, m, a):
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [0] * (n + 1)
    for i in range(n):
        t[i + 1] = t[i] + i * a[i]
    from collections import deque
    q = deque()
    q.append(0)
    res = -float('inf')
    for j in range(1, n + 1):
        while q and t[q[0]] > t[j]:
            q.popleft()
        if q:
            res = max(res, t[j] - t[q[0]] + (s[j] - s[q[0]]) * (m + 1))
        while q and t[j] <= t[q[-1]]:
            q.pop()
        q.append(j)
    return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 3

def solve(n, m, a):
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最大
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最大
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最大
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最大
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最大
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最小
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最小值最大
    # 从a中选出m个数，使得sum_{i=1}^{M} i × B_i的最大值最大
    # 从a中选出m个数，使得sum_{i

=======
Suggestion 4

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1]+a[i])
    from collections import deque
    q = deque()
    q.append((0,0))
    res = -float("inf")
    for i in range(1,n+1):
        while q and q[0][0] < i-m:
            q.popleft()
        res = max(res,s[i]-q[0][1])
        while q and q[-1][1] >= s[i]:
            q.pop()
        q.append((i,s[i]))
    print(res)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] >= 0:
            ans += a[i]
            a[i] = 0
    a.sort()
    a.reverse()
    for i in range(m):
        if a[i] < 0:
            ans -= a[i]
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    for i in range(n):
        a[i+1] += a[i]
    ans = -10**10
    for i in range(n-m+1):
        ans = max(ans,a[i+m]-a[i])
    for i in range(1,m+1):
        ans += i*a[i]
    print(ans)

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    # print(A)
    # print(A[0:M])
    # print(sum([i*A[i] for i in range(M)]))
    # print(sum([i*A[i] for i in range(M,N)]))
    ans = sum([i*A[i] for i in range(M)])
    tmp = ans
    for i in range(M,N):
        tmp += (i+1)*A[i] - sum([j*A[j] for j in range(i-M+1,i)])
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans,sum([(i+1)*j for i,j in enumerate(a[i:i+m])]))
    print(ans)

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = dp[i][0] + a[i]
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j-1] + a[i-1] * j
    ans = 0
    for i in range(m+1):
        ans = max(ans,dp[n][i])
    print(ans)
solve()
