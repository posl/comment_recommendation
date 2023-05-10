def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    graph = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(v, p):
        c = 1
        for u in graph[v]:
            if u == p:
                continue
            if c == color[p]:
                c += 1
            color[u] = c
            c += 1
            dfs(u, v)
    
    color = [0] * n
    color[0] = 1
    dfs(0, -1)
    
    print(max(color))
    for a, b in edges:
        print(color[b-1])

if __name__ == '__main__':
    solve()