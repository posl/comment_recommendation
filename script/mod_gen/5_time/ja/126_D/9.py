def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u-1, v-1, w))
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    color = [-1]*n
    color[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if color[v] != -1:
                continue
            color[v] = 1-color[u] if w%2 else color[u]
            stack.append(v)
    print(*color, sep='\n')

if __name__ == '__main__':
    main()