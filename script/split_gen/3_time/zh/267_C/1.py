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
