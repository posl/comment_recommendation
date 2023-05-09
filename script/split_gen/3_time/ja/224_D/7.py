def main():
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    points = list(map(int, input().split()))
    points = [p-1 for p in points]
    #print(edges)
    #print(points)
    #print(points)
    #print(M, edges, points)
    # 隣接行列を作る
    board = [[0 for i in range(9)] for j in range(9)]
    for edge in edges:
        board[edge[0]-1][edge[1]-1] = 1
        board[edge[1]-1][edge[0]-1] = 1
    #print(board)
    # 空の頂点を探す
    empty = 0
    for i in range(9):
        if i not in points:
            empty = i
    #print(empty)
    # 空の頂点に隣接する頂点を探す
    adj = []
    for i in range(9):
        if board[empty][i] == 1:
            adj.append(i)
    #print(adj)
    # 空の頂点に隣接する頂点に置かれたコマを探す
    adj_points = []
    for i in range(8):
        if points[i] in adj:
            adj_points.append(i)
    #print(adj_points)
    # コマの移動
    for i in range(8):
        for j in range(8):
            if points[i] == adj[j]:
                points[i], points[adj_points[j]] = points[adj_points[j]], points[i]
    #print(points)
    # 完成かどうか判定
    if points == [0, 1, 2, 3, 4, 5, 6, 7]:
        print(0)
    else:
        print(-1)
