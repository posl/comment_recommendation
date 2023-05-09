def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1]*N
    dist[X] = 0
    stack = [X]
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if dist[w] == -1:
                dist[w] = dist[v]+1
                stack.append(w)
    ans = [0]*N
    for i in range(N):
        if i == X or i == Y:
            continue
        if dist[i] == -1:
            continue
        ans[dist[i]] += 1
    for i in range(1, N):
        if ans[i] > 0:
            print(i, ans[i])
main()

if __name__ == '__main__':
    main()