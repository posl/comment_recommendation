def main():
    n, m = map(int, input().split())
    bridge = []
    for _ in range(m):
        a, b = map(int, input().split())
        bridge.append((a, b))
    bridge.sort()
    # print(bridge)
    bridge_set = set()
    for i in range(m):
        bridge_set.add(bridge[i])
    # print(bridge_set)
    # print(bridge_set)
    def dfs(graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for v in graph[vertex]:
                    stack.append(v)
        return visited
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for i in range(m):
        graph[bridge[i][0]].append(bridge[i][1])
        graph[bridge[i][1]].append(bridge[i][0])
    # print(graph)
    # print(dfs(graph, 1))
    count = 0
    for i in range(1, n + 1):
        if i not in dfs(graph, 1):
            count += 1
    print(count - 1)
    # print(graph)
    # print(dfs(graph, 1))
