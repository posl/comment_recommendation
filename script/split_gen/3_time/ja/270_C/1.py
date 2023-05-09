def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    q = [X]
    while q:
        x = q.pop()
        for y in edge[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
    ans = [0] * N
    for i, d in enumerate(dist):
        ans[d] += 1
    for i in range(1, N):
        print(ans[i] // 2)
