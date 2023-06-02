Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[3][0])
    #print(a[3][1])
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
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[0][3])
    #print(a[0][4])
    #print(a[0][5])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1

=======
Suggestion 2

def problems107_b():
    pass

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]

    # 各行各列に黒マスがあるかどうかのフラグ
    row = [False] * H
    col = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True

    # どの行もどの列も黒マスがあるかどうか
    for i in range(H):
        if row[i]:
            for j in range(W):
                if col[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 4

def main():
    #print("请输入行数H和列数W：")
    H, W = map(int, input().split())
    #print("请输入网格：")
    a = [list(input()) for i in range(H)]
    #print("输入的网格为：")
    #print(a)
    #print("网格的行数为：",len(a))
    #print("网格的列数为：",len(a[0]))
    #print("网格的第一行为：")
    #print(a[0])
    #print("网格的第一列为：")
    #print([x[0] for x in a])
    row = [0]*H
    col = [0]*W
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                row[i] = 1
                col[j] = 1
    #print("网格的行状态为：")
    #print(row)
    #print("网格的列状态为：")
    #print(col)
    for i in range(H):
        if row[i] == 1:
            for j in range(W):
                if col[j] == 1:
                    print(a[i][j], end="")
            print()

=======
Suggestion 5

def main():
    #读入数据
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    #处理数据
    #行列都是白色的行列
    white_rows = [i for i in range(h) if all(a[i][j] == '.' for j in range(w))]
    white_cols = [j for j in range(w) if all(a[i][j] == '.' for i in range(h))]
    #输出数据
    for i in range(h):
        if i in white_rows:
            continue
        for j in range(w):
            if j in white_cols:
                continue
            print(a[i][j], end='')
        print()

=======
Suggestion 6

def solve():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
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
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for j in range(W):
        if '#' in [a[i][j] for i in range(H)]:
            c.append([a[i][j] for i in range(H)])
    for i in range(len(b)):
        print(''.join([c[j][i] for j in range(len(c))]))

=======
Suggestion 8

def get_input():
    H, W = map(int, input().split())
    a = []
    for _ in range(H):
        a.append(list(input()))
    return H, W, a

=======
Suggestion 9

def get_matrix():
    H, W = map(int, input().split())
    matrix = []
    for i in range(H):
        row = input()
        matrix.append(row)
    return matrix
