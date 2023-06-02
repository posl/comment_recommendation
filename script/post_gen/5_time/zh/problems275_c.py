Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 1. 读入数据
    # 2. 计算
    # 3. 输出结果
    # 4. 退出程序
    pass

=======
Suggestion 2

def get_num_of_chessboard(s):
    res = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if s[i][j + 1] == '#' and s[i + 1][j] == '#' and s[i + 1][j + 1] == '#':
                        res += 1
    return res

=======
Suggestion 3

def solve():
    s = []
    for i in range(9):
        s.append(input())
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i - 1 >= 0 and j - 1 >= 0 and s[i - 1][j - 1] == '#':
                    if i - 1 >= 0 and j >= 0 and s[i - 1][j] == '#':
                        if i >= 0 and j - 1 >= 0 and s[i][j - 1] == '#':
                            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # 读取输入
    S = []
    for i in range(9):
        S.append(input())

    # 计算
    count = 0
    for r in range(9):
        for c in range(9):
            if S[r][c] == "#":
                if r+1 < 9 and c+1 < 9 and S[r+1][c] == "#" and S[r][c+1] == "#" and S[r+1][c+1] == "#":
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    S = []
    for i in range(9):
        S.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if S[i][j] == "#":
                if i == 0 and j == 0:
                    if S[i][j + 1] == "#" and S[i + 1][j] == "#" and S[i + 1][j + 1] == "#":
                        count += 1
                elif i == 0 and j == 8:
                    if S[i][j - 1] == "#" and S[i + 1][j] == "#" and S[i + 1][j - 1] == "#":
                        count += 1
                elif i == 8 and j == 0:
                    if S[i][j + 1] == "#" and S[i - 1][j] == "#" and S[i - 1][j + 1] == "#":
                        count += 1
                elif i == 8 and j == 8:
                    if S[i][j - 1] == "#" and S[i - 1][j] == "#" and S[i - 1][j - 1] == "#":
                        count += 1
                elif i == 0:
                    if S[i][j - 1] == "#" and S[i][j + 1] == "#" and S[i + 1][j] == "#" and S[i + 1][j - 1] == "#" and S[i + 1][j + 1] == "#":
                        count += 1
                elif i == 8:
                    if S[i][j - 1] == "#" and S[i][j + 1] == "#" and S[i - 1][j] == "#" and S[i - 1][j - 1] == "#" and S[i - 1][j + 1] == "#":
                        count += 1
                elif j == 0:
                    if S[i][j + 1] == "#" and S[i - 1][j] == "#" and S[i + 1][j] == "#" and S[i - 1][j + 1] == "#" and S[i + 1][j + 1] == "#":
                        count +=

=======
Suggestion 6

def main():
    # 读取数据
    data = []
    for i in range(9):
        data.append(list(input()))
    # print(data)

    # 统计棋子个数
    count = 0
    for i in range(9):
        for j in range(9):
            if data[i][j] == "#":
                count += 1
    # print(count)

    # 统计顶点个数
    count2 = 0
    for i in range(9):
        for j in range(9):
            if i < 8 and j < 8:
                if data[i][j] == "#" and data[i + 1][j] == "#" and data[i][j + 1] == "#" and data[i + 1][j + 1] == "#":
                    count2 += 1
    # print(count2)

    # 输出结果
    print(count - count2)

=======
Suggestion 7

def main():
    # 读入数据
    s = []
    for i in range(9):
        s.append(list(input()))
    # 求解
    ans = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if s[i + 1][j] == '#' and s[i][j + 1] == '#' and s[i + 1][j + 1] == '#':
                        ans += 1
    # 输出结果
    print(ans)

=======
Suggestion 8

def read_input():
    try:
        while True:
            yield input()
    except EOFError:
        pass

=======
Suggestion 9

def main():
    s = []
    for i in range(9):
        s.append(input())
    count = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i+1 < 9 and j+1 < 9 and s[i+1][j] == '#' and s[i][j+1] == '#' and s[i+1][j+1] == '#':
                    count += 1
    print(count)

=======
Suggestion 10

def main():
    # 读取输入
    s = []
    for i in range(9):
        s.append(input())

    # 计算
    count = 0
    for r in range(9):
        for c in range(9):
            if s[r][c] == '#':
                if r < 8 and c < 8 and s[r + 1][c + 1] == '#' and s[r + 1][c] == '#' and s[r][c + 1] == '#':
                    count += 1

    # 输出
    print(count)
