def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = [[a - 1, b - 1] for a, b in ab]
    graph = [[] for _ in range(N)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                stack.append(nv)
    if -1 in dist[1:]:
        print("No")
        return
    ans = [-1] * N
    for i, d in enumerate(dist):
        if d == 1:
            ans[i] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if ans[nv] == -1:
                ans[nv] = v
                stack.append(nv)
    print("Yes")
    for a in ans[1:]:
        print(a + 1)
main()
