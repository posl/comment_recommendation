def main():
    N, M = map(int, input().split())
    if N <= 0 or M <= 0:
        print('N or M is not in limit')
        return
    if N > 400 or M > 1000000:
        print('N or M is not in limit')
        return
    # 棋盘
    chess = [[0 for x in range(N)] for y in range(N)]
    # 起始位置
    chess[0][0] = 1
    # 棋子位置
    x = 0
    y = 0
    # 棋子移动
    while x < N:
        while y < N:
            # 棋子移动到(x, y)的距离
            distance = (x * x + y * y) ** 0.5
            # 棋子移动到(x, y)的距离正好是(M)^(1/2)的那个方格
            if distance == M ** 0.5:
                chess[x][y] = 1
            y += 1
        x += 1
        y = 0
    # 棋子移动的最小操作数
    for i in range(N):
        for j in range(N):
            if chess[i][j] == 0:
                # 棋子不能到达(i, j)
                chess[i][j] = -1
            elif chess[i][j] == 1:
                # 棋子可以到达(i, j)
                chess[i][j] = i + j
    # 打印棋子移动的最小操作数
    for i in range(N):
        for j in range(N):
            print(chess[i][j], end=' ')
        print()
