def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    #print(G)
    color = [-1] * N
    def dfs(v, p, c):
        color[v] = c
        c = 1
        for u in G[v]:
            if u == p:
                continue
            if c == color[v]:
                c += 1
            dfs(u, v, c)
            c += 1
    dfs(0, -1, 1)
    print(max(color))
    for c in color[1:]:
        print(c)
