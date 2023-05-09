def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1]*N
    dist[X] = 0
    q = [X]
    while q:
        x = q.pop()
        for y in graph[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
    count = [0]*N
    count[0] = N*(N-1)//2
    for d in dist:
        if d != -1:
            count[d] += 1
    print(count[Y])
