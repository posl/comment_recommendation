def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [False] * N
    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if visited[i]:
                continue
            dfs(i)
    cnt = 0
    for i in range(N):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()