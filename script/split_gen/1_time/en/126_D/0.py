def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [-1] * N
    color[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for u, w in G[v]:
            if color[u] == -1:
                color[u] = color[v] + w
                q.append(u)
    for c in color:
        print(c % 2)
