def solve():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    def make_graph(AB):
        graph = [[] for _ in range(N)]
        for a, b in AB:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        return graph
    def dfs(graph, v, visited):
        visited[v] = True
        for nv in graph[v]:
            if visited[nv]:
                continue
            dfs(graph, nv, visited)
    def is_connected(graph):
        visited = [False] * N
        dfs(graph, 0, visited)
        return all(visited)
    def solve():
        AB_graph = make_graph(AB)
        CD_graph = make_graph(CD)
        if not is_connected(AB_graph) or not is_connected(CD_graph):
            return False
        AB_degrees = [len(v) for v in AB_graph]
        CD_degrees = [len(v) for v in CD_graph]
        return sorted(AB_degrees) == sorted(CD_degrees)
    if solve():
        print("Yes")
    else:
        print("No")
