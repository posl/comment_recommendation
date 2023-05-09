def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)
    seen = [False] * n
    count = 0
    for v in range(n):
        if seen[v]:
            continue
        dfs(v)
        count += 1
    print(count)
main()

if __name__ == '__main__':
    main()