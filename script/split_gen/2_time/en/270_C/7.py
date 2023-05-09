def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        U, V = map(int, input().split())
        U -= 1
        V -= 1
        edges[U].append(V)
        edges[V].append(U)
    dist = [-1] * N
    dist[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for u in edges[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                queue.append(u)
    ans = [0] * N
    for i in range(N):
        if i == X or i == Y:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        if ans[i] == 0:
            continue
        print(i, ans[i])
