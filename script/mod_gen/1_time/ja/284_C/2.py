def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)
    seen = [False] * N
    count = 0
    for i in range(N):
        if seen[i]:
            continue
        dfs(i)
        count += 1
    print(count)

if __name__ == '__main__':
    main()