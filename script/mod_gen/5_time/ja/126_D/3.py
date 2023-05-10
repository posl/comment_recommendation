def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    ans = [0] * n
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    def dfs(v, p, d):
        ans[v] = d % 2
        for u, w in graph[v]:
            if u == p:
                continue
            dfs(u, v, d+w)
    dfs(0, -1, 0)
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()