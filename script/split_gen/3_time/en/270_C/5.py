def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    ans = [0] * N
    for i in range(N):
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i] // 2)
