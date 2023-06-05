Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if i == 0:
                    a = i + 1
                else:
                    a = i
                if j == 0:
                    b = j + 1
                else:
                    b = j
                if i == 9:
                    c = i + 1
                else:
                    c = i + 2
                if j == 9:
                    d = j + 1
                else:
                    d = j + 2
    print(a, b)
    print(c, d)

=======
Suggestion 2

def main():
    # 读入数据
    s = []
    for i in range(10):
        s.append(input())
    # 找到最左边的#和最右边的#
    left = 10
    right = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                left = min(left, j)
                right = max(right, j)
    # 找到最上面的#和最下面的#
    top = 10
    bottom = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                top = min(top, i)
                bottom = max(bottom, i)
    # 根据最左边的#和最右边的#，找到A和B
    A = 10 - (right - left + 1) + 1
    B = 10
    # 根据最上面的#和最下面的#，找到C和D
    C = 10 - (bottom - top + 1) + 1
    D = 10
    # 打印结果
    print(A, B)
    print(C, D)

=======
Suggestion 3

def solve():
    # 从标准输入读取数据.
    # 10行
    s = []
    for i in range(10):
        s.append(input())

    # 从s中找到第一个有#的行
    for i in range(10):
        if '#' in s[i]:
            # 从s中找到第一个有#的列
            for j in range(10):
                if s[i][j] == '#':
                    # 找到第一个有#的行i和列j
                    # 从s中找到最后一个有#的行
                    for k in range(9, -1, -1):
                        if '#' in s[k]:
                            # 从s中找到最后一个有#的列
                            for l in range(9, -1, -1):
                                if s[k][l] == '#':
                                    # 找到最后一个有#的行k和列l
                                    # 打印结果
                                    print(i + 1, l + 1)
                                    print(k + 1, j + 1)
                                    return

=======
Suggestion 4

def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                print(i + 1, j + 1)
                return

=======
Suggestion 5

def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if s[i] == '..........':
            s[i] = '..........'
        elif s[i] == '##########':
            s[i] = '##########'
        else:
            s[i] = s[i][1:9]
    for i in range(10):
        print(s[i])

=======
Suggestion 6

def problem269_b():
    pass

=======
Suggestion 7

def get_input():
    n = 10
    s = []
    for i in range(n):
        s.append(input())
    return s

=======
Suggestion 8

def main():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i+1,j+1)
                break
        else:
            continue
        break
    for i in range(9,-1,-1):
        for j in range(9,-1,-1):
            if s[i][j] == '#':
                print(i+1,j+1)
                break
        else:
            continue
        break

=======
Suggestion 9

def main():
    s = []
    for i in range(10):
        s.append(list(input()))
    # print(s)
    # print(s[0][0])
    # print(s[1][0])
    # print(s[2][0])
    # print(s[3][0])
    # print(s[4][0])
    # print(s[5][0])
    # print(s[6][0])
    # print(s[7][0])
    # print(s[8][0])
    # print(s[9][0])
    # print(s[0][1])
    # print(s[1][1])
    # print(s[2][1])
    # print(s[3][1])
    # print(s[4][1])
    # print(s[5][1])
    # print(s[6][1])
    # print(s[7][1])
    # print(s[8][1])
    # print(s[9][1])
    # print(s[0][2])
    # print(s[1][2])
    # print(s[2][2])
    # print(s[3][2])
    # print(s[4][2])
    # print(s[5][2])
    # print(s[6][2])
    # print(s[7][2])
    # print(s[8][2])
    # print(s[9][2])
    # print(s[0][3])
    # print(s[1][3])
    # print(s[2][3])
    # print(s[3][3])
    # print(s[4][3])
    # print(s[5][3])
    # print(s[6][3])
    # print(s[7][3])
    # print(s[8][3])
    # print(s[9][3])
    # print(s[0][4])
    # print(s[1][4])
    # print(s[2][4])
    # print(s[3][4])
    # print(s[4][4])
    # print(s[5][4])
    # print(s[6][4])
    # print(s[7][4])
    # print(s[8][4])
    # print(s[9][4])
    # print(s[0][5])
    # print(s[1][5])
    # print(s[2][

=======
Suggestion 10

def main():
    s = []
    for i in range(10):
        s.append(input())
    print(s)
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                print(i, j)
