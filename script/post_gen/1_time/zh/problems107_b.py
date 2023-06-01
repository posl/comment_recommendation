Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find_row_white(row):
    for i in range(len(row)):
        if row[i] == '#':
            return False
    return True

=======
Suggestion 2

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())

    # 从上往下找，找到第一个有黑色的行
    for i in range(H):
        if '#' in a[i]:
            first_black_row = i
            break

    # 从下往上找，找到第一个有黑色的行
    for i in range(H-1, -1, -1):
        if '#' in a[i]:
            last_black_row = i
            break

    # 从左往右找，找到第一个有黑色的列
    for i in range(W):
        if '#' in [a[j][i] for j in range(H)]:
            first_black_col = i
            break

    # 从右往左找，找到第一个有黑色的列
    for i in range(W-1, -1, -1):
        if '#' in [a[j][i] for j in range(H)]:
            last_black_col = i
            break

    # 输出结果
    for i in range(first_black_row, last_black_row+1):
        print(a[i][first_black_col:last_black_col+1])

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]

    row = [False] * h
    col = [False] * w
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True

    for i in range(h):
        if row[i]:
            for j in range(w):
                if col[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 5

def problems107_b():
    pass

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    h = [False] * H
    w = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                h[i] = True
                w[j] = True
    for i in range(H):
        if h[i]:
            for j in range(W):
                if w[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[0][3])
    #print(a[0][4])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[1][3])
    #print(a[1][4])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[2][3])
    #print(a[2][4])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[3][3])
    #print(a[3][4])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[4][3])
    #print(a[4][4])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[5][3])
    #print(a[5][4])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[6][3])
    #print(a[6][4])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[7][3])
    #print(a[7][4])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[8][2])
    #print(a[8][3])
    #print(a[8][4])
    #print(a[9][0])
    #print(a[9][1])
    #print(a[9][2])
    #print(a[9][3])
    #print(a[9][4])
    #print(a[10][0])
    #print(a[10

=======
Suggestion 8

def main():
    # 读入数据
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    # 判断每行是否有黑格子
    # 判断每列是否有黑格子
    # 如果有，则输出
    # 如果没有，则不输出
    ans = []
    for i in range(h):
        if '#' in a[i]:
            ans.append(a[i])

    for i in range(w):
        for j in range(h):
            if ans[j][i] == '#':
                break
        else:
            continue
        break
    else:
        ans = []

    # 输出结果
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 9

def input_data():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    return H, W, a
