def main():
    N, Q = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    def dfs(v, p, d):
        depth[v] = d
        for u in edges[v]:
            if u != p:
                dfs(u, v, d+1)
    depth = [0] * N
    dfs(0, -1, 0)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (depth[c-1] + depth[d-1]) % 2 == 0:
            print('Town')
        else:
            print('Road')
