def main():
    N = int(input())
    edges = []
    for i in range(N):
        edges.append([int(i) for i in input().split()])
    points = [int(i) for i in input().split()]
    #print(N, edges, points)
    #print(edges)
    #print(points)
    #グラフの作成
    graph = [[0 for i in range(9)] for j in range(9)]
    for i in range(N):
        graph[edges[i][0]-1][edges[i][1]-1] = 1
        graph[edges[i][1]-1][edges[i][0]-1] = 1
    #print(graph)
    #グラフの隣接頂点の作成
    adj = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 1:
                adj[i][j] = 1
                adj[i][points[j-1]-1] = 1
                adj[points[j-1]-1][i] = 1
    #print(adj)
    #グラフの隣接頂点の隣接頂点の作成
    adj2 = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if adj[i][j] == 1:
                for k in range(9):
                    if adj[j][k] == 1:
                        adj2[i][k] = 1
    #print(adj2)
    #グラフの隣接頂点の隣接頂点の隣接頂点の作成
    adj3 = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if adj2[i][j] == 1:
                for k in range(9):
                    if adj[j][k] == 1:
                        adj3[i][k] = 1
    #print(adj3)
    #グラフの隣接頂点の隣接頂点の隣接

if __name__ == '__main__':
    main()