def main():
    # 读入数据
    n, m = map(int, input().split())
    # 读入道路
    road = []
    for i in range(m):
        road.append(list(map(int, input().split())))
    # print(road)
    # 建立邻接矩阵
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in road:
        matrix[i[0]-1][i[1]-1] = 1
    # print(matrix)
    # 遍历邻接矩阵
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1:
                        if matrix[k][i] == 1:
                            count += 1
    print(count)
