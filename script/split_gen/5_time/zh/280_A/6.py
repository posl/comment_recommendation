def main():
    #读取行数和列数
    line = input().split()
    row = int(line[0])
    column = int(line[1])
    #读取棋盘状态，用二维数组存储
    chessboard = [[0 for i in range(column)] for j in range(row)]
    for i in range(row):
        line = input()
        for j in range(column):
            if line[j] == '#':
                chessboard[i][j] = 1
    #计算棋盘上的棋子数
    sum = 0
    for i in range(row):
        for j in range(column):
            sum += chessboard[i][j]
    print(sum)
