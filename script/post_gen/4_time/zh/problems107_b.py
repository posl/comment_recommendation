Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if '#' in a[i]:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        d = []
        for j in range(len(b)):
            d.append(b[j][i])
        if '#' in d:
            c.append(d)
    for i in range(len(c)):
        print(''.join(c[i]))

main()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    rows = [False] * H
    cols = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                rows[i] = True
                cols[j] = True
    for i in range(H):
        if rows[i]:
            for j in range(W):
                if cols[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 3

def problem107_b():
    pass

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    # print(a)
    # print(len(a))
    # print(len(a[0]))
    # print(a[0][0])
    # print(a[1][1])
    # print(a[2][2])
    # print(a[3][3])
    # print(a[4][4])
    # print(a[5][5])
    # print(a[6][6])
    # print(a[7][7])
    # print(a[8][8])
    # print(a[9][9])
    # print(a[10][10])
    # print(a[11][11])
    # print(a[12][12])
    # print(a[13][13])
    # print(a[14][14])
    # print(a[15][15])
    # print(a[16][16])
    # print(a[17][17])
    # print(a[18][18])
    # print(a[19][19])
    # print(a[20][20])
    # print(a[21][21])
    # print(a[22][22])
    # print(a[23][23])
    # print(a[24][24])
    # print(a[25][25])
    # print(a[26][26])
    # print(a[27][27])
    # print(a[28][28])
    # print(a[29][29])
    # print(a[30][30])
    # print(a[31][31])
    # print(a[32][32])
    # print(a[33][33])
    # print(a[34][34])
    # print(a[35][35])
    # print(a[36][36])
    # print(a[37][37])
    # print(a[38][38])
    # print(a[39][39])
    # print(a[40][40])
    # print(a[41][41])
    # print(a[42][42])
    # print(a[43][43])
    # print(a[44][44])
    # print(a[45][45])
    # print(a[46][46])
    # print(a[47][47])
    # print(a[48][48])
    # print(a[49][49])
    # print(a

=======
Suggestion 5

def get_input():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    return H, W, a

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    row = [False] * H
    col = [False] * W

    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True

    for i in range(H):
        if row[i]:
            for j in range(W):
                if col[j]:
                    print(a[i][j], end='')
            print()

=======
Suggestion 7

def problems107_b():
    return None

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    hlist = []
    wlist = []
    for i in range(h):
        if a[i].count('#') == 0:
            hlist.append(i)
    for j in range(w):
        if [a[i][j] for i in range(h)].count('#') == 0:
            wlist.append(j)
    for i in range(h):
        if i not in hlist:
            print(''.join([a[i][j] for j in range(w) if j not in wlist]))

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    #print(a)
    row = [False] * H
    col = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                row[i] = True
                col[j] = True
    #print(row)
    #print(col)
    for i in range(H):
        if row[i]:
            for j in range(W):
                if col[j]:
                    print(a[i][j], end='')
            print()
