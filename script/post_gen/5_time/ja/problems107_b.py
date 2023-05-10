Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    rows = [False] * H
    columns = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                rows[i] = True
                columns[j] = True
    for i in range(H):
        if rows[i]:
            for j in range(W):
                if columns[j]:
                    print(a[i][j], end="")
            print()

=======
Suggestion 2

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
Suggestion 3

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    # 行の削除
    a = [row for row in a if "#" in row]
    # 列の削除
    a = list(map(list, zip(*a)))
    a = [col for col in a if "#" in col]
    a = list(map(list, zip(*a)))

    for row in a:
        print("".join(row))

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    h = []
    for i in range(H):
        if a[i].count(".") != W:
            h.append(a[i])
    w = []
    for i in range(W):
        cnt = 0
        for j in range(H):
            if a[j][i] == ".":
                cnt += 1
        if cnt != H:
            w.append(i)
    for i in range(len(h)):
        for j in range(len(w)):
            print(h[i][w[j]], end="")
        print()

=======
Suggestion 5

def main():
    import sys
    # input = sys.stdin.readline  #文字列では使わない
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    # print(a)
    # print(a[0][0])
    # print(a[1][0])
    # print(a[0][1])
    # print(a[1][1])
    # print(a[0][2])
    # print(a[1][2])
    # print(a[0][3])
    # print(a[1][3])
    # print(a[0][4])
    # print(a[1][4])
    # print(a[0][5])
    # print(a[1][5])
    # print(a[0][6])
    # print(a[1][6])
    # print(a[0][7])
    # print(a[1][7])
    # print(a[0][8])
    # print(a[1][8])
    # print(a[0][9])
    # print(a[1][9])

    # print(a[0][0])
    # print(a[0][1])
    # print(a[0][2])
    # print(a[0][3])
    # print(a[0][4])
    # print(a[0][5])
    # print(a[0][6])
    # print(a[0][7])
    # print(a[0][8])
    # print(a[0][9])
    # print(a[1][0])
    # print(a[1][1])
    # print(a[1][2])
    # print(a[1][3])
    # print(a[1][4])
    # print(a[1][5])
    # print(a[1][6])
    # print(a[1][7])
    # print(a[1][8])
    # print(a[1][9])
    # print(a[2][0])
    # print(a[2][1])
    # print(a[2][2])
    # print(a[2][3])
    # print(a[2][4])
    # print(a[2][5])
    # print(a[2][6])
    # print(a[2][7])
    # print(a[2][8])
    # print(a[2

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)] # 2次元配列の入力の受け取り
    #print(a)
    #print(a[0][0])

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

    #print("a[0][0] = " + a[0][0])
    #print("a[0][1] = " + a[0][1])
    #print("a[0][2] = " + a[0][2])
    #print("a[0][3] = " + a[0][3])
    #print("a[0][4] = " + a[0][4])

    #print("a[1][0] = " + a[1][0])
    #print("a[1][1] = " + a[1][1])
    #print("a[1][2] = " + a[1][2])
    #print("a[1][3] = " + a[1][3])
    #print("a[1][4] = " + a[1][4])

    #print("a[2][0] = " + a[2][0])
    #print("a[2][

=======
Suggestion 7

def inputToArray(input):
    return [input() for i in range(H)]

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    for i in range(h):
        if a[i] == "." * w:
            a[i] = ""
    for j in range(w):
        if all(a[i][j] == "." for i in range(h)):
            for i in range(h):
                a[i] = a[i][:j] + a[i][j+1:]
    for i in range(h):
        print(a[i])

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    for i in range(h):
        if a[i].count("#") == w:
            continue
        else:
            for j in range(w):
                if a[i][j] == "#":
                    continue
                else:
                    if j == w-1:
                        a[i] = ""
                    else:
                        a[i] = a[i][:j] + a[i][j+1:]
                    w -= 1
                    break
    for k in range(w):
        if all(a[l][k] == "#" for l in range(h)):
            continue
        else:
            for m in range(h):
                if a[m][k] == "#":
                    continue
                else:
                    if m == h-1:
                        for n in range(h):
                            a[n] = a[n][:k] + a[n][k+1:]
                    else:
                        for n in range(h):
                            a[n] = a[n][:k] + a[n][k+1:]
                    h -= 1
                    break
    for o in range(h):
        print(a[o])

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    #print(a)

    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])

    #print(a[0][0] == a[0][1])
    #print(a[0][0] == a[1][0])
    #print(a[0][0] == a[1][1])

    #print(a[0][1] == a[1][0])
    #print(a[0][1] == a[1][1])

    #print(a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    #print(a[0][0] == a[0][1] == a[1][0] == a[1][1])

    for i in range(H):
        for j in range(W):
            if a[i][j] == ".":
                if i == 0:
                    if j == 0:
                        if a[i][j] == a[i][j+1] == a[i+1][j] == a[i+1
