def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    ans = [0] * N
    for i in range(N):
        if i == X or i == Y:
            continue
        dist = [-1] * N
        dist[i] = 0
        que = [i]
        while que:
            v = que.pop()
            for nv in graph[v]:
                if dist[nv] != -1:
                    continue
                dist[nv] = dist[v] + 1
                que.append(nv)
        ans[dist[X] + dist[Y] + 1] += 1
    print(*ans[1:])
