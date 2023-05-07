def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [0] * N
    color[0] = 1
    stack = [(0, 0)]
    while stack:
        v, p = stack.pop()
        for nv, w in G[v]:
            if nv == p:
                continue
            color[nv] = color[v] + w % 2
            stack.append((nv, v))
    for c in color:
        print(c % 2)
