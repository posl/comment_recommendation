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
