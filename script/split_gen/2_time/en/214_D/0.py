def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    d = [0] * N
    q = [0]
    while q:
        v = q.pop()
        for u, w in G[v]:
            if d[u] == 0:
                d[u] = d[v] + w
                q.append(u)
    print(sum(d))
