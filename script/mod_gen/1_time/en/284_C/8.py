def main():
    N, M = map(int, input().split())
    #print(N, M)
    graph = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)
    visited = [False] * (N+1)
    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            ans += 1
            stack = [i]
            while stack:
                v = stack.pop()
                if visited[v]:
                    continue
                visited[v] = True
                for w in graph[v]:
                    if not visited[w]:
                        stack.append(w)
    print(ans)

if __name__ == '__main__':
    main()