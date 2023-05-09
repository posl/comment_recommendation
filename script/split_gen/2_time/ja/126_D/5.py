def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))
    #print(G)
    color = [-1] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        v, c = stack.pop()
        for nv, w in G[v]:
            if color[nv] == -1:
                color[nv] = (c + w) % 2
                stack.append((nv, color[nv]))
    for c in color:
        print(c)
