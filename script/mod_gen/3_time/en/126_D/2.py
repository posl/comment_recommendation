def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append([v-1, w])
        G[v-1].append([u-1, w])
    color = [-1]*N
    color[0] = 0
    def dfs(v):
        for nv, w in G[v]:
            if color[nv] == -1:
                color[nv] = (color[v]+w)%2
                dfs(nv)
    dfs(0)
    for i in color:
        print(i)
main()
