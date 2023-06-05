Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    H, W = input().split()
    H = int(H)
    W = int(W)
    a = []
    for i in range(H):
        a.append(input())
    return H, W, a

=======
Suggestion 2

def get_input():
    # 获取输入
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    return H, W, a

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [list(input()) for i in range(h)]
    a = [list(i) for i in zip(*a) if i.count(".") != h]
    a = [list(i) for i in zip(*a) if i.count(".") != w]
    for i in a:
        print("".join(i))

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(input()))
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

def main():
    pass

=======
Suggestion 6

def main():
    #读入数据
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    #判断每一行是否都是白色方块
    #如果是白色方块，就删除该行
    #如果不是，就保留该行
    #判断每一列是否都是白色方块
    #如果是白色方块，就删除该列
    #如果不是，就保留该列
    #输出最终结果
    for i in range(h):
        if a[i].count('.') == w:
            a[i] = ''
    for j in range(w):
        if [a[i][j] for i in range(h)].count('.') == h:
            for i in range(h):
                a[i] = a[i][:j] + a[i][j + 1:]
    for i in range(h):
        if a[i] != '':
            print(a[i])

=======
Suggestion 7

def main():
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
Suggestion 8

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(list(input()))
    h = [0] * H
    w = [0] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                h[i] = 1
                w[j] = 1
    for i in range(H):
        if h[i] == 1:
            for j in range(W):
                if w[j] == 1:
                    print(a[i][j], end = '')
            print()
main()

=======
Suggestion 9

def solve():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for j in range(W):
        if '#' in [b[i][j] for i in range(len(b))]:
            c.append([b[i][j] for i in range(len(b))])
    for i in range(len(c)):
        print(''.join(c[i]))

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][1])
    #print(a[2][1])
    #print(a[3][1])
    #print(a[4][1])
    #print(a[5][1])
    #print(a[6][1])
    #print(a[0][2])
    #print(a[1][2])
    #print(a[2][2])
    #print(a[3][2])
    #print(a[4][2])
    #print(a[5][2])
    #print(a[6][2])
    #print(a[0][3])
    #print(a[1][3])
    #print(a[2][3])
    #print(a[3][3])
    #print(a[4][3])
    #print(a[5][3])
    #print(a[6][3])
    #print(a[0][4])
    #print(a[1][4])
    #print(a[2][4])
    #print(a[3][4])
    #print(a[4][4])
    #print(a[5][4])
    #print(a[6][4])
    #print(a[0][5])
    #print(a[1][5])
    #print(a[2][5])
    #print(a[3][5])
    #print(a[4][5])
    #print(a[5][5])
    #print(a[6][5])
    #print(a[0][6])
    #print(a[1][6])
    #print(a[2][6])
    #print(a[3][6])
    #print(a[4][6])
    #print(a[5][6])
    #print(a[6][6])
    #print(a[0][7])
    #print(a[1][7])
    #print(a[2][7])
    #print(a[3][7])
    #print(a[4][7])
    #print(a[5][7])
    #print(a[6][7])
    #print(a[0][8])
    #print(a[1][8])
