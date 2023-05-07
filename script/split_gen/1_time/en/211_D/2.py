def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    mod = 10**9 + 7
    n, m = map(int, input().split())
    if m == 0:
        print(0)
        return
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    dist = [-1]*n
    dist[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[n-1] == -1:
        print(0)
        return
    dp = [0]*n
    dp[n-1] = 1
    for i in range(n-2, -1, -1):
        for nv in g[i]:
            if dist[nv] == dist[i] + 1:
                dp[i] += dp[nv]
                dp[i] %= mod
    print(dp[0])
