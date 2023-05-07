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
        v = q.pop()
        for to in edge[v]:
            if dist[to] != -1:
                continue
            dist[to] = dist[v] + 1
            q.append(to)
    for i in range(N):
        if i == X:
            continue
        if dist[i] == -1:
            continue
        print(dist[i]//2 + 1, end=" ")
    print()
