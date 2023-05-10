def dfs(node, parent, counters, edges):
    counters[node] += counters[parent]
    for child in edges[node]:
        if child == parent:
            continue
        dfs(child, node, counters, edges)
