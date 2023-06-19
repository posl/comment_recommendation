Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(M):
        sum += (i+1)*A[i]
    max = sum
    for i in range(M,N):
        sum += (i+1)*A[i] - (i-M+1)*A[i-M]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    print(b)
    print(max(b[i+j]-b[i]+a[i]*(j+1) for i in range(n-m+1) for j in range(m)))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, M, A)
    # print(len(A))
    max_sum = 0
    for i in range(0, len(A)-M+1):
        # print(i)
        # print(A[i:i+M])
        sum = 0
        for j in range(0, M):
            sum += (j+1) * A[i+j]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]
    for i in range(n):
        b.append(b[i]+a[i])
    print(b)
    ans = -float("inf")
    for i in range(m,n+1):
        ans = max(ans,b[i]-b[i-m])
    print(ans)

=======
Suggestion 5

def solve(n, m, a):
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    from collections import deque
    q = deque()
    q.append(0)
    ans = -10**18
    for i in range(1, n + 1):
        if q[0] < i - m:
            q.popleft()
        ans = max(ans, s[i] - s[q[0]] - (i - q[0]) * m)
        while q and s[q[-1]] >= s[i] - i * m:
            q.pop()
        q.append(i)
    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 6

def solve(n, m, a):
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = max(c[i], b[i + 1])
    d = [0] * (n + 1)
    for i in range(n):
        d[i + 1] = max(d[i], c[i + 1] + b[i + 1])
    res = 0
    for i in range(1, m + 1):
        res = max(res, d[i] + b[i])
    return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 7

def solve(n, m, a):
    #print(n, m, a)
    ans = 0
    for i in range(m):
        ans += (i+1) * a[i]
    #print(ans)
    tmp = ans
    for i in range(m, n):
        tmp = tmp + (i+1) * a[i] - (i-m+1) * a[i-m]
        ans = max(ans, tmp)
        #print(tmp)
    return ans

=======
Suggestion 8

def solve(n, m, A):
    B = [0] * n
    for i in range(n - 1):
        if A[i + 1] > A[i]:
            B[i] = 1
        elif A[i + 1] < A[i]:
            B[i] = -1

    print(B)

    if m == 1:
        return max(A)

    if m == 2:
        return max(A[0] + 2 * A[1], 2 * A[0] + A[1])

    dp = [0] * n
    dp[0] = 0
    dp[1] = max(0, B[0] + 2 * B[1])
    for i in range(2, n):
        dp[i] = max(0, dp[i - 2] + B[i - 1] + 2 * B[i], dp[i - 1] + B[i] + 2 * B[i - 1])

    print(dp)

    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, sum([j * B[i + j] for j in range(m)]))

    return ans

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]
    for i in range(n):
        b.append(b[i]+a[i])
    maxv = -float('inf')
    for i in range(n-m+1):
        maxv = max(maxv,b[i+m]-b[i])
    print(maxv)

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] == 0:
            a[i] = -1
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    from collections import deque
    q = deque()
    ans = -10**18
    for i in range(n+1):
        while q and s[q[-1]] >= s[i]:
            q.pop()
        q.append(i)
        if i >= m:
            ans = max(ans,s[i] - s[q.popleft()])
    print(ans)
solve()
