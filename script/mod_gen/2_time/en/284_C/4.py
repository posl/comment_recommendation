def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for u in graph[v]:
                if visited[u]:
                    continue
                visited[u] = True
                stack.append(u)
    print(ans)

if __name__ == '__main__':
    main()