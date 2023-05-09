def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(tuple(map(int, input().split())))
    adj = [[] for _ in range(n+1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    colors = [None] * (n+1)
    colors[1] = 0
    stack = [1]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if colors[v] is None:
                colors[v] = (colors[u] + w) % 2
                stack.append(v)
    print('
'.join(map(str, colors[1:])))
