def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    #print(edges)
    g = [[] for _ in range(n+1)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    #print(g)
    color = [0] * (n+1)
    color[1] = 0
    q = [1]
    while len(q) > 0:
        u = q.pop()
        for v, w in g[u]:
            if color[v] == 0:
                if w % 2 == 0:
                    color[v] = color[u]
                else:
                    color[v] = 1 - color[u]
                q.append(v)
    for i in range(1, n+1):
        print(color[i])
main()

if __name__ == '__main__':
    main()