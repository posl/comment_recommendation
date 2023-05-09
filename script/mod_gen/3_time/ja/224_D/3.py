def main():
    M = int(input())
    G = [[False]*9 for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1][v-1] = True
        G[v-1][u-1] = True
    p = list(map(int, input().split()))
    for i in range(8):
        G[i][p[i]-1] = True
        G[p[i]-1][i] = True
    def bfs(s, t):
        dist = [-1]*9
        dist[s] = 0
        que = [s]
        while que:
            v = que.pop()
            for i in range(9):
                if G[v][i] and dist[i] == -1:
                    dist[i] = dist[v] + 1
                    que.append(i)
        return dist[t]
    def dfs(v, s, d, c):
        if v == 8:
            if s == d:
                return c
            else:
                return 10**9
        r = 10**9
        for i in range(9):
            if G[v][i] and i != s:
                r = min(r, dfs(v+1, i, d, c+bfs(s, i)))
        return r
    r = 10**9
    for i in range(9):
        r = min(r, dfs(0, i, i, 0))
    print(-1 if r == 10**9 else r)

if __name__ == '__main__':
    main()