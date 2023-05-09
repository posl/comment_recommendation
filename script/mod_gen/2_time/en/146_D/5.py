def main():
    N = int(input())
    edges = []
    for i in range(N - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    #print(edges)
    #print(N)
    #make a graph
    graph = [[] for i in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    #make a tree
    visited = [False] * (N + 1)
    visited[1] = True
    stack = [1]
    tree = [[] for i in range(N + 1)]
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                tree[v].append(i)
                stack.append(i)
                visited[i] = True
    #print(tree)
    #make a color
    color = [-1] * (N + 1)
    color[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        c = 0
        for i in tree[v]:
            if c == color[v]:
                c += 1
            color[i] = c
            c += 1
            stack.append(i)
    #print(color)
    #print
    print(max(color))
    for i in range(N - 1):
        a, b = edges[i]
        if color[a] > color[b]:
            print(color[b] + 1)
        else:
            print(color[a] + 1)

if __name__ == '__main__':
    main()