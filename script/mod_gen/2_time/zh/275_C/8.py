def getSquareCount():
    # 读取输入
    squares = []
    for i in range(9):
        squares.append(input())
    # 找到所有可能的正方形
    squarePoints = []
    for r in range(8):
        for c in range(8):
            if squares[r][c] == '#':
                squarePoints.append((r, c))
    # 计算所有可能的正方形的顶点
    squareVertexes = []
    for point in squarePoints:
        squareVertexes.append((point[0], point[1], point[0], point[1] + 1))
        squareVertexes.append((point[0], point[1], point[0] + 1, point[1]))
        squareVertexes.append((point[0], point[1] + 1, point[0] + 1, point[1] + 1))
        squareVertexes.append((point[0] + 1, point[1], point[0] + 1, point[1] + 1))
    # 计算所有可能的正方形的顶点是否都在棋盘上
    count = 0
    for vertex in squareVertexes:
        if vertex[0] >= 0 and vertex[0] <= 8 and vertex[1] >= 0 and vertex[1] <= 8 and vertex[2] >= 0 and vertex[2] <= 8 and vertex[3] >= 0 and vertex[3] <= 8:
            count += 1
    # 返回结果
    return count

if __name__ == '__main__':
    getSquareCount()