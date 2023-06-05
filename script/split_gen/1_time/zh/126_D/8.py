def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    tree = [[] for i in range(n + 1)]
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    color = [-1] * (n + 1)
    color[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u in tree[v]:
            if color[u] == -1:
                color[u] = color[v] ^ 1
                stack.append(u)
    for v in range(1, n + 1):
        print(color[v])
