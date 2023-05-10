def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                stack.append(u)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (dist[c] + dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')
    return
