def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            paths += find_all_paths(graph, node, end, path)
    return paths
N,M = map(int,raw_input().split())
graph = {}
for i in range(M):
    u,v = map(int,raw_input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]
cnt = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        paths = find_all_paths(graph, i, j)
        for path in paths:
            if len(path) == 3:
                cnt += 1
print cnt

if __name__ == '__main__':
    find_all_paths()