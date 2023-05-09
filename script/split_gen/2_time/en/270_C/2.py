def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        v = q.pop()
        for nv in edges[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])
