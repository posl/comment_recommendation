Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i > 0 and j > 0 and S[i-1][j-1] == '#':
                    if i > 0 and S[i-1][j] == '#':
                        if j > 0 and S[i][j-1] == '#':
                            count += 1
    print(count)

=======
Suggestion 2

def main():
    S = []
    for i in range(9):
        S.append(input())
    cnt = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if S[i][j + 1] == '#' and S[i + 1][j] == '#' and S[i + 1][j + 1] == '#':
                        cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    # 读取输入
    input = []
    for i in range(9):
        input.append(input())
    # 遍历每个点，检查是否有四个顶点都有棋子的正方形
    count = 0
    for r in range(9):
        for c in range(9):
            if input[r][c] == "#":
                if r + 1 < 9 and c + 1 < 9 and input[r + 1][c] == "#" and input[r][c + 1] == "#" and input[r + 1][
                    c + 1] == "#":
                    count += 1
    print(count)

=======
Suggestion 4

def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i == 0 and j == 0:
                    if S[i][j+1] == '#' and S[i+1][j] == '#':
                        count += 1
                elif i == 0 and j == 8:
                    if S[i][j-1] == '#' and S[i+1][j] == '#':
                        count += 1
                elif i == 8 and j == 0:
                    if S[i][j+1] == '#' and S[i-1][j] == '#':
                        count += 1
                elif i == 8 and j == 8:
                    if S[i][j-1] == '#' and S[i-1][j] == '#':
                        count += 1
                elif i == 0:
                    if S[i][j-1] == '#' and S[i][j+1] == '#' and S[i+1][j] == '#':
                        count += 1
                elif i == 8:
                    if S[i][j-1] == '#' and S[i][j+1] == '#' and S[i-1][j] == '#':
                        count += 1
                elif j == 0:
                    if S[i-1][j] == '#' and S[i+1][j] == '#' and S[i][j+1] == '#':
                        count += 1
                elif j == 8:
                    if S[i-1][j] == '#' and S[i+1][j] == '#' and S[i][j-1] == '#':
                        count += 1
                else:
                    if S[i-1][j] == '#' and S[i+1][j] == '#' and S[i][j-1] == '#' and S[i][j+1] == '#':
                        count += 1
    print(count)

=======
Suggestion 5

def main():
    s = []
    for i in range(9):
        s.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i == 0:
                    if j == 0:
                        if s[i+1][j] == '#' and s[i][j+1] == '#' and s[i+1][j+1] == '#':
                            count += 1
                    elif j == 8:
                        if s[i+1][j] == '#' and s[i][j-1] == '#' and s[i+1][j-1] == '#':
                            count += 1
                    else:
                        if s[i+1][j] == '#' and s[i][j-1] == '#' and s[i][j+1] == '#' and s[i+1][j-1] == '#' and s[i+1][j+1] == '#':
                            count += 1
                elif i == 8:
                    if j == 0:
                        if s[i-1][j] == '#' and s[i][j+1] == '#' and s[i-1][j+1] == '#':
                            count += 1
                    elif j == 8:
                        if s[i-1][j] == '#' and s[i][j-1] == '#' and s[i-1][j-1] == '#':
                            count += 1
                    else:
                        if s[i-1][j] == '#' and s[i][j-1] == '#' and s[i][j+1] == '#' and s[i-1][j-1] == '#' and s[i-1][j+1] == '#':
                            count += 1
                else:
                    if j == 0:
                        if s[i-1][j] == '#' and s[i+1][j] == '#' and s[i][j+1] == '#' and s[i-1][j+1] == '#' and s[i+1][j+1] == '#':
                            count += 1
                    elif j == 8:
                        if s[i-1][j] == '#' and s[i+1][j] == '#' and s[i][j-1] == '#' and s[i-1][j

=======
Suggestion 6

def main():
    # 读取输入
    s_list = []
    for i in range(9):
        s_list.append(input())
    # print(s_list)

    # 遍历所有的格子
    count = 0
    for i in range(9):
        for j in range(9):
            # 顶点有棋子
            if s_list[i][j] == "#":
                # 向右下角遍历
                for k in range(1, 9 - max(i, j)):
                    if s_list[i + k][j + k] == "#":
                        # 向左下角遍历
                        for l in range(1, min(j, 9 - i)):
                            if s_list[i + l][j - l] == "#":
                                # 向左上角遍历
                                for m in range(1, min(i, j)):
                                    if s_list[i - m][j - m] == "#":
                                        # 向右上角遍历
                                        for n in range(1, min(9 - i, j)):
                                            if s_list[i + n][j - n] == "#":
                                                count += 1
    print(count)

=======
Suggestion 7

def problem275_c():
    pass

=======
Suggestion 8

def find_square(board):
    # 从左上角开始遍历
    length = len(board)
    result = 0
    for i in range(length):
        for j in range(length):
            if board[i][j] == '#':
                # 从该点出发，遍历右边和下边的所有点
                for k in range(j+1, length):
                    if board[i][k] == '#':
                        for l in range(i+1, length):
                            if board[l][j] == '#' and board[l][k] == '#':
                                result += 1
    return result

=======
Suggestion 9

def main():
    s = []
    for i in range(9):
        s.append(input())
    #print(s)
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i+1 < 9 and j+1 < 9:
                    if s[i+1][j] == '#' and s[i][j+1] == '#' and s[i+1][j+1] == '#':
                        count += 1
    print(count)

=======
Suggestion 10

def main():
    # 读入数据
    lines = []
    for i in range(9):
        lines.append(input())
    # 计算
    count = 0
    for i in range(9):
        for j in range(9):
            if lines[i][j] == '#':
                if i == 0:
                    continue
                if j == 0:
                    continue
                if lines[i - 1][j - 1] == '#':
                    if lines[i - 1][j] == '#':
                        if lines[i][j - 1] == '#':
                            count += 1
    # 输出结果
    print(count)

main()
