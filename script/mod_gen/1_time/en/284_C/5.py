def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [False] * N
    components = 0
    for i in range(N):
        if visited[i]:
            continue
        stack = [i]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    stack.append(w)
        components += 1
    print(components)
main()
