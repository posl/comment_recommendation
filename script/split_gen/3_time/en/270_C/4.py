def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    dist = [-1] * N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for nv in edges[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            stack.append(nv)
    ans = [0] * N
    for i in range(N):
        ans[dist[i]] += 1
    print(*ans[1:])
