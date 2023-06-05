def main():
    n,x,y = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    parent = [0]*(n+1)
    parent[x] = -1
    stack = [x]
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if parent[child] == 0:
                parent[child] = node
                stack.append(child)
    path = []
    node = y
    while node != -1:
        path.append(node)
        node = parent[node]
    print(*path[::-1])
