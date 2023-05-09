def main():
    # input
    N, M = map(int, input().split())
    uvs = [[*map(int, input().split())] for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    for uv in uvs:
        graph[uv[0]].append(uv[1])
        graph[uv[1]].append(uv[0])
    # print(graph)
    # compute
    visited = [False] * (N+1)
    visited[0] = True
    ans = 0
    for i in range(1, N+1):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            now = stack.pop()
            if visited[now]:
                continue
            visited[now] = True
            for j in graph[now]:
                stack.append(j)
    # output
    print(ans)

if __name__ == '__main__':
    main()