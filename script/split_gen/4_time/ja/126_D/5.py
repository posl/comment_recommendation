def main():
    N = int(input())
    edges = []
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    #print(edges)
    colors = [-1]*(N+1)
    colors[1] = 0
    #print(colors)
    queue = [1]
    while queue:
        #print(queue)
        now = queue.pop(0)
        for u, v, w in edges:
            if u == now and colors[v] == -1:
                if w % 2 == 0:
                    colors[v] = colors[u]
                else:
                    colors[v] = 1 - colors[u]
                queue.append(v)
            elif v == now and colors[u] == -1:
                if w % 2 == 0:
                    colors[u] = colors[v]
                else:
                    colors[u] = 1 - colors[v]
                queue.append(u)
    for i in range(1, N+1):
        print(colors[i])
