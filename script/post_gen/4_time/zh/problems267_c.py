Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 初始化
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]

    # 解决
    ans = -10 ** 18
    for i in range(m, n + 1):
        ans = max(ans, b[i] - b[i - m])
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        ans += (i + 1) * a[i]
    tmp = ans
    for i in range(m, n):
        tmp += (i + 1) * a[i] - (i - m + 1) * a[i - m]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def max_sum(n, m, a):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i - 1] + a[i - 1]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i >= m:
            dp[i] = max(dp[i - 1], res[i] - res[i - m])
    return dp[n]

=======
Suggestion 4

def solve(n, m, a):
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    from collections import deque
    q = deque()
    ans = -float('inf')
    for i in range(n + 1):
        while q and q[0][1] < i - m:
            q.popleft()
        if q:
            ans = max(ans, s[i] - q[0][0] - i * m)
        while q and q[-1][0] >= s[i] - i * m:
            q.pop()
        q.append((s[i] - i * m, i))
    return ans

=======
Suggestion 5

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 计算前缀和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 计算答案
    ans = -(10 ** 18)
    for i in range(1, n + 1):
        if i - m >= 0:
            ans = max(ans, s[i] - s[i - m])
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[:m])
    t = sum([i*a[i] for i in range(m)])
    ans = t
    for i in range(m,n):
        t += (m-1)*a[i] - 2*s + a[i-m]
        ans = max(ans, t)
        s += a[i] - a[i-m]
    print(ans)

main()

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(1,m+1):
        ans += i*a[i-1]
    tmp = ans
    for i in range(m,n):
        tmp += (i+1)*a[i]
        tmp -= (i-m+1)*a[i-m]
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, A[i + M] - A[i] + sum(range(1, M + 1)) * A[i])
    print(ans)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    res = -10**10
    for i in range(m, n+1):
        res = max(res, s[i] - s[i-m])
    print(res)

=======
Suggestion 10

def resolve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] * (i + 1)
    ans = sum
    for i in range(m):
        sum -= a[n - 1 - i] * (n - i)
        sum += a[i] * (n - i)
        ans = max(ans, sum)
    print(ans)
