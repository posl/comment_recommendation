Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #input
    squares = []
    for i in range(9):
        squares.append(input())
    #solve
    count = 0
    for i in range(8):
        for j in range(8):
            if squares[i][j] == '#' and squares[i][j+1] == '#' and squares[i+1][j] == '#' and squares[i+1][j+1] == '#':
                count += 1
    #output
    print(count)

=======
Suggestion 2

def main():
    S = []
    for i in range(9):
        S.append(input())

    count = 0

    for i in range(9):
        for j in range(9):
            if S[i][j] == '#':
                if i <= 7 and j <= 7:
                    if S[i + 1][j] == '#' and S[i][j + 1] == '#' and S[i + 1][j + 1] == '#':
                        count += 1
                if i >= 1 and j >= 1:
                    if S[i - 1][j] == '#' and S[i][j - 1] == '#' and S[i - 1][j - 1] == '#':
                        count += 1
                if i <= 7 and j >= 1:
                    if S[i + 1][j] == '#' and S[i][j - 1] == '#' and S[i + 1][j - 1] == '#':
                        count += 1
                if i >= 1 and j <= 7:
                    if S[i - 1][j] == '#' and S[i][j + 1] == '#' and S[i - 1][j + 1] == '#':
                        count += 1

    print(count)

=======
Suggestion 3

def get_input():
    input_str = []
    for i in range(9):
        input_str.append(input())
    return input_str

=======
Suggestion 4

def main():
    matrix = []
    for i in range(9):
        matrix.append(input())
    count = 0
    for i in range(1, 8):
        for j in range(1, 8):
            if matrix[i][j] == "#":
                if matrix[i-1][j-1] == "#" and matrix[i-1][j] == "#" and matrix[i][j-1] == "#":
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    board = [input() for _ in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == '#':
                cnt += 1
    print(cnt)

=======
Suggestion 6

def is_chessboard(cell):
    if cell == '#':
        return True
    else:
        return False

=======
Suggestion 7

def main():
    s = []
    for i in range(9):
        s.append(input())

    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                continue
            if i - 1 >= 0 and j - 1 >= 0 and s[i - 1][j - 1] == '.':
                continue
            if i - 1 >= 0 and s[i - 1][j] == '.':
                continue
            if i - 1 >= 0 and j + 1 < 9 and s[i - 1][j + 1] == '.':
                continue
            if j - 1 >= 0 and s[i][j - 1] == '.':
                continue
            if j + 1 < 9 and s[i][j + 1] == '.':
                continue
            if i + 1 < 9 and j - 1 >= 0 and s[i + 1][j - 1] == '.':
                continue
            if i + 1 < 9 and s[i + 1][j] == '.':
                continue
            if i + 1 < 9 and j + 1 < 9 and s[i + 1][j + 1] == '.':
                continue
            ans += 1

    print(ans)

=======
Suggestion 8

def main():
    # 读取输入
    input = []
    for i in range(9):
        input.append(input())

    # 处理
    count = 0
    for i in range(9):
        for j in range(9):
            if input[i][j] == '#':
                count += 1

    # 输出结果
    print(count)

main()

=======
Suggestion 9

def problems275_c():
    pass

=======
Suggestion 10

def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())

    # 计算
    # 遍历9*9的格子
    # 如果该格子是#，则遍历该格子的右侧和下侧的格子，如果都是#，则答案+1
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == "#":
                if j < 8 and s[i][j + 1] == "#" and i < 8 and s[i + 1][j] == "#":
                    ans += 1

    # 输出
    print(ans)
