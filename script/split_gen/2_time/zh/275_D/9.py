def main():
    # 读取数据
    S = []
    for i in range(9):
        S.append(input())
    #print(S)
    # 画出棋盘
    chessboard = []
    for i in range(9):
        chessboard.append([])
        for j in range(9):
            chessboard[i].append(0)
    #print(chessboard)
    # 统计棋盘上的棋子
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                chessboard[i][j] = 1
    #print(chessboard)
    # 检查棋盘上的正方形
    count = 0
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 1 and chessboard[i+1][j] == 1 and chessboard[i][j+1] == 1 and chessboard[i+1][j+1] == 1:
                count += 1
    print(count)
