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
    dist = [-1] * N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                stack.append(nv)
    ans = [0] * N
    for i in range(N):
        if i == X:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        print(ans[i])

if __name__ == '__main__':
    main()