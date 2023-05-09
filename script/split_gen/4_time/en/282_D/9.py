def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    # 1. Create an adjacency list
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge[0] - 1, edge[1] - 1
        adj_list[u].append(v)
        adj_list[v].append(u)
    # 2. Find the connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        component = [i]
        queue = [i]
        while queue:
            node = queue.pop()
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    component.append(neighbor)
                    queue.append(neighbor)
        components.append(component)
    # 3. Count the number of edges that connect different components
    ans = 0
    for component in components:
        num_nodes = len(component)
        num_edges = 0
        for node in component:
            num_edges += len(adj_list[node])
        num_edges //= 2
        num_internal_edges = num_edges - (num_nodes - 1)
        num_external_edges = num_nodes * (num_nodes - 1) // 2 - num_internal_edges
        ans += num_external_edges
    print(ans)
