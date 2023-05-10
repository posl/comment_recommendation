def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    dist = [N] * N
    dist[X] = 0
    que = [X]
    while que:
        q = que.pop()
        for v in G[q]:
            if dist[v] > dist[q] + 1:
                dist[v] = dist[q] + 1
                que.append(v)
    print(dist[Y])
