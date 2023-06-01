Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_input():
    h, w = input().split()
    h = int(h)
    w = int(w)
    a = []
    for i in range(h):
        a.append(input())
    return h, w, a

=======
Suggestion 3

def solve(h, w, a):
    rows = [False] * h
    cols = [False] * w
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                rows[i] = True
                cols[j] = True
    for i in range(h):
        if rows[i]:
            for j in range(w):
                if cols[j]:
                    print(a[i][j], end='')
            print('')

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(list(input()))
    del_row = []
    del_col = []
    for i in range(H):
        if a[i].count("#") == 0:
            del_row.append(i)
    for j in range(W):
        flag = True
        for i in range(H):
            if a[i][j] == "#":
                flag = False
                break
        if flag:
            del_col.append(j)
    for i in range(H):
        if i not in del_row:
            for j in range(W):
                if j not in del_col:
                    print(a[i][j], end="")
            print()

=======
Suggestion 5

def problems107_b():
    H, W = map(int, input().split())
    a = [input() for i in range(H)]
    b = []
    for i in range(H):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        t = []
        for j in range(len(b)):
            t.append(b[j][i])
        if '#' in t:
            c.append(t)
    for i in range(len(c)):
        print(''.join(c[i]))

=======
Suggestion 6

def problems107_b(H, W, a):
    #print(H, W, a)
    ans = []
    for i in range(H):
        if not '#' in a[i]:
            continue
        ans.append(a[i])
    ans = list(zip(*ans))
    for i in range(len(ans)):
        if not '#' in ans[i]:
            continue
        ans[i] = ''.join(ans[i])
    ans = list(zip(*ans))
    for i in range(len(ans)):
        print(''.join(ans[i]))

=======
Suggestion 7

def main():
    # 读入数据
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    # 检查是否有黑色方块
    exist_black = False
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                exist_black = True

    # 压缩网格
    ans = []
    for i in range(h):
        if '#' in a[i]:
            ans.append(a[i].replace('.', ''))
    # 转置
    ans = list(map(list, zip(*ans)))
    # 再次压缩
    ans2 = []
    for i in range(w):
        if '#' in ans[i]:
            ans2.append(ans[i])
    # 转置
    ans2 = list(map(list, zip(*ans2)))

    # 输出结果
    if exist_black:
        print('\n'.join([''.join(ans2[i]) for i in range(len(ans2))]))
    else:
        print('')

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [list(input()) for i in range(h)]
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
                    print(a[i][j], end = '')
            print()

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    h_list = [0 for _ in range(h)]
    w_list = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                h_list[i] = 1
                w_list[j] = 1
    for i in range(h):
        if h_list[i] == 1:
            for j in range(w):
                if w_list[j] == 1:
                    print(a[i][j], end='')
            print()
