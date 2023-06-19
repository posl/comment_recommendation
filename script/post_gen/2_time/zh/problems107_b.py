Synthesizing 10/10 solutions

=======
Suggestion 1

def problems107_b(H, W, a):
    result = []
    for i in range(H):
        result.append([])
        for j in range(W):
            result[i].append('.')
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                for k in range(W):
                    result[i][k] = '#'
                for k in range(H):
                    result[k][j] = '#'
    return result

=======
Suggestion 2

def main():
    # 读入数据
    H, W = map(int, input().split())
    # 读入矩阵
    a = [input() for _ in range(H)]
    # 从上往下遍历
    for i in range(H):
        # 从左往右遍历
        for j in range(W):
            # 如果遇到黑色方块，则跳过
            if a[i][j] == "#":
                break
        # 如果遇到黑色方块，则跳过
        if a[i][j] == "#":
            continue
        # 如果该行只有白色方块，则删除该行
        else:
            del a[i]
            # 删除该行后，行数减一
            H -= 1
            # 因为删除了一行，所以要减一，以免跳过下一行
            i -= 1
    # 从左往右遍历
    for j in range(W):
        # 从上往下遍历
        for i in range(H):
            # 如果遇到黑色方块，则跳过
            if a[i][j] == "#":
                break
        # 如果遇到黑色方块，则跳过
        if a[i][j] == "#":
            continue
        # 如果该列只有白色方块，则删除该列
        else:
            # 从上往下删除该列
            for i in range(H):
                # 删除该列
                a[i] = a[i][:j] + a[i][j + 1:]
            # 删除该列后，列数减一
            W -= 1
            # 因为删除了一列，所以要减一，以免跳过下一列
            j -= 1
    # 输出最终状态
    for i in range(H):
        print(a[i])

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    #print(a)
    #print(a[0])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[0][3])
    #print(a[0][4])
    #print(a[0][5])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[1][3])
    #print(a[1][4])
    #print(a[1][5])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[2][3])
    #print(a[2][4])
    #print(a[2][5])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[3][3])
    #print(a[3][4])
    #print(a[3][5])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[4][3])
    #print(a[4][4])
    #print(a[4][5])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[5][3])
    #print(a[5][4])
    #print(a[5][5])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[6][3])
    #print(a[6][4])
    #print(a[6][5])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[7][3])
    #print(a[7][4])
    #print(a[7][5])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[8][2])
    #

=======
Suggestion 4

def get_input():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    return h, w, grid

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    row = [0] * H
    col = [0] * W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                row[i] = 1
                col[j] = 1
    for i in range(H):
        if row[i] == 1:
            for j in range(W):
                if col[j] == 1:
                    print(grid[i][j], end = '')
            print()

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    a = [i for i in a if "#" in i]
    a = [list(i) for i in zip(*a)]
    a = [i for i in a if "#" in i]
    a = [list(i) for i in zip(*a)]
    for i in a:
        print("".join(i))

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(input())
    b = []
    for i in range(h):
        if not a[i] == "."*w:
            b.append(a[i])
    c = []
    for i in range(w):
        flag = True
        for j in range(len(b)):
            if b[j][i] == "#":
                flag = False
                break
        if flag:
            c.append(i)
    for i in range(len(b)):
        for j in range(len(c)):
            print(b[i][c[j]],end="")
        print()

=======
Suggestion 8

def find_column(a, j):
    for i in range(len(a)):
        if a[i][j] == '#':
            return False
    return True

=======
Suggestion 9

def problems107_b():
    return None

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    b = []
    for i in range(H):
        if a[i].count("#") != 0:
            b.append(a[i])
    c = []
    for i in range(W):
        tmp = ""
        for j in range(len(b)):
            tmp += b[j][i]
        if tmp.count("#") != 0:
            c.append(tmp)
    for i in range(len(c)):
        print(c[i])
