def main():
    N, X, Y = map(int, input().split())
    # 1. 生成邻接矩阵
    # 2. 求最短路径
    # 3. 统计路径长度
    # 1. 生成邻接矩阵
    # 1.1 初始化邻接矩阵
    adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
    # 1.2 生成邻接矩阵
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            else:
                if j == i + 1:
                    adj_matrix[i][j] = 1
                else:
                    adj_matrix[i][j] = abs(i - j)
    # 2. 求最短路径
    # 2.1 初始化最短路径矩阵
    shortest_path_matrix = [[0 for _ in range(N)] for _ in range(N)]
    # 2.2 生成最短路径矩阵
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            else:
                shortest_path_matrix[i][j] = shortest_path_matrix[j][i] = shortest_path(adj_matrix, i, j)
    # 3. 统计路径长度
    # 3.1 初始化路径长度统计矩阵
    shortest_path_count_matrix = [0 for _ in range(N)]
    # 3.2 统计路径长度
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            else:
                shortest_path_count_matrix[shortest_path_matrix[i][j]] += 1
    # 4. 输出结果
    for k in range(1, N):
        print(shortest_path_count_matrix[k])
    return
