def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    #print(edges)
    # 隣接リスト
    adj = [[] for _ in range(n+1)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2]])
        adj[edge[1]].append([edge[0], edge[2]])
    #print(adj)
    # DFS
    color = [None] * (n+1)
    stack = [1]
    color[1] = 0
    while len(stack) > 0:
        u = stack.pop()
        for v, w in adj[u]:
            if color[v] is None:
                color[v] = (color[u] + w) % 2
                stack.append(v)
    #print(color)
    for i in range(1, n+1):
        print(color[i])
