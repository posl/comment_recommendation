Synthesizing 10/10 solutions

=======
Suggestion 1

def problem275_c():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())

    # 计算
    count = 0
    for r in range(9):
        for c in range(9):
            if s[r][c] == '#':
                if r + 1 < 9 and c + 1 < 9:
                    if s[r][c + 1] == '#' and s[r + 1][c] == '#' and s[r + 1][c + 1] == '#':
                        count += 1

    # 输出
    print(count)

=======
Suggestion 2

def main():
    s = []
    for i in range(9):
        s.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    s = []
    for i in range(9):
        s.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if s[i+1][j] == '#' and s[i][j+1] == '#' and s[i+1][j+1] == '#':
                        cnt += 1
    print(cnt)

=======
Suggestion 4

def get_square_count(S):
    count = 0
    for r in range(1, 8):
        for c in range(1, 8):
            if S[r][c] == "#" and S[r-1][c-1] == "#" and S[r-1][c] == "#" and S[r][c-1] == "#":
                count += 1
    return count

=======
Suggestion 5

def get_square_count():
    chessboard = []
    for i in range(9):
        chessboard.append(input())
    count = 0
    for r in range(8):
        for c in range(8):
            if chessboard[r][c] == '#' and chessboard[r][c+1] == '#' and chessboard[r+1][c] == '#' and chessboard[r+1][c+1] == '#':
                count += 1
    print(count)

get_square_count()

=======
Suggestion 6

def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())
    # 统计
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i == 0 or j == 0:
                    continue
                if s[i - 1][j - 1] == '#' and s[i - 1][j] == '#' and s[i][j - 1] == '#':
                    ans += 1
    # 输出
    print(ans)

=======
Suggestion 7

def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())
    # 计算
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i >= 1 and j >= 1 and s[i - 1][j - 1] == '#':
                    if j >= 2 and s[i][j - 2] == '#':
                        count += 1
                    if i >= 2 and s[i - 2][j] == '#':
                        count += 1
                if i >= 1 and j <= 7 and s[i - 1][j + 1] == '#':
                    if j <= 6 and s[i][j + 2] == '#':
                        count += 1
                    if i >= 2 and s[i - 2][j] == '#':
                        count += 1
                if i <= 7 and j >= 1 and s[i + 1][j - 1] == '#':
                    if j >= 2 and s[i][j - 2] == '#':
                        count += 1
                    if i <= 6 and s[i + 2][j] == '#':
                        count += 1
                if i <= 7 and j <= 7 and s[i + 1][j + 1] == '#':
                    if j <= 6 and s[i][j + 2] == '#':
                        count += 1
                    if i <= 6 and s[i + 2][j] == '#':
                        count += 1
    # 打印输出
    print(count)

=======
Suggestion 8

def get_num_of_square(S):
    count = 0
    for r in range(1, 9):
        for c in range(1, 9):
            if S[r][c] == '#':
                if S[r - 1][c - 1] == '#' and S[r - 1][c] == '#' and S[r][c - 1] == '#':
                    count += 1
    return count

=======
Suggestion 9

def main():
    board = [input() for _ in range(9)]
    count = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '#':
                count += 1
    print(count)

=======
Suggestion 10

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
