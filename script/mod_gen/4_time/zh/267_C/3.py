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

if __name__ == '__main__':
    solve()