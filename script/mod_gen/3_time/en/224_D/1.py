def main():
    M = int(input())
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
        edges.append((v, u))
    pieces = list(map(int, input().split()))
    pieces = [0] + pieces
    pieces = [pieces.index(i) for i in range(1, 9)]
    #print(pieces)
    #print(edges)
    G = [[] for i in range(9)]
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)
    #print(G)
    #print(pieces)
    #print(edges)
    def dfs(v, G, visited):
        visited[v] = True
        for nv in G[v]:
            if visited[nv] == False:
                dfs(nv, G, visited)
    visited = [False] * 9
    dfs(1, G, visited)
    if visited[2] == False or visited[3] == False or visited[9] == False:
        print(-1)
        return
    if pieces[1] != 1 or pieces[2] != 2 or pieces[3] != 3 or pieces[4] != 4 or pieces[5] != 5 or pieces[6] != 6 or pieces[7] != 7 or pieces[8] != 8:
        print(-1)
        return
    #print(pieces)
    def distance(pieces, G):
        dist = [[float("inf")] * 9 for i in range(9)]
        for i in range(9):
            dist[i][i] = 0
        for u, v in edges:
            dist[u][v] = 1
            dist[v][u] = 1
        for k in range(9):
            for i in range(9):
                for j in range(9):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        #print(dist)
        ans = 0
        for i in range(1, 9):
            ans += dist[pieces[i]][pieces[i - 1]]
        return ans
    ans = distance(pieces, G)
    print(ans)

if __name__ == '__main__':
    main()